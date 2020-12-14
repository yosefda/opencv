import numpy as np 
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('me-card.png')
plt.subplot(121)
plt.xticks([])
plt.yticks([])
plt.imshow(img)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.subplot(122)
plt.xticks([])
plt.yticks([])
plt.imshow(img2)

plt.show()