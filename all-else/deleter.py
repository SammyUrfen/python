import pyautogui
import time

def delete_watermarks(pages=50):  # You can change the number of pages
    print("You have 10 seconds to switch to LibreOffice Draw...")
    time.sleep(10)

    for i in range(pages):
        print(f"Processing page {i + 1}")

        # Move to center of screen (adjust if needed)
        # screen_width, screen_height = pyautogui.size()
        # pyautogui.moveTo(screen_width / 2, screen_height / 2)

        # Click to select watermark
        pyautogui.click()
        time.sleep(0.1)

        # Press delete
        pyautogui.press('delete')
        time.sleep(0.25)

        # Press Page Down to move to next page
        pyautogui.press('pagedown')
        time.sleep(0.3)

    print("Done!")

if __name__ == "__main__":
    delete_watermarks(pages=90)
