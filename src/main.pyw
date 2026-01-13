import os
import keyboard
import datetime
from PIL import ImageGrab
from plyer import notification

# --- CONFIGURATION ---
# Detects the root directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, 'screenshots')
# Path to the icon
ICON_PATH = os.path.join(BASE_DIR, 'assets', 'python_logo.ico')

# Ensure the screenshots folder exists
if not os.path.exists(SCREENSHOTS_DIR):
    os.makedirs(SCREENSHOTS_DIR)

def capture_screen():
    #Captures the primary monitor and saves it to the screenshots folder.
    try:
        # Generate a human-readable timestamp
        # Format: Year-Month-Day_Hour-Minute-Second (e.g., 2026-01-13_14-30-05)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Take the screenshot
        screenshot = ImageGrab.grab()
        
        # Define filename and path
        filename = f"screenshot_{timestamp}.png"
        save_path = os.path.join(SCREENSHOTS_DIR, filename)
        
        # Save file and update the total counter
        screenshot.save(save_path)

        # Feedback to user
        notification.notify(
            title="Screenshot Captured",
            message=f"Image saved as {filename}",
            app_name="Python Screenshot Tool",
            app_icon=ICON_PATH if os.path.exists(ICON_PATH) else None,
            timeout=2 # Seconds the notification stays
        )

    except Exception as e: 
        print(f"Error during capture: {e}")

if __name__ == "__main__":
    # Register the global hotkey (Ctrl + Shift + S)
    keyboard.add_hotkey('ctrl+shift+s', capture_screen)
    
    # Keeps the script running in the background
    keyboard.wait()