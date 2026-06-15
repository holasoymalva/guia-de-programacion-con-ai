#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import anthropic

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Verificar que la API Key esté presente
API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    print("Error: No se encontró la variable ANTHROPIC_API_KEY en las variables de entorno o en el archivo .env.")
    print("Por favor, crea un archivo .env en esta carpeta y agrega tu clave:")
    print("ANTHROPIC_API_KEY=tu_api_key_aquí")
    sys.exit(1)

client = anthropic.Anthropic(api_key=API_KEY)

def leer_archivos_proyecto(directorio: str, max_archivos: int = 5) -> str:
    # Extensiones de archivos de código que buscaremos
    extensiones = {'.py', '.js', '.ts', '.go', '.rs', '.java', '.json'}
    archivos_leidos = []
    
    directorio_path = Path(directorio)
    if not directorio_path.exists():
        print(f"Advertencia: El directorio '{directorio}' no existe.")
        return ""

    for ruta in directorio_path.rglob('*'):
        if (ruta.is_file() and 
            ruta.suffix in extensiones and
            'node_modules' not in str(ruta) and
            '.git' not in str(ruta) and
            'venv' not in str(ruta) and
            '__pycache__' not in str(ruta) and
            len(archivos_leidos) < max_archivos):
            try:
                # Leer el principio del archivo de código para no saturar tokens
                contenido = ruta.read_text(encoding='utf-8')[:1500]
                archivos_leidos.append(f"### Archivo: {ruta.name}\n```{ruta.suffix[1:]}\n{contenido}\n```")
                print(f"Leído con éxito: {ruta.name}")
            except Exception as e:
                print(f"Error al leer {ruta.name}: {e}")
                
    return "\n\n".join(archivos_leidos)

def generar_readme(directorio: str) -> str:
    print(f"Analizando estructura de código en: {directorio}...")
    codigo = leer_archivos_proyecto(directorio)
    
    if not codigo:
        return "No se encontraron archivos de código compatibles para analizar."

    print("Enviando código recopilado a Claude para generar el README.md...")
    try:
        respuesta = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": f"""Analiza el siguiente código de los archivos del proyecto y genera un README.md profesional, completo y bien estructurado en español.

CÓDIGO FUENTE DEL PROYECTO:
{codigo}

El README.md generado debe incluir de forma obligatoria las siguientes secciones en Markdown estructurado:
1. Título descriptivo del proyecto.
2. Descripción clara y concisa de qué hace y para quién es.
3. Lista de características clave.
4. Instrucciones paso a paso de instalación de dependencias y de ejecución.
5. Estructura física de los archivos del proyecto analizados.
6. Licencia recomendada (MIT).
Usa emojis de forma estratégica para hacerlo visualmente agradable."""
            }]
        )
        return respuesta.content[0].text
    except Exception as e:
        return f"Error al generar el README: {e}"

def main():
    # Usaremos la misma carpeta de este proyecto como demo para analizar
    directorio_a_analizar = "."
    readme_contenido = generar_readme(directorio_a_analizar)
    
    archivo_salida = "README_GENERADO.md"
    try:
        Path(archivo_salida).write_text(readme_contenido, encoding='utf-8')
        print(f"\n¡Éxito! Archivo '{archivo_salida}' generado exitosamente en esta carpeta.")
    except Exception as e:
        print(f"Error al escribir el archivo de salida: {e}")

if __name__ == "__main__":
    main()
