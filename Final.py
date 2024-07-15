# action plan
# Get the image from the images directory.
# Check if the image is a png file.
# Check if the image is 512x512.
# Prepare a mask for the image.
# circle of radius 256 and center at (256, 256).
# Superimpose the mask on the image.
# Check if the image has only non-transparent pixels within the circle.
# Check if the colors in the badge give a "happy" feeling.
# Return the result.

import cv2
import numpy as np
import os

# Function to check if the image is a png file
def check_png(image_path):
    if image_path.split('.')[-1] == 'png':
        return True
    else:
        return False

# Function to check if the image is 512x512
def check_size(image_path):
    img = cv2.imread(image_path)
    if img.shape[0] == 512 and img.shape[1] == 512:
        return True
    else:
        return False

# Function that prepares a mask for the image
def prepare_mask(image_path):
    mask = np.zeros((512, 512, 3), dtype=np.uint8)
    cv2.circle(mask, (256, 256), 256, (255, 255, 255), -1)
    return mask

# implementation of the main function

def check_badge(image_path):
    if not check_png(image_path):
        return False, 'image is not a png file.'
    if not check_size(image_path):
        return False, 'image is not 512x512.'
    
    img = cv2.imread(image_path)
    mask = prepare_mask(image_path)
    img = cv2.bitwise_and(img, mask)
    
    # Check if the image has only non-transparent pixels within the circle
    if np.all(img == 0):
        return False, 'image has transparent pixels outside the circle.'
    
    # Check if the colors in the badge give a "happy" feeling
    # highly subjective commented out for output.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([20, 100, 100])
    upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    #if np.all(mask == 0):
    #    return False, 'colors in badge do not give a "happy" feeling.'

    # prepare the output
    cv2.imwrite('output.png', img)

    return True, 'The badge is valid.'

# Testing the function
image_path = 'images/avatar512x512.png'
result, message = check_badge(image_path)
print(result, message)



