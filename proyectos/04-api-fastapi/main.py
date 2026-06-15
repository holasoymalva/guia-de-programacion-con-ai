#!/usr/bin/env python3
import os
import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import anthropic

# Cargar variables de entorno
load_dotenv()

# Verificar la API Key
API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    print("Error: No se encontró la variable ANTHROPIC_API_KEY en las variables de entorno o en el archivo .env.")
    # No detenemos el inicio del servidor, pero lo advertimos.
    # Los endpoints fallarán si no se configura la clave.

app = FastAPI(
    title="AI Code Analysis API 💻🤖",
    description="API REST de alto rendimiento que expone endpoints para analizar código y generar scripts.",
    version="1.0.0"
)

# Esquemas de entrada usando Pydantic v2
class SolicitudAnalisis(BaseModel):
    codigo: str = Field(..., description="El código fuente a ser analizado por el modelo")
    lenguaje: str = Field("python", description="El lenguaje de programación del código provisto")

class SolicitudGeneracion(BaseModel):
    descripcion: str = Field(..., description="La descripción detallada del algoritmo a generar")
    lenguaje: str = Field("python", description="El lenguaje de programación objetivo")
    incluir_tests: bool = Field(False, description="Especifica si se deben incluir pruebas unitarias en el resultado")

# Endpoint de Salud
@app.get("/salud", tags=["Sistema"])
async def verificar_salud():
    estado_key = "Configurada" if os.getenv("ANTHROPIC_API_KEY") else "No Configurada (Endpoints deshabilitados)"
    return {
        "estado": "ok",
        "version": "1.0.0",
        "credenciales_ai": estado_key
    }

# Endpoint para Analizar Código
@app.post("/analizar", tags=["AI Code Utilities"])
async def analizar_codigo(solicitud: SolicitudAnalisis):
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise HTTPException(status_code=500, detail="API Key de Anthropic no configurada en el servidor.")
        
    client = anthropic.Anthropic(api_key=key)
    
    prompt = f"""Analiza con atención el siguiente código escrito en {solicitud.lenguaje} y proporciona un reporte detallado en español.
El reporte debe incluir de forma obligatoria las siguientes secciones en Markdown:
1. Puntuación de calidad del 1 al 10 (con justificación).
2. Lista de bugs detectados, errores lógicos o de concurrencia.
3. Recomendaciones específicas para mejorar la performance o reducir memoria.
4. Mejoras de legibilidad (aplicando principios de código limpio).

Código a analizar:
```{solicitud.lenguaje.lower()}
{solicitud.codigo}
```"""

    try:
        respuesta = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        return {"analisis": respuesta.content[0].text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al llamar a la API del modelo: {e}")

# Endpoint para Generar Código
@app.post("/generar", tags=["AI Code Utilities"])
async def generar_codigo(solicitud: SolicitudGeneracion):
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise HTTPException(status_code=500, detail="API Key de Anthropic no configurada en el servidor.")
        
    client = anthropic.Anthropic(api_key=key)
    
    prompt = f"Genera código en {solicitud.lenguaje} para cumplir con la siguiente especificación: {solicitud.descripcion}.\n"
    if solicitud.incluir_tests:
        prompt += "Incluye adicionalmente una suite de pruebas unitarias completas usando un framework estándar del lenguaje."
        
    prompt += "\nDevuelve solo el código de respuesta limpio y comentarios explicativos directamente dentro del código."

    try:
        respuesta = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=3072,
            messages=[{"role": "user", "content": prompt}]
        )
        return {"codigo_generado": respuesta.content[0].text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al llamar a la API del modelo: {e}")

# Ejecución directa para pruebas de desarrollo
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
