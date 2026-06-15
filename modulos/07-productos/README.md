# Módulo 7 - Construir Productos con AI 📦

Llevar una idea de inteligencia artificial a producción implica desafíos de arquitectura, seguridad y resiliencia. No basta con hacer una llamada a una API; necesitas diseñar sistemas que controlen costos, eviten caídas del servicio y protejan los datos de tus usuarios. En este módulo analizamos la arquitectura de producción y proporcionamos un checklist de seguridad y control.

---

## 🏗️ Arquitectura de Producción de una Aplicación AI

En un entorno real, tu cliente (móvil o web) nunca debe llamar directamente a la API de AI de forma directa. La arquitectura estándar implementa capas intermedias para proteger el sistema:

```text
[Cliente Web/Mobile] ➔ [API Gateway / BFF] ➔ [Cola de Mensajes / Cache] ➔ [AI Service] ➔ [BBDD Vectorial / SQL]
```

### Componentes Clave
1. **API Gateway / Backend**: Realiza la autenticación, controla la tasa de peticiones (rate limiting) por usuario y valida los datos de entrada.
2. **Cola de Mensajes**: Si tienes flujos de procesamiento largo (como transcripción de audio o análisis de grandes documentos), usa colas (Celery, RabbitMQ) para procesar de forma asíncrona.
3. **Capa de Base de Datos**: PostgreSQL para datos de usuario y tablas relacionales, combinada con extensiones de vectores (`pgvector`) para almacenar embeddings RAG de forma integrada.

---

## 🔒 Checklist de Seguridad y Resiliencia en Backend

Asegura tu aplicación en producción verificando los siguientes puntos:

- [ ] **Rate Limiting por IP/Usuario**: Evita ataques de denegación de servicio que inflen tu factura de API. Limita el uso a un máximo razonable por minuto (e.g., 10 peticiones de generación/minuto por usuario).
- [ ] **Filtros de Sanitización**: Limpia las entradas de usuario eliminando caracteres sospechosos o bloques de código si estás procesando texto plano.
- [ ] **Manejo de Errores con Fallback**: Si la API de Claude o GPT experimenta una caída (downtime), tu frontend no debe colapsar. Muestra un mensaje amigable o desvía la llamada automáticamente a un proveedor de respaldo.
- [ ] **Logging sin Datos Sensibles (PII)**: Registra los costos de los tokens y las latencias, pero asegúrate de filtrar contraseñas, correos electrónicos o datos de tarjetas de crédito en los registros de chat.
- [ ] **Alertas de Presupuesto en el Proveedor**: Configura un límite estricto de gasto diario y mensual en tu panel de OpenAI o Anthropic.

---

## 🚫 Errores Comunes y Cómo Resolverlos

### 1. Esperar indefinidamente respuestas síncronas de la API en el servidor principal
* **El Problema**: Las respuestas de un LLM pueden tardar de 5 a 30 segundos. Si bloqueas la conexión HTTP del backend de tu servidor mientras esperas el completado, agotarás los hilos del servidor y tu web app dejará de responder a otros usuarios.
* **La Solución**: Usa streaming de respuestas (Server-Sent Events) para actualizar la pantalla del usuario en tiempo real o procesa las peticiones complejas en segundo plano (workers asíncronos) enviando una notificación (Webhook o WebSockets) al finalizar.

### 2. No prever cambios o deprecación de modelos
* **El Problema**: Configuras tu backend con el modelo `"gpt-4-0613"`. Meses después, OpenAI descontinúa el modelo y tu sistema empieza a devolver errores `400 Bad Request` en producción.
* **La Solución**: Abstente de hardcodear los nombres de los modelos en tus archivos lógicos. Utiliza variables de entorno o un servicio de configuración centralizado (`MODEL_NAME=gpt-4o`) para poder actualizar la versión al instante sin redesplegar todo el código.

---

## ✍️ Ejercicios Prácticos

### Ejercicio 1: Implementar Rate Limiting con FastAPI
**Instrucciones**: Diseña un endpoint en FastAPI `/generar` que simule una llamada a la API y que use una estructura en memoria para limitar el acceso a un máximo de 3 peticiones por minuto para un mismo usuario.

#### 🟢 Solución del Ejercicio 1:
```python
import time
from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

# Diccionario en memoria para registrar marcas de tiempo por usuario (Simulación)
registro_solicitudes = {}

LIMIT_PETICIONES = 3
INTERVALO_SEGUNDOS = 60

@app.post("/generar")
async def generar_texto(x_user_id: str = Header(...)):
    ahora = time.time()
    
    # Inicializar registro del usuario si no existe
    if x_user_id not in registro_solicitudes:
        registro_solicitudes[x_user_id] = []
        
    # Filtrar peticiones que ya expiraron del intervalo de tiempo
    registro_solicitudes[x_user_id] = [
        t for t in registro_solicitudes[x_user_id] if ahora - t < INTERVALO_SEGUNDOS
    ]
    
    # Validar si supera el límite establecido
    if len(registro_solicitudes[x_user_id]) >= LIMIT_PETICIONES:
        tiempo_restante = int(INTERVALO_SEGUNDOS - (ahora - registro_solicitudes[x_user_id][0]))
        raise HTTPException(
            status_code=429,
            detail=f"Límite de peticiones superado. Inténtalo de nuevo en {tiempo_restante} segundos."
        )
        
    # Registrar la petición actual
    registro_solicitudes[x_user_id].append(ahora)
    
    return {"status": "ok", "mensaje": "Respuesta generada con éxito"}
```
