# PyShot Utility 📸

A lightweight, high-performance background screenshot tool for Windows, developed in Python. Designed for speed, privacy, and seamless workflow integration.

## 🌟 Key Features

- **Stealth Operation**: Runs as a background process (`.pyw`) to avoid terminal interference.
- **Global Hotkey**: Instantly trigger captures from any app using `Ctrl + Shift + S`.
- **Desktop Notifications**: Real-time visual feedback using native Windows toast notifications with a custom Python icon.
- **Smart File Management**: Automatically saves screenshots with human-readable timestamps (`YYYY-MM-DD_HH-MM-SS`).
- **Zero-Config & Portable**: Uses relative paths, making it functional from any directory.

## 🛠️ Project Structure

```text
PyShot-Utility/
├── assets/            # Project icons and images
├── screenshots/       # Captured images (auto-generated)
├── src/               # Source code
│   └── main.pyw       # Main logic
├── .gitignore         # Prevents personal captures from being uploaded
├── LICENSE            # MIT License
├── README.md          # Documentation
└── requirements.txt   # Dependencies
```

🚀 Getting Started
Prerequisites
Python 3.x

Windows OS (for native notifications and hotkeys)

Installation
Clone the repository:

Bash

git clone [https://github.com/p0sadas/PyShot-Utility.git](https://github.com/p0sadas/PyShot-Utility.git)
Install dependencies:

Bash

pip install -r requirements.txt
Run the utility:

Bash

python src/main.pyw
⌨️ Usage
Press Ctrl + Shift + S at any time to capture your primary monitor.

A notification will appear in the Windows Action Center confirming the save.

🔄 Run at Startup (Optional)
To have PyShot ready every time you boot Windows:

Press Win + R, type shell:startup, and press Enter.

Create a shortcut of src/main.pyw.

Move the shortcut into the Startup folder.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

Developed by Angel Posadas Ruano
