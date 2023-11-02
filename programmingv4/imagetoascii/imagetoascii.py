##Load the Image stream to a bitmap object
##Grayscale the bitmap using a Graphics object
##Loop through the image's pixels (because we don't want one ASCII character per pixel, we take one per 10 x 5)
##To let every pixel influence the resulting ASCII char, we loop them and calculate the brightness of the amount of the current 10 x 5 block.
##Finally, append different ASCII characters based for the current block on the calculated amount.

##My goal for this project is to familiar myself with libraries and to learn

#Resources
#https://stackoverflow.com/questions/46385999/transform-an-image-to-a-bitmap
#https://stackoverflow.com/questions/60608024/greyscale-image-python-implementation
#https://en.wikipedia.org/wiki/Grayscale
#https://en.wikipedia.org/wiki/Channel_(digital_image)

from PIL import Image ##Library for image
import numpy as np 
	
img = Image.open('amongus.png')
ary = np.array(img) ##To create an array of the image

#Dot product the array by separating the R,G,B channel and use the dot product
#to gray scale
gray_image = np.dot(ary[..., :3], [0.299, 0.587, 0.114]) 


print(gray_image)