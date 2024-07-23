import time
import pyautogui

def take_screenshot(filename="screenshot.png", delay=4):
    
    try:
        time.sleep(delay)
        img = pyautogui.screenshot(filename)
        img.show()
        print(f"Screenshot saved as {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

take_screenshot("test.png")
