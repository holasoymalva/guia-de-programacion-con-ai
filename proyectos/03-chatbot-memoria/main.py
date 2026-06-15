#!/usr/bin/env python3
import os
import sys
import json
from pathlib import Path
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
ARCHIVO_MEMORIA = "memoria_chat.json"

def cargar_memoria() -> list:
    """Carga el historial de conversación anterior desde el archivo JSON local."""
    if Path(ARCHIVO_MEMORIA).exists():
        try:
            return json.loads(Path(ARCHIVO_MEMORIA).read_text(encoding='utf-8'))
        except Exception as e:
            print(f"Advertencia: No se pudo cargar el archivo de memoria ({e}). Iniciando chat nuevo.")
            return []
    return []

def guardar_memoria(historial: list):
    """Guarda los últimos 30 mensajes de conversación en el archivo JSON local."""
    try:
        # Limitamos la memoria a los últimos 30 mensajes para no saturar costos y contexto
        historial_reciente = historial[-30:] if len(historial) > 30 else historial
        Path(ARCHIVO_MEMORIA).write_text(
            json.dumps(historial_reciente, ensure_ascii=False, indent=2),
            encoding='utf-8'
        )
    except Exception as e:
        print(f"Error al guardar la memoria: {e}")

def chatbot_con_memoria():
    historial = cargar_memoria()
    print("="*50)
    print("🤖 Chatbot con Memoria Persistente")
    print("Escribe 'salir', 'exit' o 'quit' para terminar.")
    print(f"Mensajes cargados de sesiones anteriores: {len(historial)}")
    print("="*50 + "\n")
    
    while True:
        try:
            entrada = input("Tú: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo de la sesión del chat.")
            break
            
        if not entrada:
            continue
            
        if entrada.lower() in ['salir', 'exit', 'quit']:
            guardar_memoria(historial)
            print("Hasta luego. Conversación guardada de forma segura.")
            break
        
        # Agregar el input del usuario al historial
        historial.append({"role": "user", "content": entrada})
        
        # Preparar mensajes en el formato estructurado de la API de Anthropic
        # Filtrar solo campos válidos (role, content) para evitar problemas si se guardan metadatos
        mensajes_api = [{"role": m["role"], "content": m["content"]} for m in historial]
        
        print("\nPensando...", end="\r")
        try:
            respuesta = client.messages.create(
                model="claude-3-7-sonnet-20250219",
                max_tokens=1024,
                system="Eres un asistente amigable y útil con memoria persistente de conversaciones pasadas. Responde siempre en español.",
                messages=mensajes_api
            )
            
            texto_respuesta = respuesta.content[0].text
            print(" "*12, end="\r") # Limpiar el "Pensando..."
            print(f"Asistente: {texto_respuesta}\n")
            
            # Registrar la respuesta en el historial y persistir en disco
            historial.append({"role": "assistant", "content": texto_respuesta})
            guardar_memoria(historial)
            
        except Exception as e:
            print(" "*12, end="\r")
            print(f"Error al conectar con el servidor: {e}\n")
            # Removemos la última entrada del usuario si falló el procesamiento
            historial.pop()

if __name__ == "__main__":
    chatbot_con_memoria()
