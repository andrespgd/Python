from gtts import gTTS
from playsound import playsound
import os

tts = gTTS(text='hi buddy .. what is your question', lang='en', slow=True)
fname1 = "hello1.mp3"
tts.save(fname1)
playsound(fname1)
os.remove(fname1)

tts = gTTS(text='my name is mrs robot', lang='en', slow=True)
fname2 = "hello2.mp3"
tts.save(fname2)
playsound(fname2)
os.remove(fname2)
