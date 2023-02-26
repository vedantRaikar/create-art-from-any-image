# image to water color 

#importing libraries 

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

#reading the image
img = cv2.imread(r'C:\Users\vedant raikar\Desktop\project\create art from any image\tree-736885__480.jpg')

#resizing the image 
image_resized = cv2.resize(img , None , fx=1 , fy=1)


#applying median blur to remove the impurities 
image_clear = cv2.medianBlur(image_resized, 3)
image_clear = cv2.medianBlur(image_clear , 3)
image_clear = cv2.medianBlur(image_clear, 3)
image_clear = cv2.medianBlur(image_clear , 3)

#applying edge preservation filter 
image_clear = cv2.edgePreservingFilter(image_resized , sigma_s=0)

#applying bilateral filter which reduces the noise while preserving the edges 

image_filter = cv2.bilateralFilter(image_clear , 3 , 10 , 5)

for i in range(2):
    image_filter = cv2.bilateralFilter(image_filter , 3, 20 , 10)

for i in range(3):
    image_filter = cv2.bilateralFilter(image_filter , 5 , 30 , 10)


#tuning te art
gaussian_mask= cv2.GaussianBlur(image_filter, (7,7), 2)
image_sharp = cv2.addWeighted(image_filter, 1.5, gaussian_mask, -0.5, 0)
image_sharp = cv2.addWeighted(image_sharp, 1.4, gaussian_mask, -0.2, 10)

#showin the image 
cv2.imshow('art', image_sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()




