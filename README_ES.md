<div align="center">

# 📸 PyShot Utility

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)](LICENSE)

**Una herramienta ligera y de alto rendimiento para capturas de pantalla en Windows**

_Diseñada para velocidad, privacidad e integración perfecta con tu flujo de trabajo_

---

🌐 **[English](README.md)** | **Español**

---

</div>

## ✨ Características Principales

| Característica                         | Descripción                                                                        |
| -------------------------------------- | ---------------------------------------------------------------------------------- |
| 🥷 **Operación Sigilosa**              | Se ejecuta como proceso en segundo plano (`.pyw`) sin interferir con la terminal   |
| ⌨️ **Atajo Global**                    | Captura instantánea desde cualquier aplicación con `Ctrl + Shift + S`              |
| 🔔 **Notificaciones de Escritorio**    | Retroalimentación visual en tiempo real mediante notificaciones nativas de Windows |
| 📁 **Gestión Inteligente de Archivos** | Guarda automáticamente con marcas de tiempo legibles (`YYYY-MM-DD_HH-MM-SS`)       |
| 🚀 **Sin Configuración y Portátil**    | Usa rutas relativas — funciona desde cualquier directorio                          |

---

## 🗂️ Estructura del Proyecto

```
PyShot-Utility/
│
├── 📂 assets/            # Iconos e imágenes del proyecto
├── 📂 screenshots/       # Capturas guardadas (se genera automáticamente)
├── 📂 src/
│   └── 🐍 main.pyw       # Lógica principal de la aplicación
│
├── 📄 .gitignore         # Evita que tus capturas personales se suban
├── 📄 LICENSE            # Licencia MIT
├── 📄 README.md          # Documentación en inglés
├── 📄 README_ES.md       # Documentación en español
└── 📄 requirements.txt   # Dependencias
```

---

## 🚀 Primeros Pasos

### Requisitos Previos

> **Necesitas:**
>
> - 🐍 Python 3.x
> - 🪟 Windows OS (para notificaciones nativas y atajos de teclado)

### Instalación

**1️⃣ Clona el repositorio:**

```bash
git clone https://github.com/p0sadas/PyShot-Utility.git
cd PyShot-Utility
```

**2️⃣ Instala las dependencias:**

```bash
pip install -r requirements.txt
```

**3️⃣ Ejecuta la utilidad:**

```bash
python src/main.pyw
```

---

## ⌨️ Uso

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd>

Presiona el atajo en cualquier momento para capturar tu monitor principal. ¡Aparecerá una notificación en el Centro de Acciones de Windows confirmando que se guardó! ✅

---

## 🔄 Ejecutar al Iniciar Windows (Opcional)

¿Quieres que PyShot esté listo cada vez que enciendas tu computadora? Sigue estos pasos:

1. Presiona <kbd>Win</kbd> + <kbd>R</kbd>, escribe `shell:startup` y presiona <kbd>Enter</kbd>
2. Crea un acceso directo de `src/main.pyw`
3. Mueve el acceso directo a la carpeta de **Inicio**

🎉 _¡Listo! PyShot se iniciará automáticamente con Windows._

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** — consulta el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">

### 💻 Desarrollado con ❤️ por **Angel Posadas Ruano**

_Si te resulta útil, ¡considera darle una ⭐!_

</div>
