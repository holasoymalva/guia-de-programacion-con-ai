#!/usr/bin/env python3
import os
import json
from dotenv import load_dotenv
import anthropic

# Cargar variables de entorno
load_dotenv()

# Simulación de bases de datos locales
BASE_DATOS_USUARIOS = {
    "maria@ejemplo.com": {"nombre": "María García", "plan": "pro", "activo": True},
    "juan@ejemplo.com": {"nombre": "Juan Pérez", "plan": "free", "activo": True}
}

# 1. Definición de las funciones de Python locales
def buscar_usuario(email: str) -> dict:
    print(f"   [HERRAMIENTA LOCAL] Buscando usuario con email: {email}...")
    usuario = BASE_DATOS_USUARIOS.get(email)
    if usuario:
        return usuario
    return {"error": "Usuario no encontrado"}

def calcular_descuento(plan: str, monto: float) -> dict:
    print(f"   [HERRAMIENTA LOCAL] Calculando descuento para plan: {plan} y monto: ${monto}...")
    descuentos = {"free": 0.0, "pro": 0.15, "enterprise": 0.30}
    tasa = descuentos.get(plan, 0.0)
    descuento_aplicado = monto * tasa
    monto_final = monto - descuento_aplicado
    return {
        "plan": plan,
        "monto_original": monto,
        "descuento_porcentaje": tasa * 100,
        "descuento_usd": descuento_aplicado,
        "monto_final": monto_final
    }

# 2. Configuración del esquema de herramientas para la API de Anthropic
HERRAMIENTAS = [
    {
        "name": "buscar_usuario",
        "description": "Busca la información básica de perfil de un usuario registrado por su dirección de correo electrónico.",
        "input_schema": {
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "El correo electrónico exacto del usuario a buscar."}
            },
            "required": ["email"]
        }
    },
    {
        "name": "calcular_descuento",
        "description": "Calcula el descuento a aplicar y el monto final a pagar en base al plan del usuario y el monto de compra original.",
        "input_schema": {
            "type": "object",
            "properties": {
                "plan": {
                    "type": "string", 
                    "enum": ["free", "pro", "enterprise"],
                    "description": "El tipo de plan del usuario."
                },
                "monto": {
                    "type": "number", 
                    "description": "El monto total de la compra antes del descuento."
                }
            },
            "required": ["plan", "monto"]
        }
    }
]

def ejecutar_herramienta(nombre: str, input_data: dict):
    if nombre == "buscar_usuario":
        return buscar_usuario(**input_data)
    elif nombre == "calcular_descuento":
        return calcular_descuento(**input_data)
    else:
        return {"error": f"Herramienta '{nombre}' no reconocida."}

def main():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: No se encontró la variable de entorno ANTHROPIC_API_KEY.")
        return

    client = anthropic.Anthropic(api_key=api_key)
    pregunta = "¿Cuánto pagaría el usuario maria@ejemplo.com si su compra es de $100 USD?"
    
    print(f"Iniciando flujo de Tool Use con Claude.")
    print(f"Pregunta: '{pregunta}'\n")

    mensajes = [{"role": "user", "content": pregunta}]
    
    # 1. Enviar la consulta inicial con el listado de herramientas disponibles
    respuesta = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        tools=HERRAMIENTAS,
        messages=mensajes
    )
    
    # 2. Verificar si Claude decidió llamar a una herramienta (stop_reason == "tool_use")
    print(f"Claude detuvo la generación con la razón: '{respuesta.stop_reason}'")
    
    # Registrar la respuesta del asistente en el historial
    mensajes.append({"role": "assistant", "content": respuesta.content})
    
    resultados_herramientas = []
    
    # Iterar sobre los bloques de contenido de la respuesta de Claude
    for bloque in respuesta.content:
        if bloque.type == "tool_use":
            print(f" -> Claude solicita ejecutar: '{bloque.name}' con argumentos: {bloque.input}")
            
            # Ejecutar el código Python local correspondiente
            resultado = ejecutar_herramienta(bloque.name, bloque.input)
            
            # Formatear el resultado en el esquema que espera la API
            resultados_herramientas.append({
                "type": "tool_result",
                "tool_use_id": bloque.id,
                "content": json.dumps(resultado)
            })
            
    if resultados_herramientas:
        # Enviar los resultados de la ejecución de vuelta a Claude
        print("\nEnviando los resultados de las herramientas a Claude para redactar la respuesta final...")
        mensajes.append({"role": "user", "content": resultados_herramientas})
        
        respuesta_final = client.messages.create(
            model="claude-3-7-sonnet-20250219",
            max_tokens=1024,
            tools=HERRAMIENTAS,
            messages=mensajes
        )
        
        print(f"\nRespuesta final de Claude:\n{respuesta_final.content[0].text}")

if __name__ == "__main__":
    main()
