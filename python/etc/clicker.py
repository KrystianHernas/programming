import pyautogui
import time

def perform_mouse_click():
    # Simulate a mouse click at the current mouse position
    pyautogui.click()

    print("Mouse click performed")

# Main loop
while True:
    try:
        # Perform mouse click
        perform_mouse_click()

        # Wait for 2 minutes
        time.sleep(120)  # 120 seconds = 2 minutes

    except KeyboardInterrupt:
        # Handle Ctrl+C to exit the program
        print("\nProgram terminated by user")
        break
