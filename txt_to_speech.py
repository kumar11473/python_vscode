from gtts import gtts
import os

myText="text to speech conversion using python"

language= 'en'

output=gTTs(text=myText,lang=language,slow=false)

output.save("output.mp3")
os.system("start output.mp3")   