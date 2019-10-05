# CS1CImage
Project 7 of my computer science 1 class in python, Image manipulation

The user can declare an image with FileImage(path/to/image) which only supports 
gifs and ppms. Then the draw image file can be used to draw multiple images
side by side. The rotateImage90 function rotates the image 90 degrees clockwise,
sepiaImage returns a sepia tone version of that image, and transformPixels takes 
in an image, and a function that manipulates a pixel, for example:
transformPixels(myImg, gammaTwo) returns an image that is gamma corrected by two
from the original image.
