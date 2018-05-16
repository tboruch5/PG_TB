import pyautogui as pg
import webbrowser
import time
#make sure you log into gmail first
webbrowser.open("https://google.com")
time.sleep(2)
pg.typewrite("Where and when is there live music in new york", 0.1)
pg.hotkey('enter')
