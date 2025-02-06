from pathlib import Path
import sys
import tkinter as tk

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from imgdisp import *


def callback_move_handler(x, y):
    print('Callback move', x, y)
def callback_press_handler(x, y):
    print('Callback press', x, y)

import sys
import matplotlib.pyplot as plt

root = tk.Tk()
root.withdraw()

if sys.argv[1] == 'draw':
    # Test drawing algorithms
    print('Drawing tests:')
    print('#1 - Line width 1')
    img = np.zeros((500,500))
    for angle in np.arange(0., 360., 10):
        draw_line(img, 250, 250,
                    250+200*np.cos(angle*np.pi/180),
                    250+200*np.sin(angle*np.pi/180), 1.)
    plt.figure(figsize=(12,12))
    plt.imshow(img, cmap=plt.get_cmap('Greys'))

    print('#2 - Line width 10')
    img = np.zeros((500,500))
    for angle in np.arange(0., 360., 10):
        draw_line(img, 250, 250,
                    250+200*np.cos(angle*np.pi/180),
                    250+200*np.sin(angle*np.pi/180), 1., 10)
    plt.figure(figsize=(12,12))
    plt.imshow(img, cmap=plt.get_cmap('Greys'))

    print('#3 - Circle width 1')
    img = np.zeros((500,500))
    for r in np.arange(3, 200, 30):
        draw_circle(img, 250, 250, r, 1.)
    plt.figure(figsize=(12,12))
    plt.imshow(img, cmap=plt.get_cmap('Greys'))

    print('#4 - Varying thickness 1-10')
    img = np.zeros((750,750))
    n = 0
    thickness = 1
    for r in np.arange(3, 300, 15):
        draw_circle(img, 375, 375, r, 1., thickness)
        thickness += 1
        if thickness > 10:
            thickness = 1

    plt.figure(figsize=(12,12))
    plt.imshow(img, cmap=plt.get_cmap('Greys'))
    plt.show()
    sys.exit(0)

grad1 = (np.tile(np.linspace(0,1,512),512).reshape((512,512))*
            np.linspace(0,1,512).reshape((512,1)))
grad2 = (np.tile(np.linspace(0,1,2048),1024).reshape((1024,2048))*
            np.linspace(0,1,1024).reshape((1024,1)))

if sys.argv[1] == 'img1':
    # Test ImageDisp - simple image
    print('Simple 512x512, two zoom, enlarge (5,2)')
    ImageDisp(grad1, canvas_size=(512,512), flip_y=False)
    ImageDisp(grad1, canvas_size=(512,512), flip_y=True)
    ImageDisp((grad2, grad2), canvas_size=(512,512), one_zoom=False,
                enlarge_limit=(5,2))
    tk.mainloop()

if sys.argv[1] == 'img2':
    # Two images with overlay, auto_update, enlarge and separate zooms
    # Flipped y
    print('1 - Overlay left 1, right 0.5')
    overlay1 = np.zeros((grad1.shape[0], grad1.shape[1], 3))
    overlay2 = np.zeros((grad1.shape[0], grad1.shape[1], 3))
    overlay1[100:300,200:400,0] = 1.
    overlay2[200:400,100:300,0] = 0.5
    ImageDisp((grad1, grad1), (overlay1, overlay2),
                canvas_size=(512,512), auto_update=True,
                enlarge_limit=(5,5), one_zoom=False)

    print('2 - Overlay transparency Red 1, Green 0.75, Yellow 0.5')
    print('3 - Same, separate contrast')
    # Two images with overlay and transparency, auto_update, enlarge and
    # separate zooms
    overlay1 = np.zeros((grad1.shape[0], grad1.shape[1], 4))
    overlay2 = np.zeros((grad1.shape[0], grad1.shape[1], 4))
    overlay1[100:300,200:400] = (1., 0, 0, 1.)
    overlay2[200:400,100:300] = (0., 0.5, 0., 0.75)

    draw_line(overlay1, 100, 400, 400, 450, (1.,1.,0.5,0.5), 10)
    draw_circle(overlay2, 400, 400, 100, (1.,1.,0.5,0.5), 15)

    imdisp = ImageDisp([grad1, grad1], [overlay1, overlay2],
                        canvas_size=(512,512), auto_update=True,
                        enlarge_limit=(5,5), one_zoom=False)
    imdisp = ImageDisp([grad1, grad1], [overlay1, overlay2],
                        canvas_size=(512,512), auto_update=True,
                        enlarge_limit=(5,5), one_zoom=False,
                        separate_contrast=True)
    tk.mainloop()

# Two images with overzoomed overlay, auto_update, enlarge and
# separate zooms
# overlay1 = np.zeros((iss_nac_obs1.data.shape[0]*3,
#                      iss_nac_obs1.data.shape[1]*3,
#                      3))
# overlay2 = np.zeros((iss_nac_obs1.data.shape[0],
#                      iss_nac_obs1.data.shape[1],
#                      3))
# overlay1[200*3:400*3:4,500*3:700*3:5,1] = 1.

# overlay2[200:400:4,500:700:5,0] = 1.

# imdisp = ImageDisp([iss_nac_obs1.data, iss_nac_obs1.data],
#                    [overlay1, overlay2],
#                    canvas_size=(512,512), auto_update=True,
#                    enlarge_limit=(5,5), one_zoom=False)
# tk.mainloop()


#    overlay = np.zeros((img1.shape[0], img1.shape[1], 3))
#    for i in range(1024):
#        overlay[i,i,0] = 1
#        overlay[i,1023-i,1] = 1
#    imdisp.Bind_mousemove(0, callback_move_handler)
#    imdisp.Bind_b1press(0, callback_press_handler)
#    imdisp.SetOverlay(0, overlay)
#    tk.mainloop()
