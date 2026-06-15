# Módulo 3 - Prompt Engineering para Desarrolladores ✍️

El Prompt Engineering es el arte y la ciencia de diseñar instrucciones precisas para guiar el comportamiento de un LLM. Para un desarrollador, dominar el prompting significa reducir drásticamente el tiempo de depuración, evitar la generación de código redundante y forzar al modelo a entregar estructuras de datos exactas.

---

## 🎯 Anatomía de un Prompt Profesional para Desarrollo

Un prompt robusto no es una simple frase; es una estructura organizada que contiene múltiples componentes:

```text
1. ROL (Actúa como...)
2. CONTEXTO (Estoy construyendo una app con...)
3. TAREA / INSTRUCCIÓN (Genera un endpoint que...)
4. RESTRICCIONES (No uses librerías externas, usa TypeScript estricto...)
5. FORMATO DE SALIDA (Devuelve el código limpio y una explicación en JSON...)
```

---

## 📋 Prompts Listos para Copiar (Templates)

### 1. Para Refactorización y Limpieza de Código
> *"Actúa como un desarrollador Senior con foco en código limpio y buenas prácticas de diseño de software. Analiza el siguiente bloque de código.
> Tarea: Refactoriza el código para mejorar su legibilidad y eficiencia. Aplica principios SOLID y patrones de diseño si son necesarios.
> Restricciones: No cambies la funcionalidad lógica existente. No agregues librerías adicionales.
> Código original:
> [PEGA TU CÓDIGO AQUÍ]"*

### 2. Para Escribir Tests Unitarios Completos
> *"Actúa como un Ingeniero de QA y Testing de software experto.
> Contexto: Necesito asegurar la cobertura de pruebas unitarias para esta función.
> Tarea: Genera una suite de pruebas unitarias utilizando el framework de testing [e.g., PyTest / Jest].
> Asegúrate de probar:
> 1. Casos de éxito estándar (Happy path)
> 2. Valores límite (Edge cases)
> 3. Entradas inválidas o nulas (Error handling)
> Función a probar:
> [PEGA TU FUNCIÓN AQUÍ]"*

### 3. Para Debugging Eficiente
> *"Actúa como un especialista en debugging y optimización. Estoy experimentando el siguiente comportamiento inesperado en mi código.
> Error o comportamiento: [DESCRIBE EL BUG O PEGA EL LOG DE ERROR]
> Entorno: [e.g., Python 3.11, Django 4.2]
> Código involucrado:
> [PEGA TU CÓDIGO AQUÍ]
> Tarea: Explica paso a paso por qué está ocurriendo este error y proporciona la solución corregida."*

---

## 🚫 Errores Comunes y Cómo Resolverlos

### 1. Ser vago y ambiguo en las instrucciones
* **El Problema**: Escribir *"Crea un script para conectar con Stripe"*. La AI generará código usando una versión obsoleta de la librería de Stripe o un flujo que no se adapta a tu backend.
* **La Solución**: Especifica el stack exacto y la acción a realizar: *"Crea un script en Node.js usando la librería oficial de Stripe `@stripe/stripe-js` versión 14 para inicializar un flujo de Checkout con un precio ID fijo."*

### 2. Olvidar restringir el formato de salida en integraciones de API
* **El Problema**: Tu backend en Python consume la API de OpenAI y esperas recibir una lista JSON, pero el modelo te devuelve un texto explicativo como *"¡Por supuesto! Aquí tienes la lista: ... "* lo que rompe tu parser de JSON.
* **La Solución**: Usa JSON Mode en la API o instruye con firmeza: *"Devuelve exclusivamente una estructura JSON válida que cumpla con el siguiente esquema: {"usuarios": [{"id": int, "nombre": string}]}. No agregues introducciones ni explicaciones. Responde únicamente con el bloque JSON."*

---

## ✍️ Ejercicios Prácticos

### Ejercicio 1: Diseñar un Prompt de Few-Shot
**Instrucciones**: Diseña un prompt de Few-Shot para clasificar logs de un servidor en tres niveles: `INFO`, `WARNING` y `ERROR`. El modelo debe aprender del patrón basándose en ejemplos provistos y luego clasificar un log nuevo.

#### 🟢 Solución del Ejercicio 1:
```text
Actúa como un clasificador automático de logs del sistema. Clasifica el mensaje de entrada en una de las siguientes categorías: INFO, WARNING o ERROR.

Ejemplos:
Entrada: "Database connection established in 12ms" -> Salida: INFO
Entrada: "Disk space utilization is at 88%" -> Salida: WARNING
Entrada: "Failed to write user profile image to S3: Access Denied" -> Salida: ERROR
Entrada: "User session expired for id 5439" -> Salida: INFO
Entrada: "API gateway latency spikes above 2000ms" -> Salida: WARNING

Clasifica la siguiente entrada:
Entrada: "Payment processor returned status code 500 Internals" -> Salida:
```
*(El modelo completará automáticamente con `ERROR` basándose en el patrón).*
