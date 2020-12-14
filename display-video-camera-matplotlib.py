import numpy as np
import cv2
from matplotlib import pyplot as plt

def grab_frame(cap, mode='rgb'):
    ret, frame = cap.read()

    if mode == 'gray':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

cap = cv2.VideoCapture(0)

ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

im1 = ax1.imshow(grab_frame(cap, 'gray'))
im2 = ax2.imshow(grab_frame(cap))

plt.ion()
while True:
    im1.set_data(grab_frame(cap, 'gray'))
    im2.set_data(grab_frame(cap))
    plt.pause(0.1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
p.ioff()
plt.show()
