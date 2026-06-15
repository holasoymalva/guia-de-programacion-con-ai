# Módulo 4 - Integración con APIs de AI 🔌

Consumir modelos de inteligencia artificial desde tu código requiere comprender el funcionamiento de sus interfaces de programación (APIs). En este módulo abordamos el consumo directo de APIs, el manejo de respuestas en tiempo real (streaming), control de errores, rate limits y una guía detallada de presupuestos y costos.

---

## 💰 Guía de Costos de APIs (Precios por Millón de Tokens)

Los precios de las APIs se facturan en base al uso de tokens de entrada (Input) y salida (Output). A continuación, se muestra una tabla de referencia del mercado (expresada en USD por 1 millón de tokens):

| Modelo / Proveedor | Costo Input (por 1M) | Costo Output (por 1M) | Comentarios |
| :--- | :--- | :--- | :--- |
| **DeepSeek R1 / V3** | $0.14 USD (Cache Hit) / $0.55 USD | $2.19 USD | La opción más barata del mercado para razonamiento avanzado. |
| **Gemini 2.5 Flash** | $0.075 USD | $0.30 USD | Extremadamente rápido y económico para procesamiento masivo. |
| **GPT-4o-mini** | $0.15 USD | $0.60 USD | El modelo liviano de referencia de OpenAI. |
| **Claude 3.7 Sonnet** | $3.00 USD | $15.00 USD | El estándar de la industria para desarrollo de software y lógica. |
| **GPT-4o** | $5.00 USD | $15.00 USD | Excelente razonamiento general y alta disponibilidad. |
| **Gemini 2.5 Pro** | $1.25 USD | $5.00 USD | Ideal para grandes volúmenes de contexto en archivos o repositorios. |

---

## 📈 Estrategias de Control de Presupuestos
1. **Modelos Híbridos (Fallback)**: Usa modelos económicos (`Gemini Flash` o `GPT-4o-mini`) para pre-procesar, validar formatos o clasificar texto. Reserva los modelos premium (`Claude Sonnet` o `GPT-4o`) únicamente para tareas críticas de generación de código o razonamiento complejo.
2. **Caché de Contexto**: Proveedores como Anthropic y DeepSeek ofrecen descuentos significativos (hasta el 90%) si se reutiliza el mismo contexto (como un system prompt largo o un conjunto de documentos RAG) en llamadas consecutivas.
3. **Límites de Uso en los Dashboards**: Configura alertas de presupuesto mensual y límites duros de facturación en las plataformas de desarrollo para evitar sorpresas financieras por loops infinitos en tus scripts.

---

## 🚫 Errores Comunes y Cómo Resolverlos

### 1. Loop infinito de llamadas por reintentos mal programados
* **El Problema**: Ocurre un error de red o de rate limit en la API, y tu script tiene un bloque `while True:` que reintenta la llamada inmediatamente. En pocos minutos agotas tu cuota de llamadas o saturas la cuenta de cobro.
* **La Solución**: Implementa **Exponential Backoff** (espera exponencial) con jitter (aleatoriedad). Por ejemplo, si falla, espera 1s, luego 2s, 4s, 8s, antes de desistir tras un número máximo de intentos.

### 2. Guardar claves de API en el código fuente de una aplicación cliente (Frontend)
* **El Problema**: Haces llamadas a la API de OpenAI directamente desde un componente React en tu web app de producción. Un usuario inspecciona el tráfico de red o el código compilado en el navegador y extrae tu clave privada.
* **La Solución**: Crea un servidor intermedio (Backend / BFF). El frontend hace una petición HTTP a tu API propia, y tu servidor ejecuta la llamada a la API del modelo protegiendo las llaves privadas.

---

## ✍️ Ejercicios Prácticos

### Ejercicio 1: Implementar un Manejador de Rate Limits
**Instrucciones**: Escribe un decorador o una función en Python que realice una llamada simulada a la API de Anthropic y, si se arroja un error de tasa de límite (`RateLimitError`), espere de forma incremental antes de reintentar.

#### 🟢 Solución del Ejercicio 1:
```python
import time
import random

class RateLimitError(Exception):
    """Excepción simulada de límite de velocidad de la API."""
    pass

def llamada_api_segura(max_intentos=4):
    intentos = 0
    espera_base = 2.0  # segundos
    
    while intentos < max_intentos:
        try:
            # Simulación de falla en el primer y segundo intento
            intentos += 1
            if intentos < 3:
                print(f"Llamando a la API... [Intento {intentos}]")
                raise RateLimitError("Rate limit exceeded. Please try again in 2s.")
            
            # Éxito en el tercer intento
            print("Llamada exitosa. Procesando respuesta...")
            return {"status": "success", "data": "Respuesta procesada correctamente"}
            
        except RateLimitError as e:
            if intentos >= max_intentos:
                print("Se alcanzó el límite máximo de reintentos. Abortando.")
                raise e
            
            # Cálculo de retroceso exponencial con variación aleatoria (jitter)
            tiempo_espera = (espera_base ** intentos) + random.uniform(0.1, 0.5)
            print(f"RateLimit detectado: {e} | Esperando {tiempo_espera:.2f} segundos...")
            time.sleep(tiempo_espera)

# Ejecución de prueba
llamada_api_segura()
```
