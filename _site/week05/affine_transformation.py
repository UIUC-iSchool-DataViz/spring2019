# put in the same directory as your ipynb file

import math
import PIL.Image as Image

# we won't go through this in detail
def ScaleRotateTranslate(image, angle, center = None, new_center = None, scale = None,expand=False):
    if center is None:
        return image.rotate(angle)
    angle = -angle/180.0*math.pi
    nx,ny = x,y = center
    sx=sy=1.0
    if new_center:
        (nx,ny) = new_center
    if scale:
        (sx,sy) = scale
    cosine = math.cos(angle)
    sine = math.sin(angle)
    a = cosine/sx
    b = sine/sx
    c = x-nx*a-ny*b
    d = -sine/sy
    e = cosine/sy
    f = y-nx*d-ny*e
    return image.transform(image.size, Image.AFFINE, (a,b,c,d,e,f), resample=Image.BICUBIC)
