# i/p-->.txt file,# o/p-->.mp3 file

# to translate text to speech
from gtts import gTTS
# to save and play the coverted audio file
import os
# open the text file in read mode by specifying the file path
op=open('F:/projects/Venkata.txt','r')
#\n used to continue the flow of speech when reading the next line,when there are any unintended white spaces
txt=op.read().replace("\n","")
# language=english and tld-->accent=Indian
language = 'en'
kvr = gTTS(text=txt, lang=language,tld='co.in',slow=False)
# save and play the converted .mp3 file
kvr.save("Success.mp3")
os.system("Success.mp3")

# https://www.youtube.com/watch?v=hRmJ7GFNFW8
# https://www.geeksforgeeks.org/text-to-speech-changing-voice-in-python/
# https://www.youtube.com/watch?v=_Q8wtPCyMdo
# https://www.geeksforgeeks.org/convert-text-speech-python/
# https://gtts.readthedocs.io/en/latest/module.html#localized-accents
