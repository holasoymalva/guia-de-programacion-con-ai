# Módulo 9 - Fine-tuning y Modelos Propios 🎛️

El **Fine-tuning** (ajuste fino) es el proceso de tomar un modelo de lenguaje pre-entrenado y entrenarlo con un conjunto de datos específico para enseñarle un tono de comunicación particular, un formato de salida estricto o un conocimiento especializado de dominio.

---

## 🤔 ¿Cuándo hacer Fine-tuning vs RAG?

Uno de los errores más comunes al iniciar en el desarrollo de software con AI es confundir la aplicación de RAG con Fine-tuning.

| Criterio | RAG (Recomendado por defecto) | Fine-tuning |
| :--- | :--- | :--- |
| **Objetivo principal** | Proveer información factual externa y actualizada en tiempo real. | Modificar el comportamiento, tono, formato o estilo del modelo. |
| **Conocimiento dinámico** | Excelente. Ideal si tus documentos cambian constantemente. | Malo. Requiere re-entrenar el modelo cada vez que los datos cambian. |
| **Costo inicial** | Bajo. Solo requiere configurar la base de datos vectorial. | Alto. Requiere preparar miles de ejemplos de calidad y pagar el cómputo. |
| **Prevención de Alucinación**| Muy alta. Se citan fuentes directas en el prompt. | Media. El modelo aprende patrones pero sigue siendo probabilístico. |

---

## 📋 Preparación de Datasets (Formato JSONL)

Para entrenar modelos de OpenAI o Anthropic, la información debe recopilarse en archivos con formato de líneas JSON (`.jsonl`). Cada línea es un objeto JSON que representa un hilo de conversación de ejemplo completo:

```json
{"messages": [{"role": "system", "content": "Eres un asistente de Acme Corp."}, {"role": "user", "content": "Hola"}, {"role": "assistant", "content": "Hola, ¿en qué puedo ayudarte hoy?"}]}
```

### Reglas de Calidad para un Dataset Exitoso
1. **Consistencia**: Todos los ejemplos deben seguir la misma estructura y tono de respuesta.
2. **Volumen mínimo**: Se recomiendan al menos de 50 a 100 ejemplos de alta calidad para percibir mejoras de comportamiento básicas, y más de 1,000 para tareas muy complejas.
3. **Representar Casos Límite**: Incluye ejemplos de cómo debe responder el modelo ante entradas inesperadas o intentos de manipulación de instrucciones.

---

## 🚫 Errores Comunes y Cómo Resolverlos

### 1. Entrenar el modelo con datos sucios, duplicados o incompletos
* **El Problema**: Exportar conversaciones reales de tus chats de soporte directamente al dataset de entrenamiento sin filtrarlas. El modelo aprende las muletillas de tus agentes humanos, errores ortográficos o respuestas incompletas.
* **La Solución**: Limpia exhaustivamente el dataset. Escribe o cura manualmente cada ejemplo de entrada y salida para asegurarte de que representen el "comportamiento ideal".

### 2. Intentar usar Fine-tuning para memorizar datos en lugar de estructurar formatos
* **El Problema**: Hacer fine-tune de un modelo para que memorice un manual de usuario de 300 páginas. Al interrogarlo en producción, el modelo mezcla conceptos y alucina especificaciones técnicas.
* **La Solución**: Usa RAG para inyectar los fragmentos exactos del manual en el prompt, y usa Fine-tuning únicamente si necesitas que el modelo formatee la respuesta de una forma muy particular.

---

## ✍️ Ejercicios Prácticos

### Ejercicio 1: Validar Sintaxis de un Dataset en JSONL
**Instrucciones**: Diseña un script corto en Python que lea un archivo local llamado `dataset.jsonl` y verifique que cada línea contiene un JSON válido con la clave obligatoria `messages`.

#### 🟢 Solución del Ejercicio 1:
```python
import json

def validar_dataset_jsonl(filepath):
    errores = 0
    linea_num = 0
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                linea_num += 1
                line = line.strip()
                if not line:
                    continue  # Ignorar líneas vacías
                    
                try:
                    data = json.loads(line)
                    if "messages" not in data:
                        print(f"Error en Línea {linea_num}: Falta la clave obligatoria 'messages'")
                        errores += 1
                    elif not isinstance(data["messages"], list):
                        print(f"Error en Línea {linea_num}: 'messages' debe ser una lista")
                        errores += 1
                except json.JSONDecodeError as e:
                    print(f"Error de sintaxis JSON en Línea {linea_num}: {e}")
                    errores += 1
                    
        if errores == 0:
            print("¡Éxito! El dataset es completamente válido.")
        else:
            print(f"Se encontraron {errores} errores en el dataset.")
            
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filepath}")

# Uso simulado (creará un archivo temporal para validar)
with open("dataset_temporal.jsonl", "w") as temp:
    temp.write('{"messages": [{"role": "user", "content": "Hola"}]}\n')
    temp.write('{"invalido": "json"}\n')  # Línea incorrecta

validar_dataset_jsonl("dataset_temporal.jsonl")
```
