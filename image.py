from cImage import *

# object -> object
def sepiaTone(pixel):
    """Takes in a pixel and converts it to sepia and returns it"""
    R = pixel.getRed()
    G = pixel.getGreen()
    B = pixel.getBlue()
    newR = min(int(R*0.393+G*0.769+B*0.189),255)
    newG = min(int(R*0.349+G*0.686+B*0.168),255)
    newB = min(int(R*0.272+G*0.534+B*0.131),255)
    return Pixel(newR,newG,newB)

# object -> object
def sepiaImage(image):
    """Takes in a FileImage object and returns another FileImage
    object that has been changed to have a sepia tone"""
    newImg = EmptyImage(image.getWidth(),image.getHeight())
    for row in range(image.getWidth()):
        for col in range(image.getHeight()):
            newImg.setPixel(row,col,sepiaPixel(image.getPixel(row,col)))
    return newImg

# object,number -> object
def gammaN(pixel,N):
    """Takes in a pixel object and does gamma correction on
    it with a gamma value of N"""
    R = pixel.getRed()
    G = pixel.getGreen()
    B = pixel.getBlue()
    Y = min((0.00117 * R + 0.00230 * G + 0.000447 * B),1)
    U = max(min((-0.000577 * R - 0.00113 * G + 0.00171 * B),0.5),-0.5)
    V = max(min((0.00241 * R - 0.00202 * G - 0.00039 * B),0.5),-0.5)
    Y = (Y ** N)
    R = max(min(int(255 * (Y + 1.13983 * V)),255),0)
    G = max(min(int(255 * (Y - 0.39465 * U - 0.58060 * V)),255),0)
    B = max(min(int(255 * (Y + 2.03211 * U)),255),0)
    return Pixel(R,G,B)

# object -> object
def gammaTwo(pixel):
    """Takes in a pixel object and does gamma correction on
    it with a gamma value of 2"""
    return gammaN(pixel,2)

# object -> object
def gammaHalf(pixel):
    """Takes in a pixel object and does gamma correction on
    it with a gamma value of 1/2"""
    return gammaN(pixel,0.5)

# object, function -> object
def transformPixels(image,pixelProcedure):
    """Takes in an image and a pixel procedure and returns
    a new image transformed by the procedure"""
    newImg = EmptyImage(image.getWidth(),image.getHeight())
    for row in range(image.getWidth()):
        for col in range(image.getHeight()):
            newPixel = pixelProcedure(image.getPixel(row,col))
            newImg.setPixel(row,col,newPixel)
    return newImg

# object -> object
def rotateImage90(image):
    """Takes in an image and returns a new image equivalent to
    the first one rotated 90 degrees clockwise"""
    newImg = EmptyImage(image.getHeight(),image.getWidth())
    for row in range(image.getWidth()):
        for col in range(image.getHeight()):
            newImg.setPixel((image.getHeight()-1-col),(row),image.getPixel(row,col))
    return newImg

# str,list of object -> void
def drawImages(title,images):
    """Takes in a title and a list of images and creates a window
    with a title of title and with all images in the list of
    images within it"""
    width = 2
    height = 2
    for image in images:
        width += image.getWidth()
        if image.getHeight()>height:
            height = image.getHeight()+2
    myWin = ImageWin(title,width,height)
    width = 1
    height = 1
    for image in images:
        image.setPosition(width,height)
        width += image.getWidth()+1
        image.draw(myWin)
    # Exit on click does not work on my version of python/cImage


myImg = FileImage("tennis.gif")
myImg2 = FileImage("tennis2.gif")
drawImages("a",[myImg2, rotateImage90(myImg2)])
#drawImages("Tennis", [myImg,transformPixels(rotateImage90(myImg),sepiaTone),transformPixels(rotateImage90(myImg),gammaTwo)])

    
                
