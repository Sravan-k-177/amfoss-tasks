import pytesseract #for photo to txt

import re #for string to arthemetic

from PIL import Image

image = Image.open('/home/kota-sravan/Pictures/4x5.png') 

text = pytesseract.image_to_string(image)

text = text.strip() #to remove any leading or trailing white spaces

text = re.split(r'([-+/x])', text) #splits on any of these arthematic functions

def calculation(text):  #perform the calculation
    if text[1] == '+':
        result = float(text[0]) + float(text[2])
    elif text[1] == '-':
        result = float(text[0]) - float(text[2])
    elif text[1] == '/':
        result = float(text[0])/float(text[2])
    elif text[1].lower() == 'x':
        result = float(text[0]) * float(text[2])
    else:
        result = None
    return result

print(calculation(text))

