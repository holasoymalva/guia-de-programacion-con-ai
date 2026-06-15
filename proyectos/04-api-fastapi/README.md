# API REST con AI integrada (FastAPI) 🔌🧠

Esta es una API REST construida con **FastAPI** que expone endpoints para interactuar de forma inteligente con Claude (Anthropic). Permite analizar código de programación y generar scripts completos con pruebas unitarias de forma dinámica.

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

Para iniciar el servidor local de desarrollo con recarga automática, ejecuta:
```bash
python main.py
```
O bien:
```bash
uvicorn main:app --reload
```

El servidor estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 📖 Documentación Interactiva (Swagger UI)

Una vez iniciado el servidor, puedes ingresar a la interfaz interactiva para probar los endpoints directamente desde tu navegador en:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Endpoints Disponibles:

- **GET `/salud`**: Verifica la conectividad del servidor y si la clave de API está configurada.
- **POST `/analizar`**: Envía un fragmento de código y un lenguaje para recibir una auditoría completa del código.
- **POST `/generar`**: Envía una descripción funcional de un script y recibe el código fuente completo.
