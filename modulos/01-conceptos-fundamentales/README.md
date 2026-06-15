# Módulo 1 - Conceptos Fundamentales 📚

Para programar de forma eficiente con inteligencia artificial, es crucial entender las bases teóricas y tecnológicas de los Large Language Models (LLMs). En este módulo abordamos el funcionamiento de los modelos, la anatomía de los tokens, los diferentes tipos de IA y casos de uso por industria.

---

## 📊 Comparativa de Modelos de AI (Actualizada 2026)

El ecosistema de LLMs es altamente dinámico. A continuación, se muestra una comparativa detallada de los modelos de frontera más relevantes para tareas de desarrollo de software:

| Modelo | Desarrollador | Ventana de Contexto | Fortaleza Principal | Costo Relativo | Licencia / Acceso |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Claude 3.7 Sonnet** | Anthropic | 200K tokens | Programación compleja, refactorización y lógica matemática. | Medio-Alto | Comercial (Pro/API) |
| **GPT-4o** | OpenAI | 128K tokens | Razonamiento lógico general, velocidad y capacidades multimedia. | Medio | Comercial (Pro/API) |
| **Gemini 2.5 Pro** | Google | 2M tokens | Ventana de contexto gigante (ideal para repositorios completos). | Medio-Bajo | Comercial (API) |
| **DeepSeek V3 / R1** | DeepSeek | 128K tokens | Costo-beneficio extremadamente alto, razonamiento técnico avanzado. | Muy Bajo | Comercial / Abierto |
| **Llama 3.3 (70B)** | Meta | 128K tokens | Altamente personalizable, ideal para despliegues locales (self-hosted). | Gratis (Self-host) | Open Source (Permisiva) |
| **Qwen 2.5 Coder** | Alibaba | 128K tokens | Especializado en generación de código y automatización técnica. | Bajo | Open Source |

---

## 🪙 Tokens: La Moneda de la AI

Los modelos de lenguaje no leen palabras como los humanos; leen **tokens**. Un token es la unidad básica de información para un LLM. Puede ser una palabra completa, una sílaba o incluso un solo carácter.

> [!TIP]
> Como regla general para el idioma inglés, **1 token ≈ 4 caracteres** o **0.75 palabras**. En español, debido a la tokenización optimizada para inglés, las palabras suelen dividirse en más tokens, lo que aumenta los costos y reduce ligeramente el contexto efectivo.

### El Impacto Técnico de los Tokens
1. **Límite de Contexto**: Cada modelo tiene un límite máximo de tokens que puede procesar en una sola llamada (Input + Output). Si envías un archivo de código muy grande que supera este límite, el modelo olvidará el inicio o dará un error.
2. **Costos**: Las APIs cobran por el volumen de tokens procesados. Los tokens de salida (Output) suelen ser de 3 a 5 veces más costosos que los de entrada (Input).
3. **Latencia**: A mayor cantidad de tokens generados, mayor tiempo tardará la respuesta en completarse.

---

## 🚀 Casos de Uso por Industria

### 💳 FinTech (Tecnología Financiera)
- **Análisis de Riesgos**: Detección semántica de anomalías en transacciones financieras.
- **Automatización de Compliance**: Lectura y mapeo automático de regulaciones legales locales con el código del backend.
- **Asistentes de Inversión**: Procesamiento de reportes PDF corporativos estructurando datos clave en JSON.

### 🎓 EdTech (Educación)
- **Tutores Personalizados**: Explicación de conceptos de programación adaptados al nivel del estudiante.
- **Evaluación Automatizada**: Corrección de ejercicios de programación con retroalimentación en tiempo real y sugerencias de mejora.

### 🛒 E-commerce (Comercio Electrónico)
- **Generación de Contenido**: Creación masiva de descripciones de productos optimizadas para SEO.
- **Soporte Inteligente**: Chatbots de atención al cliente conectados a las bases de datos de inventario y envíos (RAG).

### 🏥 Salud y MedTech
- **Estructuración de Historiales**: Extracción de datos clave desde notas médicas desestructuradas hacia bases de datos estructuradas.
- **Soporte de Diagnóstico**: Análisis rápidos de literatura científica para médicos de atención primaria.

---

## 🚫 Errores Comunes y Cómo Resolverlos

### 1. Asumir que la ventana de contexto de 1 millón de tokens significa que puedes enviarle todo sin filtrar
* **El Problema**: Le envías a Gemini 1.5 millones de caracteres de logs de tu servidor para buscar un bug. La AI te responde algo genérico o ignora la causa real.
* **La Solución**: Aunque la ventana de contexto sea masiva, la atención del modelo se dispersa (*Lost in the Middle*). Filtra la información y dale solo las partes sospechosas y relevantes del código o logs.

### 2. Confundir el conocimiento del modelo con datos dinámicos en tiempo real
* **El Problema**: Le preguntas a un modelo base *"¿Cuál es la cotización del dólar hoy?"* o *"¿Cuáles son los últimos cambios en la API de Stripe lanzados ayer?"* y el modelo inventa una respuesta desactualizada.
* **La Solución**: Los modelos tienen una fecha de corte de conocimiento. Para datos en tiempo real, usa modelos con búsqueda web integrada o implementa tu propia infraestructura RAG (Retrieval-Augmented Generation).

---

## ✍️ Ejercicios Prácticos

### Ejercicio 1: Estimación de Costos por Tokens
**Instrucciones**: Tienes un script que analiza contratos legales. Cada contrato tiene aproximadamente 8,000 palabras en español. Usas el modelo **GPT-4o** con un costo de $5 USD por millón de tokens de entrada.
1. Calcula la cantidad estimada de tokens del contrato (asume 1 palabra en español = 1.4 tokens).
2. Calcula el costo estimado en dólares por procesar un solo contrato.

#### 🟢 Solución del Ejercicio 1:
1. **Tokens estimados**:
   $$8,000 \text{ palabras} \times 1.4 \text{ tokens/palabra} = 11,200 \text{ tokens}$$
2. **Costo por contrato**:
   $$\text{Costo} = \frac{11,200 \text{ tokens}}{1,000,000 \text{ tokens}} \times 5 \text{ USD} = 0.056 \text{ USD} \text{ (aproximadamente } 5.6 \text{ centavos de dólar por contrato)}$$
