import skimage
from skimage import data
from scipy import signal
from scipy import ndimage
from scipy.misc import imsave
import matplotlib.pyplot as plt
import matplotlib.cm as cm #
import numpy as np
import scipy as scipy
import math

fruit1 = skimage.data.imread("fruit.jpg", True)
fruit = skimage.data.imread("fruit.jpg", True)
template1 = np.copy(fruit[100:240, 100:315])

def shiftLeft(image, numOfPixels):
    for rownum in range(0, len(image), 1):
    # counts up by 1 from 0 to num of rows exclusive
        for colnum in range(0, len(image[0]) - numOfPixels, 1):
        # counts up by 1 from 0 to num of cols minus the num of pixels you want to shift by, also exclusive
            image[rownum][colnum] = image[rownum][colnum + numOfPixels]
        # sets current pixel value to the rgb value of the pixel that is numOfPixels away from it
    for rownum in range(0, len(image), 1):
        for colnum in range(len(image[0]) - numOfPixels, len(image[0]), 1 ):
        # the top two lines basically iterate through the part of the matrix that was skipped previously
            image[rownum][colnum] = 0
            # sets those rgb values to 0 - not necessary, but makes shift easy to see

def shiftRight(image, numOfPixels):
    for rownum in range(len(image) -1, -1, -1):
        for colnum in range(len(image[0]) - 1, numOfPixels - 2, -1):
            image[rownum][colnum] = image[rownum][colnum - numOfPixels]
    for rownum in range(len(image) -1, -1, -1):
        for colnum in range(numOfPixels - 1, -1, -1):
            image[rownum][colnum] = 0

def shiftUp(image, numOfPixels):
    for rownum in range(0, len(image) - numOfPixels, 1):
        for colnum in range(0, len(image), 1):
            image[rownum][colnum] = image[rownum + numOfPixels][colnum]
    for rownum in range(len(image) - numOfPixels, len(image), 1):
        for colnum in range(0, len(image), 1):
            image[rownum][colnum] = 0

def shiftDown(image, numOfPixels):
    for rownum in range(len(image) - 1, numOfPixels - 2, -1):
        for colnum in range(len(image[0]) - 1, -1, -1):
            image[rownum][colnum] = image[rownum - numOfPixels][colnum]
    for rownum in range(numOfPixels - 1, -1, -1):
        for colnum in range(len(image[0]) - 1, -1, -1):
            image[rownum][colnum] = 0

def shiftImage(image):
    numOfPixelsDown = int(input("How many pixels do you want the image to shift down by? "))
    numOfPixelsRight = int(input("How many pixels do you want the image to shift right by? "))
    if (numOfPixelsRight > 0):
        shiftRight(image,numOfPixelsRight)
    elif (numOfPixelsRight < 0):
        numOfPixelsRight *= -1
        shiftLeft(image, numOfPixelsRight)
    if (numOfPixelsDown > 0):
        shiftDown(image,numOfPixelsDown)
    elif (numOfPixelsDown < 0):
        numOfPixelsDown *= -1
        shiftUp(image, numOfPixelsDown)

def normalizeHelper(image):
    sumOfSquares = 0
    for r in range(len(image)):
        for c in range(len(image[r])):
            sumOfSquares += (image[r][c] ** 2)
    normVal = math.sqrt(sumOfSquares)
    return normVal

