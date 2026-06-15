# Generador de README Automático 📄🤖

Este script autónomo en Python analiza los archivos de código fuente de un directorio y utiliza la API de Anthropic (Claude) para redactar un archivo `README.md` profesional, completo y estructurado en español, ideal para tus repositorios de GitHub.

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

Para correr el script de generación del README, ejecuta:
```bash
python main.py
```

El script analizará los archivos locales de este mismo proyecto (`main.py`, `requirements.txt`, etc.) y creará un archivo llamado `README_GENERADO.md` en este mismo directorio. Puedes editar el script para apuntarlo a cualquier otra carpeta local.
