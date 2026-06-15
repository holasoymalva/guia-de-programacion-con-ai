#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Cargar variables de entorno
load_dotenv()

def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: No se encontró la variable de entorno OPENAI_API_KEY.")
        return

    # 1. Definir la plantilla de prompt
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Eres un experto en gastronomía internacional. Responde de manera amigable en español."),
        ("human", "Dime cuáles son los 3 ingredientes tradicionales más importantes del plato {plato} y por qué.")
    ])

    # 2. Inicializar el modelo
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

    # 3. Inicializar el parser de salida simple
    parser = StrOutputParser()

    # 4. Crear la cadena (Chain) utilizando LCEL (LangChain Expression Language)
    # El operador '|' une el prompt, el modelo y el parser en un pipeline secuencial
    chain = prompt_template | model | parser

    plato_ingresado = "Tacos al Pastor"
    print(f"Iniciando llamada de LangChain para el plato: '{plato_ingresado}'...")

    try:
        # Invocar la cadena pasando las variables requeridas por el prompt
        resultado = chain.invoke({"plato": plato_ingresado})
        print(f"\nRespuesta de LangChain:\n{resultado}")
    except Exception as e:
        print(f"Error al ejecutar la cadena de LangChain: {e}")

if __name__ == "__main__":
    main()
