# Ejemplos con LangChain 🦜🔗

Ejemplos sencillos para orquestar llamadas a modelos utilizando la librería **LangChain** y su interfaz unificada LCEL (LangChain Expression Language).

## 🚀 Instalación y Requisitos

1. Asegúrate de tener Python 3.10+ y un entorno virtual activo.
2. Instala LangChain y el adaptador de OpenAI o Anthropic:
   ```bash
   pip install langchain langchain-openai langchain-anthropic python-dotenv
   ```
3. Configura tus credenciales correspondientes en tu archivo `.env` en la raíz del proyecto.

## 💻 Ejemplos Disponibles

- **`basic_chain.py`**: Configuración de un prompt template, inicialización del modelo de OpenAI y encadenamiento del flujo de procesamiento básico usando LCEL.
