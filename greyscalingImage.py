'''
Created on Sep 1, 2021
@author: Nasir Khurshid
All right reserved.
'''
import pprint as p              #imported pprint for pretty output

def validate(val):              #function for validating values
    for x in range(len(val)):
        if val[x] > 255:
            val[x] = 255
        elif val[x] < 0:
            val[x] = 0

def func(pxl):                  #function for greyscaling each pixel
    pl = len(pxl)               #getting size of pixel
    if pl > 0 and pl < 4:       
        if pl == 1:            #greyscaling each pixel by using if conditions 
            validate(pxl[0])
            entry = int(sum(pxl[0])/3)
            pxl[0] = [entry, entry, entry]
        elif pl == 2:
            validate(pxl[0])
            entry = int(sum(pxl[0])/3)
            pxl[0] = [entry, entry, entry]
            validate(pxl[1])
            entry = int(sum(pxl[1])/3)
            pxl[1] = [entry, entry, entry]            
        else:
            validate(pxl[0])
            entry = int(sum(pxl[0])/3)
            pxl[0] = [entry, entry, entry]
            validate(pxl[1])
            entry = int(sum(pxl[1])/3)
            pxl[1] = [entry, entry, entry]
            validate(pxl[2])
            entry = int(sum(pxl[2])/3)
            pxl[2] = [entry, entry, entry]
    else:
        print("Invalid syntax for pixel 1!")

def greyscale(img):         #basic function for greyscaling
    imgpxl = len(img)       #getting size of image in pixels
    if imgpxl > 0 and imgpxl < 4:
        if imgpxl == 1:     #changing each pixel to grey by using func()
            pxl1 = img[0]
            pxl1 = func(pxl1)
        elif imgpxl == 2:
            pxl1 = img[0]
            func(pxl1)
            pxl2 = img[1]
            func(pxl2)
        else:
            pxl1 = img[0]
            func(pxl1)
            pxl2 = img[1]
            func(pxl2)
            pxl3 = img[2]
            func(pxl3)
    else:
        print("Image has zero or invalid pixels!")
    return img


#img = [[[1,2,3], [3,5,1], [8,3,1]],[[1,2,3], [3,5,1], [8,3,1]],[[1,2,3], [3,5,1], [8,3,1]]]

img = [
  [[0, 0, 258], [0, 0, 157]],
  [[1, 100, 0], [0, 10, 0]]
]

#img1 = [2,-1, 333]
#validate(img1)

print("Printing Old Image: ")
p.pprint(img)

gray = greyscale(img)

print("Printing New Image: ")
p.pprint(gray)