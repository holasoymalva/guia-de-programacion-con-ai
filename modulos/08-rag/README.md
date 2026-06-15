# Módulo 8 - RAG y Memoria en AI 🗄️

Los modelos de lenguaje tienen limitaciones de memoria y conocimientos desactualizados o privados. **RAG (Retrieval-Augmented Generation)** es el patrón de diseño estándar para solucionar esto, inyectando información relevante y verídica directamente en la ventana de contexto del LLM en tiempo real.

---

## 🏗️ El Pipeline RAG Completo

El proceso RAG consta de dos fases principales: **Ingesta de Datos** y **Consulta (Generación)**:

### 1. Ingesta de Datos (Preparación)
```text
Documento original ➔ Fragmentación (Chunking) ➔ Modelo de Embeddings ➔ Base de Datos Vectorial
```
- **Chunking (Fragmentación)**: Dividir un documento grande en bloques de texto más pequeños (por ejemplo, fragmentos de 500 palabras) para asegurar que el modelo reciba datos específicos y no sature su ventana de contexto.
- **Embeddings**: Convertir los fragmentos de texto en vectores matemáticos de alta dimensionalidad que representan su significado semántico.
- **BBDD Vectorial**: Almacenar los vectores para realizar búsquedas matemáticas ultrarápidas de similitud de coseno o distancia euclidiana.

### 2. Consulta y Generación (Tiempo de Ejecución)
```text
Pregunta del usuario ➔ Buscar fragmentos similares en BBDD Vectorial ➔ Construir Prompt con Contexto ➔ LLM responde
```
- Cuando el usuario pregunta algo, la pregunta se convierte a embedding y se buscan los 3 o 4 fragmentos de texto más similares en la base de datos vectorial.
- Estos fragmentos se inyectan en el prompt del LLM junto con la pregunta original.
- El LLM genera una respuesta "anclada" (grounded) a esa información real, eliminando casi por completo las alucinaciones.

---

## 🚫 Errores Comunes y Cómo Resolverlos

### 1. Usar un Chunk Size inadecuado
* **El Problema**:
  - Si el fragmento es muy pequeño (e.g., 10 palabras), se pierde el contexto del párrafo y la búsqueda semántica recupera información incomprensible.
  - Si el fragmento es muy grande (e.g., 5,000 palabras), inyectas demasiada información irrelevante en el prompt, encareciendo los costos y distrayendo al modelo.
* **La Solución**: Usa un tamaño estándar de 300 a 500 tokens con una superposición (overlap) del 10% al 20% (por ejemplo, 50 tokens de coincidencia entre fragmentos adyacentes) para asegurar que no se corten frases a la mitad.

### 2. No filtrar ni validar el contexto antes de enviarlo al modelo
* **El Problema**: La base de datos vectorial devuelve fragmentos que no tienen relación directa con la pregunta debido a una mala coincidencia matemática. El modelo intenta responder forzando una respuesta basada en información basura.
* **La Solución**: Configura un umbral mínimo de similitud (Threshold) y en el prompt instruye explícitamente: *"Si la respuesta no se encuentra en el contexto provisto, responde 'No tengo información suficiente en mis documentos' y no inventes datos"*.

---

## ✍️ Ejercicios Prácticos

### Ejercicio 1: Dividir Texto de forma Manual y Lógica (Chunking)
**Instrucciones**: Imagina que tienes el siguiente párrafo corto. Divídelo en fragmentos lógicos de máximo 20 palabras con un overlap de 5 palabras para no perder continuidad.

> *"La arquitectura RAG permite a los modelos de lenguaje acceder a información dinámica y privada de la empresa sin realizar entrenamientos costosos."*

#### 🟢 Solución del Ejercicio 1:

- **Fragmento 1** (14 palabras):
  > *"La arquitectura RAG permite a los modelos de lenguaje acceder a información dinámica y"*
- **Fragmento 2** (13 palabras - empieza con el overlap *"información dinámica y"*):
  > *"información dinámica y privada de la empresa sin realizar entrenamientos costosos."*
