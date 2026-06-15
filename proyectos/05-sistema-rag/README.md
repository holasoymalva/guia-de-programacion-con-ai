# Sistema RAG Completo (Simulación de Base de Datos Vectorial) 🗄️🧠

Este proyecto es un pipeline de **Retrieval-Augmented Generation (RAG)** completo en Python. El script lee archivos de texto plano (`.txt`) de una carpeta local, los fragmenta (chunking), genera embeddings locales e indexa los vectores en una base de datos vectorial local llamada **ChromaDB**. Al realizar preguntas, el script recupera los fragmentos semánticamente más similares y se los entrega a Claude para redactar una respuesta precisa y libre de alucinaciones.

## 🚀 Requisitos de Instalación

1. Asegúrate de tener Python 3.10+ instalado.
2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## 🔑 Configuración de Credenciales

Crea un archivo `.env` en la raíz de esta carpeta y agrega tu clave de API de Anthropic:
```ini
ANTHROPIC_API_KEY=tu_api_key_real_aqui
```

## 💻 Ejecución

Para iniciar la indexación automática de los documentos de prueba y realizar consultas, ejecuta:
```bash
python main.py
```

- Al correr por primera vez, el script creará la carpeta `datos_prueba/` con dos archivos de texto de prueba: `politica_vacaciones.txt` y `politica_gastos.txt`.
- Indexará estos archivos locales en la base de datos de la carpeta `./vector_db`.
- Realizará tres preguntas de prueba automáticamente en consola para demostrar el éxito de la recuperación y la detección de límites de información del modelo.
- Puedes modificar o agregar tus propios archivos `.txt` en la carpeta `datos_prueba/` para realizar experimentos personalizados.
