##How?
##From StackOverflow

##Load the Image stream to a bitmap object
##Grayscale the bitmap using a Graphics object
##Loop through the image's pixels (because we don't want one ASCII character per pixel, we take one per 10 x 5)
##To let every pixel influence the resulting ASCII char, we loop them and calculate the brightness of the amount of the current 10 x 5 block.
##Finally, append different ASCII characters based for the current block on the calculated amount.

from bitmap import BitMap ##Use bitmap library
	
