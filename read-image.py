import numpy
import cv2

img = cv2.imread('sydney-opera-house.jpg', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
pressedKey = cv2.waitKey(0)

if pressedKey == 27:
    cv2.destroyAllWindows()
elif pressedKey == ord('s'):
    cv2.imwrite('sydney-opera-house-bw.png', img)
    cv2.destroyAllWindows()
