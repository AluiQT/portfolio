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
#https://pillow.readthedocs.io/en/stable/reference/Image.html

from PIL import Image ##Library for image
import numpy as np 
	
img = Image.open('ew.png')
target_width = 70  # Replace with your desired width
target_height = int(target_width * img.height / img.width)
img = img.resize((target_width, target_height))
ary = np.array(img) ##To create an array of the image

# Split the three channels (ripped from https://stackoverflow.com/questions/46385999/transform-an-image-to-a-bitmap)
r, g, b = ary[:, :, 0], ary[:, :, 1], ary[:, :, 2]
r=r.reshape(-1)
g=r.reshape(-1)
b=r.reshape(-1)

# Standard RGB to grayscale
bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
zip(r,g,b)))
bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])

#Now that the array is gray scaled lets print ascii art (https://paulbourke.net/dataformats/asciiart/)
#For now use ten levels of grey .:-=+*#%@

#Since bitmap is a 2d array use a nested loop
#0-255 divided in 10 levels of gray is " .:-=+*#%@" so 255/10 is roughly 26 
#Consider using a data structure for this

for row in bitmap:
    pixelRow = str()
    for pixels in row:
        if pixels > 0 and pixels < 26:
            pixelRow += " "
        elif pixels >= 26 and pixels < 52:
            pixelRow += "."
        elif pixels >= 52 and pixels < 78:
            pixelRow += ":"
        elif pixels >= 78 and pixels < 104:
            pixelRow += "-"
        elif pixels >= 104 and pixels < 130:
            pixelRow += "="
        elif pixels >= 130 and pixels < 156:
            pixelRow += "+"
        elif pixels >= 156 and pixels < 182:
            pixelRow += "*"
        elif pixels >= 182 and pixels < 208:
            pixelRow += "#"
        elif pixels >= 208 and pixels < 234:
            pixelRow += "%"
        elif pixels >= 234:
            pixelRow += "@"
    print(pixelRow)
