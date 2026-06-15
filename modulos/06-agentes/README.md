# Módulo 6 - AI Agents y Automatización 🤖

Los agentes de inteligencia artificial representan el siguiente nivel de evolución de los LLMs. A diferencia de un chatbot clásico que responde de manera reactiva, un agente tiene la capacidad de planificar múltiples pasos, invocar herramientas externas y corregir sus propios errores para cumplir un objetivo complejo.

---

## 🧠 ¿Qué es un Agente de AI?

Un agente utiliza un LLM como "cerebro" central y lo dota de:
1. **Planificación**: Descomponer un objetivo grande en una secuencia lógica de subtareas.
2. **Uso de Herramientas (Tool Calling)**: Capacidad para ejecutar código Python, hacer búsquedas en internet, consultar bases de datos o llamar a APIs de terceros.
3. **Memoria**: Almacenar información de corto plazo (durante la ejecución de la tarea) y largo plazo (historial de ejecuciones previas).
4. **Reflexión**: Evaluar su propio resultado y, si es incorrecto, reintentar la tarea con un enfoque alternativo.

```text
Usuario ➔ [Cerebro LLM] ➔ Planificación ➔ Ejecución de Herramienta ➔ Análisis ➔ Resultado
```

---

## 📦 Frameworks Populares de Agentes

### 1. CrewAI (Enfoque Multi-Agente)
 CrewAI destaca por permitir diseñar sistemas basados en "roles". Puedes definir un "Investigador de Mercado", un "Escritor Técnico" y un "Auditor de Contenidos", cada uno con su propio perfil (backstory), herramientas y tareas asignadas. El framework gestiona la colaboración entre ellos para generar el entregable final.

### 2. LangChain / LangGraph (Control de Flujo)
LangGraph es la extensión de LangChain diseñada para modelar flujos de agentes como grafos dirigidos (cíclicos o acíclicos). Es ideal cuando necesitas un control muy estricto sobre las decisiones del agente y quieres evitar comportamientos impredecibles en producción.

---

## 🚫 Errores Comunes y Cómo Resolverlos

### 1. Loops infinitos del agente al intentar resolver una tarea rota
* **El Problema**: Tu agente intenta escribir en una base de datos sin permisos. La herramienta arroja un error, el agente lee el error e intenta la misma acción una y otra vez, gastando tokens indefinidamente.
* **La Solución**: Limita siempre el número máximo de iteraciones (`max_iterations` o `max_steps`) en el ejecutor del agente a un valor prudente (por ejemplo, 5 a 10 pasos).

### 2. Dar herramientas destructivas o sin control de límites
* **El Problema**: Creas una herramienta que ejecuta código del sistema y el agente por error borra directorios del servidor o altera bases de datos de producción.
* **La Solución**: Limita el entorno de ejecución de herramientas. Ejecuta los scripts generados por el agente dentro de contenedores aislados (como Docker o entornos sandbox) y nunca des accesos con permisos de administrador en producción.

---

## ✍️ Ejercicios Prácticos

### Ejercicio 1: Diseñar un Flujo Multi-Agente para Blogposts
**Instrucciones**: Diseña de manera conceptual (escribiendo los roles y tareas en español) un equipo de 2 agentes usando CrewAI para analizar un repositorio de código y escribir un artículo de blog sobre sus características.

#### 🟢 Solución del Ejercicio 1:

**Agente 1: Analista de Repositorios**
- **Rol**: Ingeniero de Software Analista de Código.
- **Objetivo**: Leer y extraer el propósito técnico del código alojado en un directorio local.
- **Herramientas**: `leer_archivo`, `listar_directorio`.
- **Backstory**: Experto en arquitectura de software capaz de descifrar código complejo rápidamente.

**Agente 2: Escritor Técnico**
- **Rol**: Redactor Creativo de Contenido Tecnológico.
- **Objetivo**: Redactar un post de blog amigable y estructurado basándose en el análisis técnico del Agente 1.
- **Herramientas**: Ninguna (solo redacción).
- **Backstory**: Experto en comunicación técnica que sabe captar la atención de desarrolladores principiantes.

**Flujo de Tareas**:
1. **Tarea 1 (Asignada al Analista)**: *"Analizar los archivos de código del proyecto y documentar en viñetas qué librerías se usan y qué hace cada archivo."*
2. **Tarea 2 (Asignada al Escritor)**: *"Tomar el reporte del Analista y escribir un artículo de blog de 400 palabras en español, incluyendo un ejemplo de uso del proyecto."*
