#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import anthropic

# Cargar variables de entorno
load_dotenv()

def main():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: No se encontró la variable de entorno ANTHROPIC_API_KEY.")
        return

    # Inicializar cliente de Anthropic
    client = anthropic.Anthropic(api_key=api_key)

    print("Enviando consulta a Claude (Model: claude-3-7-sonnet-20250219)...")
    try:
        message = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": "Explícame qué es un closure en JavaScript con un ejemplo de código corto."}
            ]
        )
        
        # Extraer respuesta
        texto = message.content[0].text
        print(f"\nRespuesta:\n{texto}")
        
    except Exception as e:
        print(f"Error al llamar a la API de Anthropic: {e}")

if __name__ == "__main__":
    main()
