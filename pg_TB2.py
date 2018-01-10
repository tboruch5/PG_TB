import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.25)
pg.hotkey('winleft','up')
pg.typewrite('amazon.com\n',.25)

time.sleep(4)

pg.hotkey('tab')
time.sleep(0.2)
pg.hotkey('tab')
time.sleep(0.2)
pg.hotkey('tab')
time.sleep(0.2)
pg.hotkey('tab')
time.sleep(0.2)
pg.hotkey('tab')
time.sleep(0.2)


pg.typewrite('chicken in a can\n',.25)
time.sleep(2)
pg.hotkey('space')
time.sleep(2)
pg.click(667, 408)
