# Módulo 0 - Mentalidad AI-First 🧠

El cambio más difícil al programar con inteligencia artificial no es aprender la sintaxis de una API o memorizar comandos; es **cambiar tu forma de pensar**. Este módulo profundiza en el cambio de paradigma de desarrollo de software y en cómo adoptar una mentalidad que te convierta en un arquitecto de soluciones en lugar de un mecanógrafo de código.

---

## 🔄 El Cambio de Paradigma: Del Flujo Tradicional al AI-First

En el desarrollo tradicional de software, el cuello de botella suele ser la velocidad de escritura, la memorización de sintaxis y la búsqueda manual en documentación o foros. Con la llegada de los LLMs, el flujo cambia drásticamente:

```text
Tradicional:  Problema ➔ Buscar en Google/Docs ➔ Escribir código ➔ Probar ➔ Repetir
AI-First:     Problema ➔ Diseñar/Describir Contexto ➔ Iterar con AI ➔ Validar ➔ Producción
```

### Los 5 Principios del Desarrollo AI-First
1. **Sé el Arquitecto, no el Mecanógrafo**: La AI es excelente generando código estructurado y repetitivo. Tu valor como desarrollador radica en definir la arquitectura, el diseño de la base de datos, el flujo de datos y la experiencia de usuario.
2. **El Contexto es el Superpoder**: La calidad del código que genera la AI es directamente proporcional al contexto que le proporcionas. Si no le describes bien la estructura de tu base de datos o el stack que usas, generará código genérico e inservible.
3. **Validar y Desconfiar por Defecto**: Los modelos de lenguaje son probabilisticos y alucinan. Tu rol cambia de ser "creador de bugs" a "auditor y depurador" del código generado.
4. **Iteración Rápida y Prototipado**: No busques la solución perfecta en el primer prompt. Genera una base, pruébala e itera agregando requerimientos de forma incremental.
5. **Aprender de la AI**: Usa los asistentes de código para que te expliquen cómo funcionan bloques de código complejos o patrones de diseño que no conoces.

---

## 🚫 Errores Comunes y Cómo Resolverlos

### 1. Copiar y pegar código ciegamente sin entenderlo
* **El Problema**: La AI genera una solución y la pegas directamente en tu archivo principal. El sistema se rompe o introduce vulnerabilidades silenciosas.
* **La Solución**: Lee cada línea generada por el asistente. Si hay una función o parámetro que no conoces, pídele: *"Explícame qué hace exactamente la línea X y cuáles son sus efectos secundarios"*.

### 2. Tratar de resolver todo el proyecto con un solo prompt masivo
* **El Problema**: Escribes un prompt gigante como *"Crea un clon de Instagram con backend de node y base de datos postgres"* y la AI te entrega código incompleto, con placeholders y de baja calidad.
* **La Solución**: Descompón el problema en micro-tareas. Primero pide la estructura de la base de datos, luego los modelos de ORM, luego un endpoint específico, y así sucesivamente.

### 3. Culpar a la AI cuando el código falla
* **El Problema**: La AI genera código con errores de sintaxis o que no compila, y el programador desiste argumentando que *"la AI no sirve"*.
* **La Solución**: Los errores de la AI suelen deberse a falta de contexto. Copia el error exacto que te arroja la consola, pégalo en el chat de la AI y pídele: *"Este es el error de consola. Analiza por qué ocurrió considerando el contexto actual y corrígelo"*.

---

## ✍️ Ejercicios Prácticos

### Ejercicio 1: De Programador Tradicional a Diseñador de Contexto
**Instrucciones**: Imagina que tienes que construir un sistema de autenticación de dos factores (2FA) vía correo electrónico en Python. Escribe cómo buscarías esto en Google (enfoque tradicional) versus cómo redactarías el prompt/contexto de partida para tu asistente de código (enfoque AI-First).

#### 🟢 Solución del Ejercicio 1:
- **Enfoque Tradicional**:
  Búsqueda en Google: *"python send email 2fa pyotp example library"* o *"fastapi 2fa email verification flow"*. Luego tendrás que leer 3 blogs diferentes y unir el código manualmente.
- **Enfoque AI-First**:
  Prompt para el Asistente:
  > *"Actúa como un desarrollador experto en seguridad web y Python. Necesito implementar un flujo de autenticación de dos factores (2FA) usando códigos OTP enviados por correo.
  > Mi stack: FastAPI, SQLAlchemy (PostgreSQL) y `emails-smtp` para el envío.
  > Tarea: Diseña el modelo de base de datos para almacenar el secreto OTP temporal, y escribe el endpoint de FastAPI `/auth/verify-2fa` que reciba el código del usuario y lo valide usando la librería `pyotp`. Asegúrate de que el código expire en 5 minutos."*
