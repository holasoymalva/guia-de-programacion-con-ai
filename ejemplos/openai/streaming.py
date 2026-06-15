#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno
load_dotenv()

client = OpenAI()

def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: No se encontró la variable de entorno OPENAI_API_KEY.")
        return

    print("Iniciando llamada con streaming a OpenAI (Model: gpt-4o-mini)...")
    print("Respuesta: ", end="", flush=True)
    
    try:
        # Habilitar stream=True para recibir fragmentos
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Explícame qué son los decoradores en Python en dos párrafos cortos."}
            ],
            stream=True
        )
        
        # Iterar e imprimir tokens en consola en tiempo real
        for chunk in stream:
            # Validar que contenga contenido de texto
            if chunk.choices[0].delta.content is not None:
                sys.stdout.write(chunk.choices[0].delta.content)
                sys.stdout.flush()
        print() # Salto de línea final
        
    except Exception as e:
        print(f"\nOcurrió un error en la llamada con streaming: {e}")

if __name__ == "__main__":
    main()
