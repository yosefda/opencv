import numpy
import cv2
from matplotlib import pyplot

img = cv2.imread('sydney-opera-house.jpg')

# b,g,r = cv2.split(img)
# img = cv2.merge([r,g,b])
# pyplot.imshow(img)

# pyplot.imshow(img[:,:,::-1])

pyplot.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
