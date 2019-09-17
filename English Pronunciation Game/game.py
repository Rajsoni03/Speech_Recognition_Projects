import pyaudio
import speech_recognition as sr
import pyttsx3
from time import sleep

r = sr.Recognizer()
engine = pyttsx3.init()
total,right,wrong,miss = 0,0,0,0

f = open("text_data/sentence.txt", "r")
string = str(f.read()).lower().replace('\n','').split('.')

for i in string:
    print('Read: '+i)
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text = str(text).lower()
            print('You:  '+text)
            if i == text:
                print('>>Very Good', end='\n\n')
                engine.say('Very Good')
                right+=1
            else:
                print('>>Not Mached', end='\n\n')
                engine.say('Not Mached')
                wrong+=1
            engine.runAndWait()
        except:
            print('>>You Miss',end='\n\n')
            engine.say('You Miss')
            engine.runAndWait()
            miss+=1
        sleep(5)
    total+=1
f.close()
print('Total = ',total,'\nRight = ',right,'\nWrong = ',wrong,'\nMiss = ',miss)