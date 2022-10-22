import pyttsx3

# import win32api
text_speech = pyttsx3.init() 

voices = text_speech.getProperty('voices')
 

text_speech.setProperty('voice', voices[1].id)
while True:  
 answer = input("Enter text want to convert to speech : ")
 text_speech.setProperty('rate',120)
 text_speech.say(answer)

 text_speech.runAndWait()

