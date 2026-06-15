# Guía de Contribución 🚀

¡Gracias por tu interés en contribuir a la **Guía de Programación con AI**! Este proyecto es posible gracias a personas como tú que dedican su tiempo para mejorar este recurso para la comunidad hispanohablante.

Aquí te mostramos cómo puedes participar.

## 🗺️ Formas de Contribuir

1. **Mejorar el contenido**: Corregir errores ortográficos, aclarar explicaciones o expandir las guías teóricas en los módulos.
2. **Añadir ejemplos de código**: Crear mejores scripts prácticos en la carpeta `ejemplos/` o en `proyectos/`.
3. **Reportar Bugs o Proponer Features**: Si encuentras algo roto o crees que falta una herramienta vital, abre un Issue.
4. **Compartir**: Cuéntale a tus amigos y compañeros sobre esta guía. ¡Una estrella en el repositorio ayuda muchísimo!

---

## 🛠️ Nuestro Flujo de Trabajo

### 1. Requisitos Previos
Asegúrate de tener instalado:
- **Git**
- **Python 3.10+** (para probar los ejemplos locales)
- Una API Key de algún proveedor si vas a desarrollar características de código (por ejemplo, OpenAI, Anthropic o Gemini).

### 2. Pasos para Contribuir

1. **Haz un Fork** de este repositorio en tu cuenta de GitHub.
2. **Clona tu fork** localmente:
   ```bash
   git clone https://github.com/tu-usuario/guia-de-programacion-con-ai.git
   cd guia-de-programacion-con-ai
   ```
3. **Crea una nueva rama** descriptiva para tus cambios:
   ```bash
   git checkout -b feature/mi-nueva-seccion
   # o para correcciones
   git checkout -b fix/corregir-enlace-modulo-2
   ```
4. **Realiza tus cambios** y asegúrate de verificar que:
   - Todo el contenido esté escrito en **español claro**.
   - Los bloques de código de Markdown usen la sintaxis correcta.
   - Si añades código Python, tenga sintaxis correcta y sea ejecutable.
5. **Realiza commits** limpios siguiendo la convención de [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/):
   ```bash
   git commit -m "feat: agregar sección de Vibe Coding en módulo 5"
   git commit -m "fix: corregir llamada a la API de Anthropic en ejemplo de streaming"
   ```
6. **Sube tu rama (Push)** a tu fork de GitHub:
   ```bash
   git push origin feature/mi-nueva-seccion
   ```
7. **Abre un Pull Request (PR)** hacia la rama `main` del repositorio original.

---

## 🎨 Guía de Estilo

- **Idioma**: Español neutro y comprensible. Evita tecnicismos excesivos sin explicarlos previamente en el glosario.
- **Formato**: Usa Markdown estándar. Aprovecha las alertas de GitHub (`> [!NOTE]`, `> [!IMPORTANT]`, etc.) de forma estratégica.
- **Código**:
  - Usa nombres de variables descriptivos en español (o inglés estándar de programación si es más natural).
  - Incluye comentarios claros explicando el razonamiento del prompt o el uso de la API.
  - Asegúrate de usar variables de entorno para las credenciales y credenciales sensibles (`dotenv`).

---

## 🤝 Código de Conducta

Esperamos un ambiente de respeto, inclusión y colaboración constructiva. Las críticas al código o contenido deben ser siempre amigables y enfocadas en la mejora continua.

¡Hagamos de esta la mejor guía de programación con inteligencia artificial en español! 💚
