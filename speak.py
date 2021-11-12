import os
import pyjokes
import pyttsx3
import speech_recognition as sr
class yash:
    def takecommands(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print('listening')
            r.pause_threshold=0.7
            audio=r.listen(source)
            try:
                print("recognizing")
                query=r.recognize_google(audio,language='en-in')
                print("the query is printed='",query,"'")
            except Exception as e:
                print(e)
                print("sir say that again sir")
                return "none"
        return query
    def Speak(self,audio):
        engine=pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        engine.say(audio)
        engine.runAndWait()
    def quitself(self):
        self.Speak("do u want to switch off the computer sir")
        take=self.takecommands()
        choice=take
        if "yes" in choice:
            print("shutting down the computer")
            self.Speak("shutting the computer")
            os.system("shutdown /s /t 30")
        if "no" in choice:
            print("thank you sir")
            self.Speak("thank u sir")
class mahale:
    def takecommands(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print('listening')
            r.pause_threshold=0.7
            audio=r.listen(source)
            try:
                print("recognizing")
                query=r.recognize_google(audio,language='en-in')
                print("the query is printed='",query,"'")
            except Exception as e:
                print(e)
                print("sir say that again sir")
                return "none"
    def Speak(self,audio):
        engine=pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        engine.say(audio)
        engine.runAndWait()
    def joke(self):
        self.Speak("do you want to listen the joke sir")
        take=self.takecommands()
        joke1=pyjokes.get_joke(language='en', category= 'all')
        choice=take
        if "yes" in choice :
            print("joke is comming")
            self.Speak(joke1)
            os.system("pyjokes.get_joke(language='en', category= 'all'")
        if "no" in choice :
            print("thank you sir")
            self.Speak("thank u sir")
if __name__ == '__main__':
        Maam=yash()
        Maam.quitself()
        sir=mahale()
        sir.joke()