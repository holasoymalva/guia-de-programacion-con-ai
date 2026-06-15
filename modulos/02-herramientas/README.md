# Módulo 2 - Herramientas AI para Desarrolladores 🛠️

La productividad de un programador AI-First depende directamente del dominio de sus herramientas. En este módulo analizamos los asistentes de código más potentes, cómo configurarlos y proponemos un stack tecnológico recomendado según el tipo de aplicación que estés construyendo.

---

## 💻 Asistentes de Código en el IDE

### 1. Cursor: El Editor Pensado para AI
Cursor es un fork de VS Code diseñado desde el inicio para trabajar con modelos de lenguaje. Sus funciones estrella son:
- **Tab (Autocompletado)**: Sugiere múltiples líneas de código e incluso cambios estructurales antes de que los escribas.
- **Cmd + K (Edit/Generate)**: Permite editar o generar código directamente sobre la línea seleccionada en el archivo.
- **Composer (Cmd + I)**: Una interfaz multiarchivo. Puedes pedirle que cree un frontend en React y modifique el backend de FastAPI al mismo tiempo.
- **Contexto Avanzado (`@`)**: Puedes escribir `@Files` o `@Codebase` para que el modelo lea partes específicas de tu repositorio.

### 2. GitHub Copilot: El Estándar de la Industria
Desarrollado por GitHub y OpenAI, destaca por su integración nativa en múltiples entornos de desarrollo (VS Code, Visual Studio, Neovim, JetBrains). Su fuerte es el autocompletado en línea y su chat de contexto integrado.

### 3. Claude Code: La Terminal Inteligente
Lanzada por Anthropic, es una herramienta de CLI (Línea de Comandos) que actúa como un agente de desarrollo autónomo. Puede leer tu repositorio, crear y modificar archivos, correr tus tests, analizar errores y realizar commits en Git de forma autónoma.

---

## 📦 Stack AI Recomendado por Tipo de Proyecto

| Tipo de Proyecto | IDE / Asistente | Capa de Orquestación | Base de Datos Vectorial | APIs de AI / Modelos | Hosting / Deploy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Aplicación Web (Next.js)** | Cursor (Composer) + v0 | Vercel AI SDK | Supabase (pgvector) | Claude 3.7 Sonnet | Vercel |
| **Backend de Alta Performance** | VS Code + Copilot | LangChain (Python/TS) | Qdrant | DeepSeek R1 + Gemini | Railway / Docker |
| **Mobile App (Flutter/React Native)** | Cursor | Mastra / Agentes locales | Pinecone | GPT-4o-mini | Expo / EAS / Firebase |
| **Sistema RAG Corporativo** | VS Code + Aider | LlamaIndex (Python) | ChromaDB / pgvector | Claude 3.7 / Gemini | AWS / GCP |
| **Sistemas Multi-Agente** | Cursor + Claude Code | CrewAI / AutoGen | ChromaDB | Groq (Llama 3) / DeepSeek | Fly.io / VPS |

---

## 🚫 Errores Comunes y Cómo Resolverlos

### 1. Ignorar el archivo `.gitignore` y subir las credenciales de la API a GitHub
* **El Problema**: Configuras una herramienta local de AI, creas un archivo `.env` para tu API Key y por error haces commit y push. Tu clave es filtrada y en pocas horas bots consumen tu saldo de API.
* **La Solución**: Antes de realizar cualquier commit, asegúrate de que el archivo `.env` esté listado en tu `.gitignore`. Usa variables de entorno globales en tus despliegues.

### 2. Confusión de contexto usando `@codebase` en Cursor en repositorios gigantescos
* **El Problema**: Escribes una pregunta simple en el chat de Cursor usando `@codebase` en un proyecto de millones de líneas. El sistema se vuelve extremadamente lento y la respuesta pierde precisión.
* **La Solución**: Sé selectivo. Usa `@File <nombre>` o `@Folder <nombre>` para limitar el contexto solo a los componentes involucrados en la tarea actual.

---

## ✍️ Ejercicios Prácticos

### Ejercicio 1: Configurar un Entorno AI Seguro
**Instrucciones**: Crea un archivo de configuración básica para garantizar que tu IDE y tus scripts no expongan tus credenciales.
1. Escribe la estructura típica de un archivo `.gitignore` para un proyecto de desarrollo AI en Python.
2. Crea un archivo de plantilla `.env.example` para que tus colaboradores sepan qué variables configurar sin revelar tu clave privada.

#### 🟢 Solución del Ejercicio 1:

1. **Contenido de `.gitignore`**:
   ```text
   # Python virtual environments
   venv/
   .venv/
   env/
   
   # IDE configuration
   .vscode/
   .idea/
   .cursor/
   
   # Environment variables and secrets
   .env
   .env.local
   
   # Databases
   *.db
   vector_db/
   chroma_db/
   ```

2. **Contenido de `.env.example`**:
   ```ini
   # Copia este archivo como .env y rellena con tus API Keys reales
   OPENAI_API_KEY=tu_api_key_de_openai
   ANTHROPIC_API_KEY=tu_api_key_de_anthropic
   GEMINI_API_KEY=tu_api_key_de_gemini
   DEEPSEEK_API_KEY=tu_api_key_de_deepseek
   
   # Configuraciones del Servidor
   PORT=8000
   DEBUG=True
   ```
