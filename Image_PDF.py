##Image to PDF converter using python

from PIL import Image
# Please replace image location with the path of file for example:- C:\Users\Dell\Desktop\GENERAL TOOLS\C langauage\python\apple.png
image1 = Image.open(r"Image location ")
im1=image1.convert('RGB')
im1.save(r"Location to save pdf file")
# Please replace "location to save pdf by the location where u wanna save file for example:- C:\Users\Dell\Desktop\GENERAL TOOLS\C langauage\python\1450330231-04db904008-banana1.pdf"

"""
Explanation:-
This code will take any type of image as input and will convert it to pdf:-
1. We will be using PIL library which can also be said as subset of Pillow library.
2. Secondly we will be using a pre build function of PIL library which is named as "Image" it take image as argument to read it.
3. We need to put a "r" before the image because we need to open it in read mode.
4. Next we will create a variable to store the converted(im1 here) we will be using convert function here which will convert it to needful.
4. We will be calling save function to save the image in desierd location given by the uer.
4. Important :-
   #Please give extension in both file location for ex:- image.png in input location
"""
#Thanks for viewing contributed by:- Hemang Jiwnani
