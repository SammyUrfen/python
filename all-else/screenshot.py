from PIL import ImageGrab, Image

def capture_entire_screen():
    """
    Captures a screenshot of the entire screen and returns it as an Image object.
    """
    screenshot = ImageGrab.grab()  # Capture the entire screen
    return screenshot

def crop_image_based_on_tick(screenshot, tick_x, tick_y):
    """
    Crops the image to a specific region based on the tick button coordinates.

    Args:
        screenshot (Image): The screenshot of the entire screen.
        tick_x (float): The x-coordinate of the tick button.
        tick_y (float): The y-coordinate of the tick button.

    Returns:
        Image: The cropped image.
    """
    # Define the bounding box for the equation area
    left = tick_x - 75
    top = tick_y - 400
    right = tick_x + 275
    bottom = tick_y - 200

    # Crop the image to the defined bounding box
    cropped_img = screenshot.crop((left, top, right, bottom))
    return cropped_img

# Usage example
if __name__ == "__main__":
    # Step 1: Capture the entire screen
    entire_screen = capture_entire_screen()
    entire_screen.save("Math_bot/saves/screen.png")

    # Step 2: Define the tick button coordinates (replace these with the actual coordinates)
    tick_button_x = 860.2255249  # X-coordinate of the tick button
    tick_button_y = 736.39825439  # Y-coordinate of the tick button

    # Step 3: Crop the image based on the tick button coordinates
    cropped_image = crop_image_based_on_tick(entire_screen, tick_button_x, tick_button_y)

    # Step 4: Save or display the cropped image
    cropped_image.save("Math_bot/saves/crop.png")
    cropped_image.show()
