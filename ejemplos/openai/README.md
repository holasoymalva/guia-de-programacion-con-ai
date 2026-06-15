# Ejemplos con la API de OpenAI 🟢🤖

Ejemplos sencillos y auto-contenidos escritos en Python para interactuar con los modelos de OpenAI (como GPT-4o o GPT-4o-mini).

## 🚀 Instalación y Requisitos

1. Asegúrate de tener Python 3.10+ y un entorno virtual activo.
2. Instala la librería oficial de OpenAI:
   ```bash
   pip install openai python-dotenv
   ```
3. Configura tu API Key en tu archivo `.env` en la raíz de tu proyecto:
   ```ini
   OPENAI_API_KEY=tu_api_key_real_aqui
   ```

## 💻 Ejemplos Disponibles

- **`completion.py`**: Envío de un prompt simple y recepción de la respuesta completa del modelo (bloque único).
- **`streaming.py`**: Consumo de respuestas en tiempo real (streaming) para actualizar la consola a medida que se generan los tokens.
