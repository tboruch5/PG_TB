import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hello Teo how can I help you!")
    print("Listening...")
    audio = r.listen(source)
    print("thinking...")


try:
    words = r.recognize_google(audio)
    speak.Speak("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    wb.open("https://www.google.com/search?q=" + words)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
