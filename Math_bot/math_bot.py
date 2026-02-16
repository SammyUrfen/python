import cv2
import numpy as np
from PIL import ImageGrab, Image
import pyautogui
import time


def main():

    """
    The main function for the Math Bot. This function captures the screen, and finds the tick and cross buttons.
    It then crops the image to get only the equation based on the tick button's coordinates.
    The equation is then passed to the ocr function to get the lhs and rhs.
    The lhs and rhs are then compared, and the bot clicks the tick or cross button accordingly.
    The bot waits for 0.5 seconds before repeating the process.
    """
    while True:

        screen = screencapture()

        # tick_point and cross points are numpy.ndarrays
        tick_point, cross_point = find_buttons(
            im1=screen,
            tick_template_path="templates/tick.png",
            cross_template_path="templates/cross.png"
        )

        # getting the x,y of tick, cross
        if tick_point is not None:
            tick_point_x, tick_point_y = tick_point.tolist()
            cross_point_x, cross_point_y = cross_point.tolist()
        else:
            continue

        # crop the image to get only the equation based on coords of tick point
        eqn = crop_img(screen, tick_point_x, tick_point_y)
        eqn.show()

        """
        Code to get lhs and rhs from ocr

        lhs, rhs = ocr(eqn)
        

        lhs = eval(lhs)
        if lhs == rhs:
            click(tick_point_x, tick_point_y)
        else:
            click(cross_point_x, cross_point_y)

        time.sleep(0.5)
        """
        


def screencapture():
    # Captures a screenshot of the entire screen and returns it as an Image object.

    screenshot = ImageGrab.grab()
    return screenshot


def crop_img(screenshot, tick_x, tick_y):
    """
        Crops the im 

            Args:
            screenshot (Image): The screenshot of the entire screen.
            tick_x (float): The x-coordinate of the tick button.
            tick_y (float): The y-coordinate of the tick button.

        Returns:
            Image: The cropped image.
        """

    left = tick_x - 75
    top = tick_y - 400
    right = tick_x + 275
    bottom = tick_y - 200

    cropped_img = screenshot.crop((left, top, right, bottom))
    return cropped_img


def ocr(crop_img):
    ...
    #returns lhs and rhs of the equation on the image by doing ocr on it





def find_buttons(im1, tick_template_path, cross_template_path, radius=30, min_neighbors=5):

    """
    Finds the location of the tick and cross buttons in the given image.

    Args:
    im1 (Image): The image to search in.
    tick_template_path (str): The path to the image of the tick button.
    cross_template_path (str): The path to the image of the cross button.
    radius (int, optional): The distance a point can be from another point and still be considered a neighbor. Defaults to 30.
    min_neighbors (int, optional): The minimum number of neighbors a point must have to be considered a valid match. Defaults to 5.

    Returns:
    tuple: A tuple of two numpy arrays, the first is the location of the tick button and the second is the location of the cross button.
    """
    im1 = np.array(im1)
    tick_template = cv2.imread(tick_template_path)
    cross_template = cv2.imread(cross_template_path)


    im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    tick_gray = cv2.cvtColor(tick_template, cv2.COLOR_BGR2GRAY)
    cross_gray = cv2.cvtColor(cross_template, cv2.COLOR_BGR2GRAY)

    # Detect SIFT features and compute descriptors
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(im1_gray, None)
    kp_tick, des_tick = sift.detectAndCompute(tick_gray, None)
    kp_cross, des_cross = sift.detectAndCompute(cross_gray, None)

    # Match features using BFMatcher
    matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    tick_matches = matcher.match(des_tick, des1)
    cross_matches = matcher.match(des_cross, des1)

    # Function to find the best match based on proximity
    def find_best_match(matches, keypoints, radius, min_neighbors):
        """
        Finds the best match in the list of matches based on the proximity of the matches.

        Args:
        matches (list): A list of matches from the feature matching algorithm.
        keypoints (list): A list of keypoints from the feature detection algorithm.
        radius (int): The distance a point can be from another point and still be considered a neighbor.
        min_neighbors (int): The minimum number of neighbors a point must have to be considered a valid match.

        Returns:
        tuple: The best match in the list of matches, or None if no match with at least the minimum required neighbors was found.
        """
        best_point = None
        max_neighbors = 0

        for match in matches:
            pt = np.array(keypoints[match.trainIdx].pt)
            # Count neighbors within the radius
            neighbors = sum(np.linalg.norm(pt - np.array(keypoints[m.trainIdx].pt)) < radius for m in matches)

            # Update the best point if current point has more neighbors
            if neighbors > max_neighbors:
                max_neighbors = neighbors
                best_point = pt

            # If the point has at least the minimum required neighbors, return it
            if neighbors >= min_neighbors:
                return best_point

        # If no point with enough neighbors was found, return None
        return best_point if max_neighbors >= min_neighbors else None

    # Find the best points for both tick and cross
    tick_point = find_best_match(tick_matches, kp1, radius, min_neighbors)
    cross_point = find_best_match(cross_matches, kp1, radius, min_neighbors)

    # Return the best locations
    return tick_point, cross_point


def click(x, y):
    #self explanatory   
    pyautogui.click(x, y)



if __name__ == "__main__":
    main()
