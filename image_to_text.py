#install the library called as pytesseract which extracts text from images. It is an OCR Engine
#pip install pytesseract
import pytesseract
from PIL import Image
image = Image.open('image.jpg')  # Replace 'image.jpg' with the path to your image file
text = pytesseract.image_to_string(image)
text = pytesseract.image_to_string(image, lang='eng')  # Specify the language as English


print(text)
#you will be able to see text extracted from images