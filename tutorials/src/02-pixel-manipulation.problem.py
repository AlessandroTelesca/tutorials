# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place,
# count the used colors in the image

import cv2
import numpy as np

# Loading images in grey and color
grayScaleImage = cv2.imread("./tutorials/data/images/Bumbu_Rawon.jpg", cv2.IMREAD_GRAYSCALE)
colorImage = cv2.imread("./tutorials/data/images/Bumbu_Rawon.jpg", cv2.IMREAD_COLOR)

# Do some print out about the loaded data using type, dtype and shape
print("Color image type:" , type(colorImage) , "Grayscale image type:" , type(grayScaleImage))
print("Color image dtype:" , colorImage.dtype , "Grayscale image dtype:" , grayScaleImage.dtype)
print("Color image shape:" , colorImage.shape , "Grayscale image shape:" , grayScaleImage.shape)

# Extract the size or resolution of the image
height, width, channels = colorImage.shape
print("Height:", height, "Width:", width, "Channels:", channels)

# Resize image
newWidth = 30
newHeight = 20
newSize = (newWidth, newHeight)
resizedImage = cv2.resize(grayScaleImage, newSize)
heightres, widthres = resizedImage.shape
print("Height:", heightres, "Width:", widthres)

# Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for general access on ndarrays
# Print first row
# print("print first row" , grayScaleImage[:,1])

# Print first column
# print("print first column" , grayScaleImage[1,:])

# Continue with the color image

#  Set an area of the image to black
colorImage[100:200, 300:400] = 0

# Show the image and wait until key pressed

# Find all used colors in the image
# print("Used colors in the image", colorImage[:,:])

# Copy one part of an image into another one
maxheight, maxwidth, channels = colorImage.shape

onion = colorImage[0:100, 100:200]
colorImage[maxheight-100:maxheight, maxwidth-100:maxwidth] = onion

# Save image to a file

#  Show the image again
#show color image
cv2.namedWindow("Color", cv2.WINDOW_GUI_NORMAL)
imshow = cv2.imshow("Color", colorImage)

#show gray image
cv2.namedWindow("Gray", cv2.WINDOW_GUI_NORMAL)
imshow = cv2.imshow("Gray", grayScaleImage) 

# show resized image
cv2.namedWindow("Resized", cv2.WINDOW_GUI_NORMAL)
imshow = cv2.imshow("Resized", resizedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Show the original image (copy demo)
