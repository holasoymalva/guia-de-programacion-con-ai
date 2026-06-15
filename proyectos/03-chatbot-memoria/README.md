# Chatbot con Memoria Persistente 🤖💾

Este es un chatbot conversacional de consola escrito en Python. Lo especial de este proyecto es que almacena localmente el historial de conversaciones en un archivo JSON (`memoria_chat.json`). Al cerrar el programa y volverlo a abrir, el chatbot recordará la conversación de la sesión anterior.

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

Para iniciar el chat en consola, ejecuta:
```bash
python main.py
```

- Puedes chatear con él de forma natural.
- Escribe `salir`, `exit` o `quit` para guardar la conversación y cerrar de forma ordenada.
- La memoria de la conversación se almacena localmente en el archivo `memoria_chat.json`.
