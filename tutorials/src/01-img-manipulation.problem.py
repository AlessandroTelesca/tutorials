# Exercise #1
# -----------
#
# Load, resize and rotate an image. And display it to the screen.

#  First step is to import the opencv module which is called 'cv2'

#  Check the opencv version

#  Load an image with image reading modes using 'imread'
# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.
# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).
# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.

#  Resize image with 'resize'

#  Rotate image (but keep it rectangular) with 'rotate'

#  Save image with 'imwrite'

#  Show the image with 'imshow'

import cv2

print(cv2.__version__)

image = cv2.imread("./tutorials/data/images/blobtest.jpg", cv2.IMREAD_COLOR)

newHeight = 300
newWidth = 1800
newSize = (newWidth, newHeight)
image = cv2.resize(image, newSize)

image = cv2.rotate(image, cv2.ROTATE_180)

cv2.imwrite("tutorial01Image.jpg", image)

title = "OpenCV Python Tutorial"
cv2.namedWindow(title, cv2.WINDOW_GUI_EXPANDED)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()