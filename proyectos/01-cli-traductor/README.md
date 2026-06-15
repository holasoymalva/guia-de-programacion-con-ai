# CLI de Traducción de Código 🔄

Este es una herramienta de línea de comandos sencilla construida en Python que utiliza la API de Anthropic (Claude) para traducir fragmentos de código de un lenguaje a otro de forma automática.

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

Para correr el script de traducción con el ejemplo predeterminado (Fibonacci de JavaScript a Python), simplemente ejecuta:
```bash
python main.py
```
