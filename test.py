import pyautogui
import time

for i in range(1, 10):
    message = f"I love you {i} - {i}"
    pyautogui.write(message)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Add a short delay to ensure the text is copied
    print(f"Message {i} copied to clipboard: {message}")
    pyautogui.press('enter')  # Press Enter to move to the next line (optional)
