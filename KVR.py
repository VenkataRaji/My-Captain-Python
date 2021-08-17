# import pyttsx3
from gtts import gTTS
import os

# if the file is in PDF format
import PyPDF2
# pdf=open('C:/Users/R.R.10.02.21/Downloads/Venkata.pdf','rb')
# read=PyPDF2.PdfFileReader(pdf)
# pg=read.getPage(0)
# txt=pg.extractText()

# using gTTS directly
op=open('C:/Users/R.R.10.02.21/Downloads/Venkata.txt','r')
txt=op.read().replace("\n"," ")
language = 'en'
kvr = gTTS(text=txt, lang=language,tld='co.in',slow=False)
kvr.save("Success.mp3")
os.system("Success.mp3")

# using pysstx
# spkr=pyttsx3.init()
# spkr.say(txt)
# spkr.runAndWait()
