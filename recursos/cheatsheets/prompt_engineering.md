# Cheatsheet de Prompt Engineering 📝⚡

Guía rápida de referencia con técnicas, parámetros y buenas prácticas para obtener los mejores resultados de los LLMs.

---

## 🛠️ Técnicas Clave de Prompting

| Técnica | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| **Zero-Shot** | Pedir al modelo que realice una tarea sin darle ejemplos previos. | *"Escribe una función en Python para revertir un string."* |
| **Few-Shot** | Dar ejemplos de entrada y salida para guiar la respuesta del modelo. | * Ver ejemplo abajo |
| **Chain-of-Thought (CoT)** | Forzar al modelo a razonar y explicar el proceso paso a paso antes de responder. | *"Analiza el bug paso a paso, escribe tu hipótesis y luego el código corregido."* |
| **System Prompts** | Instrucciones globales que van al inicio y definen el rol del asistente. | *"Eres un traductor. Solo respondes con texto traducido, sin introducciones."* |

### Ejemplo de Few-Shot
```text
Convierte textos a mayúsculas y remueve acentos:
canción -> CANCION
árbol -> ARBOL
teléfono -> TELEFONO
computación ->
```

---

## ⚙️ Parámetros Clave de la API

- **Temperature (0.0 a 2.0)**:
  - **`0.0`**: Respuestas deterministas y predecibles. Ideal para **código**, matemáticas y análisis estructurados.
  - **`0.7`**: Balance entre precisión y creatividad. Ideal para **chatbots** conversacionales.
  - **`1.0+`**: Respuestas altamente creativas y variadas. Ideal para **brainstorming**.
- **Max Tokens**: Límite estricto de tokens que el modelo puede generar en la respuesta.
- **Top P (Nucleus Sampling)**: Controla la diversidad seleccionando tokens que sumen un porcentaje de probabilidad acumulada (e.g., `0.9` analiza solo el 90% superior de opciones lógicas).

---

## 🧠 Estructura de Prompt "Perfecta"
```text
[ROL]        Actúa como un experto en base de datos.
[CONTEXTO]   Tengo una tabla 'usuarios' con 10,000 registros.
[TAREA]      Escribe una consulta SQL para obtener los 10 usuarios que más gastan.
[RESTRIC.]   No uses subconsultas complejas, optimiza para tiempos de ejecución cortos.
[FORMATO]    Devuelve solo el código SQL plano.
```
