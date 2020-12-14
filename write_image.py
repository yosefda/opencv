import numpy as np 
import cv2

img = cv2.imread('me-card.png', 0)
cv2.namedWindow('source-image', cv2.WINDOW_NORMAL)
cv2.imshow('source-image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('me-card-gray.png', img)
    cv2.destroyAllWindows()