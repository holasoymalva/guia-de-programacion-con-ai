#!/usr/bin/env python3
import re
from datetime import datetime
from pathlib import Path

def actualizar_fecha_readme(readme_path: Path):
    if not readme_path.exists():
        print(f"Error: No se encontró el archivo {readme_path}")
        return False
        
    print(f"Leyendo {readme_path}...")
    contenido = readme_path.read_text(encoding="utf-8")
    
    # Obtener la fecha actual formateada en español
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    fecha_hoy = datetime.now()
    fecha_formateada = f"{meses[fecha_hoy.month - 1]} {fecha_hoy.year}"
    
    # Buscar el patrón de última actualización en el README
    # Formato esperado: *Ultima actualizacion: Junio 2025 · Version 3.0*
    patron = r"\*Ultima actualizacion: [a-zA-Z]+ \d{4} · Version \d+\.\d+\*"
    reemplazo = f"*Ultima actualizacion: {fecha_formateada} · Version 3.0*"
    
    if re.search(patron, contenido):
        nuevo_contenido = re.sub(patron, reemplazo, contenido)
        readme_path.write_text(nuevo_contenido, encoding="utf-8")
        print(f"README actualizado con éxito. Nueva fecha: {fecha_formateada}")
        return True
    else:
        print("Advertencia: No se encontró la etiqueta de última actualización en el formato esperado.")
        return False

def main():
    readme_principal = Path("README.md")
    actualizar_fecha_readme(readme_principal)

if __name__ == "__main__":
    main()
