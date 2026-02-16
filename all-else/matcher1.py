import cv2
import numpy as np


def find_buttons(im1_path, tick_template_path, cross_template_path, radius=30, min_neighbors=5):
    # Load images
    im1 = cv2.imread(im1_path)
    tick_template = cv2.imread(tick_template_path)
    cross_template = cv2.imread(cross_template_path)

    # Convert images to grayscale
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

for i in range(1,8):
    tick_point, cross_point = find_buttons(
        im1_path=f"Math_bot/tests/{i}.png",
        tick_template_path="Math_bot/templates/tick.png",
        cross_template_path="Math_bot/templates/cross.png"
    )


    print("Tick button location:", tick_point)
    print("Cross button location:", cross_point)

    # Optional: Visualize the match
    def visualize_match(im1_path, tick_point, cross_point):
        im1 = cv2.imread(im1_path)
        if tick_point is not None:
            cv2.circle(im1, tuple(int(x) for x in tick_point), 10, (0, 255, 0), 2)
        if cross_point is not None:
            cv2.circle(im1, tuple(int(x) for x in cross_point), 10, (0, 0, 255), 2)
        cv2.imshow("Matched Locations", im1)
        cv2.imwrite(f"Math_bot/saves/{i}.png", im1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Visualize the matched locations
    visualize_match(f"Math_bot/tests/{i}.png", tick_point, cross_point)
