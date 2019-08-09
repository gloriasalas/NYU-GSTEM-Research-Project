import numpy as np
import matplotlib
import scipy.misc 
import skimage
from scipy import ndimage
from skimage import data
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy import signal
from scipy import misc

pluto = skimage.data.imread("pluto.png", True)
pluto2 = skimage.data.imread("pluto.png", True)
template1 = np.copy(pluto[100:240, 100:315])

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

def shiftDown(image, numOfPixels):
    for rownum in range(len(image) - 1, numOfPixels - 2, -1):
        for colnum in range(len(image[0]) - 1, -1, -1):
            image[rownum][colnum] = image[rownum - numOfPixels][colnum]
    for rownum in range(numOfPixels - 1, -1, -1):
        for colnum in range(len(image[0]) - 1, -1, -1):
            image[rownum][colnum] = 0
            
def shiftUp(image, numOfPixels):
    for rownum in range(0, len(image) - numOfPixels, 1):
        for colnum in range(0, len(image), 1):
            image[rownum][colnum] = image[rownum + numOfPixels][colnum]
    for rownum in range(len(image) - numOfPixels, len(image), 1):
        for colnum in range(0, len(image), 1):
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
shiftImage(pluto)

def maximumImage(image):
     =(column >= 0, col < nCols, ++col )   
     = (rownum >= 0, row < nRows, ++row ) 
    #// do something with array[row][col]
print (maximumImage)

conv = scipy.signal.fftconvolve(pluto, pluto2, mode = 'same')

#corr = scipy.signal.correlate2d(pluto, pluto2)

plt.gray()
plt.imshow(pluto2)

plt.subplot(221)
plt.imshow(pluto, cmap=plt.cm.gray)
scipy.misc.imsave('translatedpluto.png', pluto)
plt.axis('off')
plt.title('Translation')
plt.subplot(222)
plt.imshow(pluto2, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Original')
plt.subplot(223)
plt.imshow(conv, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Convolution')
plt.subplot(224)
template1 = np.copy(pluto[100:240, 100:315]) # right eye
plt.imshow(template1, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Patch')
#plt.subplot(224)
#plt.imshow(corr, cmap=plt.cm.gray)
#plt.axis('off')
#plt.title('Correlation')

plt.show()

