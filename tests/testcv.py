import cv2

# Load the image
img = cv2.imread('images/avatar.png')

# Check if the image was loaded successfully
if img is None:
    print('Failed to load image.')
else:
    # Save the image
    cv2.imwrite('output_avatar.png', img)
    print('Image saved as output_avatar.png')
