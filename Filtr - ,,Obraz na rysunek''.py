def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255          
    result[back==255]=255
    return result.astype('uint8')

import numpy as np
def grayscale(rgb):   #skala szarości
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

#wczytywanie obrazu
#img = 'JP2.jpg' #z dysku
img ="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" #z internetu

import imageio
s = imageio.imread(img)
g=grayscale(s)  #zastosowanie skali szarości i zmiana obrazu na czarno biały
i = 255-g   #odwracanie obrazu
import scipy.ndimage
b = scipy.ndimage.filters.gaussian_filter(i,sigma=20)  #rozmycie obrazu za sprawą filtra gaussowskiego
r= dodge(b,g) #dodawanie i łączenie
 
import matplotlib.pyplot as plt
plt.imshow(r, cmap="gray")
plt.imsave('rysunek.png', r, cmap='gray', vmin=0, vmax=255) #zapisywanie

