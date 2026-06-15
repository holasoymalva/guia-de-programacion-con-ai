# Cheatsheet de Atajos de Asistentes de Código ⌨️⚡

Guía rápida de atajos de teclado y comandos de contexto para **GitHub Copilot** y **Cursor** en VS Code.

---

## 🚀 Atajos Esenciales en Cursor

| Combinación de Teclas | Acción | Contexto |
| :--- | :--- | :--- |
| **`Cmd + K`** (macOS)<br>**`Ctrl + K`** (Windows) | **Generar / Editar código** | En línea, en el archivo activo. |
| **`Cmd + L`** (macOS)<br>**`Ctrl + L`** (Windows) | **Abrir Chat de Cursor** | Añade el código seleccionado al chat. |
| **`Cmd + I`** (macOS)<br>**`Ctrl + I`** (Windows) | **Abrir Composer (Multiarchivo)** | Permite editar múltiples archivos a la vez. |
| **`Cmd + Enter`** | **Aceptar cambio sugerido** | En el cuadro de cambios de Cmd+K. |
| **`Option + Enter`** | **Preguntar sobre todo el codebase** | En el Chat de Cursor. |

### Símbolos de Contexto en Cursor (`@`)
- **`@Codebase`**: Analiza todo el repositorio de código.
- **`@Files`**: Apunta a archivos locales específicos.
- **`@Folders`**: Apunta a directorios locales específicos.
- **`@Docs`**: Permite al modelo buscar en documentación externa indexada.
- **`@Git`**: Analiza los diffs del commit actual o commits previos.

---

## 🐱 Atajos Esenciales en GitHub Copilot

| Combinación de Teclas | Acción | Contexto |
| :--- | :--- | :--- |
| **`Tab`** | **Aceptar sugerencia** | Cuando aparece texto gris sugerido. |
| **`Esc`** | **Rechazar sugerencia** | Oculta la sugerencia activa. |
| **`Option + ]`** (macOS)<br>**`Alt + ]`** (Windows) | **Siguiente sugerencia** | Muestra alternativas disponibles. |
| **`Option + [`** (macOS)<br>**`Alt + [`** (Windows) | **Sugerencia anterior** | Muestra alternativas previas. |
| **`Ctrl + Enter`** | **Abrir panel de sugerencias** | Abre una pestaña con hasta 10 opciones de código. |
| **`Cmd + Shift + I`** | **Chat Rápido / Inline Chat** | Abre un cuadro de chat sobre la línea actual. |

### Comandos de Barra Diagonal en Copilot Chat (`/`)
- **`/explain`**: Explica cómo funciona el código seleccionado.
- **`/tests`**: Genera pruebas unitarias para la función seleccionada.
- **`/fix`**: Propone una solución para los errores del código seleccionado.
- **`/help`**: Muestra ayuda de comandos disponibles.
