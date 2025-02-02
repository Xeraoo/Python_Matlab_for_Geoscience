from spectral import *
import spectral.io.envi as envi
import spectral.io.erdas as erdas

img = open_image('92AV3C.lan')
print(img.__class__)
print(img.shape)
print(img) 
pixel = img[50,100]
print(pixel.shape)
band6 = img[:,:,5]
print(band6.shape)
arr = img.load()

print(arr.__class__)
print(arr.info())
print(arr.shape)

img = open_image('92AV3C.lan')
img.bands = aviris.read_aviris_bands('92AV3C.spc')
img = erdas.open('92AV3C.lan')
print(img)
from spectral import *
view = imshow(img, (29, 19, 9))
