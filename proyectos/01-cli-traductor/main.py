#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv
import anthropic

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Verificar que la API Key esté presente
API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    print("Error: No se encontró la variable ANTHROPIC_API_KEY en las variables de entorno o en el archivo .env.")
    print("Por favor, crea un archivo .env en esta carpeta y agrega tu clave:")
    print("ANTHROPIC_API_KEY=tu_api_key_aquí")
    sys.exit(1)

client = anthropic.Anthropic(api_key=API_KEY)

def traducir_codigo(codigo: str, origen: str, destino: str) -> str:
    print(f"Enviando solicitud a Claude para traducir de {origen} a {destino}...")
    try:
        mensaje = client.messages.create(
            model="claude-3-7-sonnet-20250219",  # Usando el modelo de frontera de Anthropic
            max_tokens=2048,
            messages=[{
                "role": "user",
                "content": f"""Traduce el siguiente código de {origen} a {destino}.
Mantén la misma funcionalidad exacta.
Adapta las convenciones del lenguaje destino (por ejemplo, snake_case en Python, camelCase en JavaScript).
Incluye comentarios explicando diferencias importantes de sintaxis o de comportamiento.

Código en {origen}:
```{origen.lower()}
{codigo}
```
Devuelve solo el código {destino} traducido."""
            }]
        )
        return mensaje.content[0].text
    except Exception as e:
        return f"Error al llamar a la API de Anthropic: {e}"

def main():
    # Código de ejemplo predeterminado (Fibonacci en JavaScript)
    codigo_js = """
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}
"""
    print("=== Código Original (JavaScript) ===")
    print(codigo_js.strip())
    print("\n" + "="*40 + "\n")
    
    codigo_python = traducir_codigo(codigo_js, "JavaScript", "Python")
    
    print("\n=== Código Traducido a Python ===")
    print(codigo_python)

if __name__ == "__main__":
    main()
