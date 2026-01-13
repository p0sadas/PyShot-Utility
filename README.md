<div align="center">

# 📸 PyShot Utility

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**A lightweight, high-performance background screenshot tool for Windows**

_Designed for speed, privacy, and seamless workflow integration_

---

🌐 **English** | **[Español](README_ES.md)**

---

</div>

## ✨ Key Features

| Feature                       | Description                                                          |
| ----------------------------- | -------------------------------------------------------------------- |
| 🥷 **Stealth Operation**      | Runs as a background process (`.pyw`) to avoid terminal interference |
| ⌨️ **Global Hotkey**          | Instantly trigger captures from any app using `Ctrl + Shift + S`     |
| 🔔 **Desktop Notifications**  | Real-time visual feedback using native Windows toast notifications   |
| 📁 **Smart File Management**  | Auto-saves with human-readable timestamps (`YYYY-MM-DD_HH-MM-SS`)    |
| 🚀 **Zero-Config & Portable** | Uses relative paths — works from any directory                       |

---

## �️ Project Structure

```
PyShot-Utility/
│
├── 📂 assets/            # Project icons and images
├── 📂 screenshots/       # Captured images (auto-generated)
├── 📂 src/
│   └── 🐍 main.pyw       # Main application logic
│
├── 📄 .gitignore         # Prevents personal captures from being uploaded
├── 📄 LICENSE            # MIT License
├── 📄 README.md          # Documentation
└── 📄 requirements.txt   # Dependencies
```

---

## 🚀 Getting Started

### Prerequisites

<<<<<<< HEAD
> **Requirements:**
>
> - 🐍 Python 3.x
> - 🪟 Windows OS (for native notifications and hotkeys)
=======

>>>>>>> 879f437088e3442d4e72445482fa7f31afe79585

### Installation

<<<<<<< HEAD
**1️⃣ Clone the repository:**
=======

>>>>>>> 879f437088e3442d4e72445482fa7f31afe79585

```bash
git clone https://github.com/p0sadas/PyShot-Utility.git
cd PyShot-Utility
```

**2️⃣ Install dependencies:**

```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
**3️⃣ Run the utility:**
=======

>>>>>>> 879f437088e3442d4e72445482fa7f31afe79585

```bash
python src/main.pyw
```

---

## ⌨️ Usage

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd>

Press the hotkey at any time to capture your primary monitor. A notification will appear in the Windows Action Center confirming the save! ✅

---

## 🔄 Run at Startup (Optional)

Want PyShot ready every time you boot Windows? Follow these steps:

1. Press <kbd>Win</kbd> + <kbd>R</kbd>, type `shell:startup`, and press <kbd>Enter</kbd>
2. Create a shortcut of `src/main.pyw`
3. Move the shortcut into the **Startup** folder

🎉 _That's it! PyShot will now launch automatically on boot._

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### 💻 Developed with ❤️ by **Angel Posadas Ruano**

_If you find this useful, consider giving it a ⭐!_

</div>
