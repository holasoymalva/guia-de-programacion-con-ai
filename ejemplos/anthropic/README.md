# Ejemplos con la API de Anthropic 🟠🤖

Ejemplos prácticos y auto-contenidos escritos en Python para interactuar con los modelos Claude de Anthropic (como Claude 3.5 o 3.7 Sonnet).

## 🚀 Instalación y Requisitos

1. Asegúrate de tener Python 3.10+ y un entorno virtual activo.
2. Instala la librería oficial de Anthropic:
   ```bash
   pip install anthropic python-dotenv
   ```
3. Configura tu API Key en tu archivo `.env` en la raíz de tu proyecto:
   ```ini
   ANTHROPIC_API_KEY=tu_api_key_real_aqui
   ```

## 💻 Ejemplos Disponibles

- **`completion.py`**: Petición de texto simple para recibir una respuesta en un bloque único de texto.
- **`streaming.py`**: Consumo de respuestas en tiempo real (streaming) para actualizar la consola token a token.
- **`tools.py`**: Configuración y simulación de **Tool Use** (Function Calling), enseñando a Claude a decidir cuándo y cómo llamar a funciones de Python locales.
