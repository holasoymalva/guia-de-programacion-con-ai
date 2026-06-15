#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno
load_dotenv()

# Inicializar cliente
# OpenAI lee la variable OPENAI_API_KEY por defecto
client = OpenAI()

def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: No se encontró la variable de entorno OPENAI_API_KEY.")
        return

    print("Enviando consulta a OpenAI (Model: gpt-4o-mini)...")
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un tutor técnico conciso. Responde siempre en español."},
                {"role": "user", "content": "¿Por qué es importante usar variables de entorno en el desarrollo?"}
            ],
            temperature=0.3
        )
        
        # Extraer y mostrar el texto de la respuesta
        respuesta = completion.choices[0].message.content
        print(f"\nRespuesta:\n{respuesta}")
        
    except Exception as e:
        print(f"Ocurrió un error en la llamada: {e}")

if __name__ == "__main__":
    main()
