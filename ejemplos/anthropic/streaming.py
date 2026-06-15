#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv
import anthropic

# Cargar variables de entorno
load_dotenv()

def main():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: No se encontró la variable de entorno ANTHROPIC_API_KEY.")
        return

    client = anthropic.Anthropic(api_key=api_key)

    print("Iniciando llamada con streaming a Claude (Model: claude-3-7-sonnet-20250219)...")
    print("Respuesta: ", end="", flush=True)

    try:
        # Usar la función stream para el manejo en tiempo real
        with client.messages.stream(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1024,
            messages=[{"role": "user", "content": "Dime qué novedades técnicas importantes trae Python 3.13."}]
        ) as stream:
            for text in stream.text_stream:
                sys.stdout.write(text)
                sys.stdout.flush()
        print() # Salto de línea final
        
    except Exception as e:
        print(f"\nOcurrió un error en el streaming: {e}")

if __name__ == "__main__":
    main()
