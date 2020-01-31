from pdf2image import *
import pytesseract
from gtts import gTTS
import sys
import os
from PyPDF2 import PdfFileReader
path= str(sys.argv[1:])[2:-2]
pdf = PdfFileReader(open(path,'rb'))
pages = pdf.getNumPages()
lan = 'en'
inp=path[path.rfind('/')+1:path.rfind('.')]
os.mkdir(inp)
for i in range(1, pages+1):
	image = convert_from_path(path, first_page=i, last_page=i)
	print("Converting page: "+ str(i) + "/" + str(pages));
	say = pytesseract.image_to_string(image[0]);
	try:
		obj = gTTS(text=say, lang=lan, slow=False)
	except:
		continue	
	obj.save( inp + "/Page" + str(i) + ".mp3")
print("Conversion of " + path + " Complete")
