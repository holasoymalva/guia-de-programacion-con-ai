#!/usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path
from dotenv import load_dotenv
import chromadb
import anthropic

# Cargar variables de entorno
load_dotenv()

# Verificar API Key
API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    print("Error: No se encontró la variable ANTHROPIC_API_KEY en las variables de entorno o en el archivo .env.")
    print("Por favor, crea un archivo .env en esta carpeta y agrega tu clave:")
    print("ANTHROPIC_API_KEY=tu_api_key_aquí")
    sys.exit(1)

# Crear directorio de datos de prueba si no existe
DIR_DATOS = Path("./datos_prueba")
DIR_DATOS.mkdir(exist_ok=True)

# Crear archivos de ejemplo si la carpeta está vacía
if not any(DIR_DATOS.iterdir()):
    print("Creando archivos de texto de prueba en la carpeta 'datos_prueba/'...")
    (DIR_DATOS / "politica_vacaciones.txt").write_text(
        "Política de Vacaciones: Los empleados a tiempo completo en Acme Corp tienen derecho a 15 días hábiles de vacaciones al año después de completar un año de antigüedad. Las solicitudes deben enviarse con 2 semanas de anticipación.",
        encoding="utf-8"
    )
    (DIR_DATOS / "politica_gastos.txt").write_text(
        "Política de Gastos: Los viáticos por concepto de comidas de viaje están limitados a un máximo de $50 USD diarios. Se requiere presentar factura electrónica oficial dentro de los primeros 5 días hábiles después de regresar.",
        encoding="utf-8"
    )

# Inicializar clientes
# Usamos un cliente persistente en local para ver los archivos creados en disco
chroma_client = chromadb.PersistentClient(path="./vector_db")
anthropic_client = anthropic.Anthropic(api_key=API_KEY)

# Crear o recuperar la colección de documentos
# ChromaDB por defecto utiliza un modelo integrado de embeddings (all-MiniLM-L6-v2) en local 
# por lo que no es estrictamente obligatorio usar la API de OpenAI para generar embeddings en esta demo.
coleccion = chroma_client.get_or_create_collection(
    name="documentos_corporativos",
    metadata={"hnsw:space": "cosine"}
)

def indexar_documentos(directorio: str):
    """Lee archivos .txt del directorio, los divide en chunks e indexa en ChromaDB."""
    print(f"\nIndexando archivos en '{directorio}'...")
    documentos = []
    ids = []
    metadatas = []
    
    dir_path = Path(directorio)
    archivos = list(dir_path.glob("**/*.txt"))
    
    if not archivos:
        print("No se encontraron archivos .txt para indexar.")
        return
        
    for idx, ruta in enumerate(archivos):
        try:
            contenido = ruta.read_text(encoding='utf-8')
            # Chunking simple basado en palabras (chunks de 50 palabras con overlap de 10)
            palabras = contenido.split()
            chunk_size = 50
            overlap = 10
            
            chunks = []
            for i in range(0, len(palabras), chunk_size - overlap):
                chunk = ' '.join(palabras[i:i + chunk_size])
                if chunk.strip():
                    chunks.append(chunk)
                    
            for j, chunk in enumerate(chunks):
                chunk_id = f"{ruta.stem}_{j}"
                documentos.append(chunk)
                ids.append(chunk_id)
                metadatas.append({"fuente": ruta.name, "chunk_index": j})
                print(f" -> Chunk generado: '{chunk_id}'")
        except Exception as e:
            print(f"Error al procesar archivo {ruta.name}: {e}")
            
    if documentos:
        # Añadir a la base de datos (Chroma calcula los embeddings automáticamente)
        coleccion.add(documents=documentos, ids=ids, metadatas=metadatas)
        print(f"¡Indexación terminada! Se agregaron {len(documentos)} chunks a la base de datos.")
    else:
        print("No se generaron chunks válidos.")

def preguntar(pregunta: str, top_k: int = 2) -> str:
    """Busca en ChromaDB y envía los resultados a Claude para generar una respuesta grounded."""
    print(f"\nPregunta del usuario: '{pregunta}'")
    print("Buscando fragmentos relevantes en la base de datos vectorial...")
    
    # Consultar la colección
    resultados = coleccion.query(query_texts=[pregunta], n_results=top_k)
    
    documentos_encontrados = resultados.get('documents', [[]])[0]
    fuentes_encontradas = resultados.get('metadatas', [[]])[0]
    
    if not documentos_encontrados:
        return "No se encontró información relevante en los documentos indexados."
        
    # Construir el contexto
    contexto = ""
    for idx, doc in enumerate(documentos_encontrados):
        fuente = fuentes_encontradas[idx].get("fuente", "Desconocida")
        contexto += f"--- Inicio Fragmento (Fuente: {fuente}) ---\n{doc}\n--- Fin Fragmento ---\n\n"
        
    print(f"Se encontraron {len(documentos_encontrados)} fragmentos relevantes. Enviando a Claude...")
    
    # Prompt de RAG que restringe al modelo a usar solo el contexto provisto
    prompt = f"""Responde a la pregunta basándote ÚNICAMENTE en el contexto de documentos proporcionado abajo.
Si la respuesta no se puede deducir del contexto provisto, responde exactamente con la frase: "No encontré esa información en los documentos." y no inventes datos.

CONTEXTO DE DOCUMENTOS:
{contexto}

PREGUNTA: {pregunta}
Respuesta en español:"""

    try:
        respuesta = anthropic_client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return respuesta.content[0].text
    except Exception as e:
        return f"Error al generar la respuesta con Claude: {e}"

def main():
    # 1. Ejecutar indexación de los archivos de prueba creados
    indexar_documentos("./datos_prueba")
    
    # 2. Hacer preguntas de prueba
    res1 = preguntar("¿Cuántos días de vacaciones tienen los empleados?")
    print(f"Respuesta Claude:\n{res1}\n")
    
    res2 = preguntar("¿Cuál es el límite de gastos para comidas de viaje?")
    print(f"Respuesta Claude:\n{res2}\n")
    
    res3 = preguntar("¿Cuál es la política de la empresa sobre el trabajo remoto?")
    print(f"Respuesta Claude:\n{res3}\n")

if __name__ == "__main__":
    main()
