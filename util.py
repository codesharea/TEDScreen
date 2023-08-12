import matplotlib
import matplotlib.pyplot as plt
import cv2
import numpy as np

classes = ['Normal TED', 'Mild TED', 'Severe TED']
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", [(0,'black'), (0.06,'blue'), 
                                                                  (0.23, '#2ab6c6'), (0.38,'yellow'), 
                                                               (0.6,'red'), (1,'white')])
def resize(img, size=(256,256)):
    imgs_scaled = []
    imgs_scaled.append(cv2.resize(img, size))
    return imgs_scaled

def to_3dimg(imgs, cm=None):
    imgs3d = []
    for img in imgs:
        img = cm((img/255.))
        colored_image = (img[:, :, :3])
        imgs3d.append(colored_image)
    return np.array(imgs3d)