# template: width = 3 height = 3
def normalize(image, templateWidth, templateHeight):
    normalizedImage = np.copy(image)
    for r in range(len(image)):
        for c in range(len(image[r])):
    #for r in range(templateHeight - 1 / 2, len(image) - ((templateHeight - 1) / 2) - 1, 1):
        #for c in range(templateWidth - 1 / 2, len(image[0]) - ((templateWidth - 1) / 2) - 1, 1):
            halfHeight = int((templateHeight - 1) / 2) #1
            #print halfHeight
            halfWidth = int((templateWidth - 1) / 2) #1
            #print halfWidth
            #lol = image[0:3, 0:3]
            if ((r - halfHeight >= 0) and (r + halfHeight < len(image)) and (c - halfWidth >= 0) and (c + halfWidth < len(image[r]))):
                template = image[r - halfHeight:r + halfHeight + 1][c - halfWidth:c + halfWidth + 1]
            #print "hi"
                #template = image[r - ((templateHeight - 1) / 2):r + ((templateHeight - 1) / 2) + 1, c - ((templateWidth - 1) / 2):c + ((templateWidth - 1) / 2)] + 1]
                normalizedImage[r][c] = normalizeHelper(template)
                #print normalizedImage[r][c]
            else:
                normalizedImage[r][c] = 0
                #print "hi"
    return normalizedImage

shiftImage(fruit)

#corr = scipy.signal.correlate2d(apple1, apple1)

def normalizeHelper(image):
    sumOfSquares = 0
    for r in range(len(image)):
        for c in range(len(image[r])):
            sumOfSquares += (image[r][c] ** 2)
    normVal = (math.sqrt(sumOfSquares)) + 1
    return normVal

def normalize(image, templateWidth, templateHeight):
    normalizedImage = np.copy(image)
    halfHeight = int((templateHeight - 1) / 2)
    halfWidth = int((templateWidth - 1) / 2)
    for r in range(halfHeight, len(image) - halfHeight, 1):
        for c in range(halfWidth, len(image[r]) - halfWidth, 1):
            template = np.copy(image[r-halfHeight:r+halfHeight+1, c-halfWidth:c+halfWidth+1])
            normalizedImage[r][c] = normalizeHelper(template)
    for r in range(halfHeight):
        normalizedImage[r] = 1
    for r in range(len(image) - halfHeight,len(image),1):
        normalizedImage[r] = 1
    for r in range(halfHeight, len(image) - halfHeight, 1):
        for c in range(0, halfWidth, 1):
            normalizedImage[r][c] = 1
    for r in range(halfHeight, len(image) - halfHeight, 1):
        for c in range(len(image[0]) - halfWidth, len(image[0]), 1):
              normalizedImage[r][c] = 1
    return normalizedImage

plt.gray()


plt.subplot(231)
plt.imshow(fruit1, cmap=plt.cm.gray)
plt.title('Original')
plt.axis('off')
plt.subplot(232)
plt.imshow(fruit, cmap=plt.cm.gray)
plt.title('Translation')
plt.axis('off')
plt.subplot(233)
plt.imshow(template1, cmap=plt.cm.gray)
plt.title('Patch')
plt.axis('off')
plt.subplot(234)
convolvedFruit = scipy.signal.fftconvolve(fruit, template1, mode = 'same')
scipy.misc.imsave("convfruit1.png", convolvedFruit)
plt.imshow(convolvedFruit, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Convolution')
#plt.subplot(224)
#plt.imshow(corr, cmap=plt.cm.gray)
#plt.axis('off')
#plt.title('Correlation')
plt.subplot(235)
norm = normalize(fruit, 10, 10)
scipy.misc.imsave("normFruit.png",norm)
plt.imshow(norm, cmap=plt.cm.gray)
plt.title('Normalized')
plt.axis('off')
plt.subplot(236)
normConvolved = np.copy(convolvedFruit)
scipy.misc.imsave("NormConvolved.png",normConvolved)
# if it says index out of bounds or something like that, fix the convolve function
for r in range(len(normConvolved)):
    for c in range(len(normConvolved[1])):
        if (norm[r][c] != 1) :
            normConvolved[r][c] = convolvedFruit[r][c]/norm[r][c]
plt.imshow(normConvolved, cmap=plt.cm.gray)
brightSpot = np.unravel_index(np.argmax(normConvolved), normConvolved.shape)
facecolor='none' # this returns the coordinates of the max val
plt.title('C/N')

plt.show()

