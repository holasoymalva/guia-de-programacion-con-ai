# Módulo 5 - Proyectos Prácticos y Vibe Coding 🚀

En este módulo llevamos la teoría a la práctica. Explicamos cómo construir y ejecutar 5 proyectos reales con integraciones de AI y exploramos el flujo de trabajo moderno conocido como **Vibe Coding** utilizando herramientas no-code/low-code como Lovable y v0.

---

## 🏗️ Los 5 Proyectos del Repositorio

El repositorio cuenta con 5 proyectos listos para ser ejecutados localmente en la carpeta `proyectos/`:

1. **01-cli-traductor**: Herramienta de línea de comandos en Python que toma archivos de código fuente y traduce su sintaxis a otro lenguaje conservando la lógica y agregando comentarios detallados de las diferencias.
2. **02-generador-readme**: Script autónomo que lee los archivos de código de un directorio local y genera automáticamente un archivo `README.md` estructurado y profesional usando Claude.
3. **03-chatbot-memoria**: Chatbot conversacional de consola que almacena localmente el historial de conversaciones en formato JSON para simular memoria persistente de largo plazo.
4. **04-api-fastapi**: API REST de alto rendimiento construida con FastAPI que integra endpoints para analizar la calidad del código, buscar vulnerabilidades y generar código unitario.
5. **05-sistema-rag**: Pipeline completo de Retrieval-Augmented Generation que toma archivos de texto del disco, los divide en chunks, genera embeddings vectoriales y almacena los vectores en ChromaDB para realizar búsquedas semánticas basadas en preguntas.

---

## ⚡ Vibe Coding: Desarrollo Dirigido por Lenguaje Natural

El **Vibe Coding** es un paradigma de desarrollo donde el programador actúa como director creativo y supervisor, mientras que las herramientas de IA generativa escriben, compilan y despliegan todo el código de la aplicación web a partir de prompts.

### Flujo de Trabajo con Lovable y v0 (Vercel)

```text
Idea ➔ Prompt Inicial (v0) ➔ Componente Visual ➔ Conectar a Supabase (Lovable) ➔ Despliegue en 1 Click
```

1. **Generación de UI con v0**:
   - Ingresas a `v0.dev` y describes la interfaz: *"Crea una tabla interactiva para gestionar las tareas de un equipo, con filtros por prioridad y modo oscuro premium"*.
   - v0 te devuelve código React con Tailwind CSS listo para copiar o descargar.
2. **Desarrollo Full-Stack con Lovable**:
   - Permite crear aplicaciones web funcionales escribiendo instrucciones simples.
   - Lovable se conecta automáticamente con **Supabase** para configurar la base de datos (tablas, relaciones, autenticación).
   - Genera los flujos de frontend interactivos y realiza el despliegue automático en la nube.
3. **Rol del Desarrollador en Vibe Coding**:
   - **Control de Cambios**: Supervisar que las solicitudes no rompan la base de datos.
   - **Estructuración de Datos**: Diseñar adecuadamente las relaciones entre tablas para que la IA entienda el modelo del negocio.

---

## 🚫 Errores Comunes y Cómo Resolverlos

### 1. Inconsistencia en el entorno virtual al ejecutar múltiples proyectos
* **El Problema**: Instalar las dependencias de todos los proyectos de forma global en tu computadora. Esto genera conflictos de versiones (e.g., diferentes versiones de la librería de `anthropic` o `openai`).
* **La Solución**: Usa entornos virtuales independientes (`venv`) para cada proyecto y ejecuta `pip install -r requirements.txt` dentro de cada carpeta.

### 2. Guardar archivos de bases de datos vectoriales locales en Git
* **El Problema**: Ejecutas el sistema RAG y se crea una base de datos local en la carpeta `vector_db/`. Haces commit y subes miles de archivos binarios e índices de ChromaDB a tu repositorio de GitHub.
* **La Solución**: Agrega la carpeta de base de datos local (`vector_db/` o `chroma.sqlite3`) en tu archivo `.gitignore`.

---

## ✍️ Ejercicios Prácticos

### Ejercicio 1: Desplegar un Entorno Virtual Independiente
**Instrucciones**: Inicializa un entorno de desarrollo para probar el proyecto `01-cli-traductor`. Escribe la secuencia de comandos de terminal requerida en macOS/Linux.

#### 🟢 Solución del Ejercicio 1:
```bash
# 1. Navegar a la carpeta del proyecto
cd proyectos/01-cli-traductor/

# 2. Crear el entorno virtual llamado 'venv'
python3 -m venv venv

# 3. Activar el entorno virtual
source venv/bin/activate

# 4. Instalar las dependencias requeridas
pip install --upgrade pip
pip install -r requirements.txt

# 5. Ejecutar la aplicación
python main.py
```
