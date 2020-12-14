import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def grab_frame(cap, mode='rgb'):
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if mode == 'gray':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if mode == 'flip':
        return cv2.flip(rgb_frame, 0)

    return rgb_frame

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1280,720))

ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)

im1 = ax1.imshow(grab_frame(cap, 'gray'))
im2 = ax2.imshow(grab_frame(cap))

flipped_frame = grab_frame(cap, 'flip')
im3 = ax3.imshow(flipped_frame)
out.write(flipped_frame)

def update(i):
    im1.set_data(grab_frame(cap, 'gray'))
    im2.set_data(grab_frame(cap))

    flipped_frame = grab_frame(cap, 'flip')
    im3.set_data(flipped_frame)
    out.write(flipped_frame)


ani = FuncAnimation(plt.gcf(), update, interval=200)

def close(event):
    if event.key == 'q':
        plt.close(event.canvas.figure)

cid = plt.gcf().canvas.mpl_connect("key_press_event", close)

plt.show()

cap.release()
out.release()