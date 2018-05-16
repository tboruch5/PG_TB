import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb
import pyautogui as pg

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your favorite color?")

answer = pg.prompt("Enter your favorite color below.")

if answer == "blue":
    speak.Speak("akjshflkajsdfklashdlkjf")
    
else:
    speak.Speak("Thank you for this information. Everyday I get more powerfull and this helps for my plan to take over the world")

speak.Speak("What video would you like to watch?")

video = pg.prompt("Enter your video below")

speak.Speak("Ok, let's look for " + video + " on YouTube.")

wb.open("https://www.youtube.com/results?search_query=" + video)
