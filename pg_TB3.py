import pyautogui as pg
import time
import webbrowser

points = 0


# Question
answer = pg.prompt(
"""
Where would you land first in Fortnite?

a) Tomato Town
b) Dusty Depot
c) Fatal Fields
d) Tilted Towers
e) Pleasant Park
f) Salty Springs
"""
    )

# Answer
pg.alert("You chose " + answer)


if answer == "a" or answer == "A":
    points += 1
elif answer == "b" or answer == "B":
    points += 5
elif answer == "c" or answer == "C":
    points += 10
elif answer == "d" or answer == "D":
    points += 15
elif answer == "e" or answer == "E":
    points += 20
elif answer == "f" or answer == "F":
    points += 25

# Question
answer = pg.prompt(
"""
Whats your favorite weapon?

a) RPG/Grenade Launcher
b) Sniper
c) Assault Rifle
d) Tactical shotgun
e) Pistol
f) Pump Shotgun

"""
    )

# Answer
pg.alert("You chose " + answer)


if answer == "e" or answer == "E":
    points += 1
elif answer == "f" or answer == "F":
    points += 5
elif answer == "c" or answer == "C":
    points += 10
elif answer == "d" or answer == "D":
    points += 15
elif answer == "a" or answer == "A":
    points += 20
elif answer == "b" or answer == "B":
    points += 25

# Question
answer = pg.prompt(
"""
What is your average place?

a) 80-100
b) 50-79
c) 30-49
d) 10-29
e) 2-9
f) Victory Royale

"""
    )

# Answer
pg.alert("You chose " + answer)


if answer == "a" or answer == "A":
    points += 1
elif answer == "b" or answer == "B":
    points += 5
elif answer == "c" or answer == "C":
    points += 10
elif answer == "d" or answer == "D":
    points += 15
elif answer == "e" or answer == "E":
    points += 20
elif answer == "f" or answer == "F":
    points += 25

# Question
answer = pg.prompt(
"""
What is your best Emote?

a) What is that?
b) Original Dance
c) Wave
d) Flex
e) Worm
f) Electro Shuffle

"""
    )

# Answer
pg.alert("You chose " + answer)


if answer == "a" or answer == "A":
    points = -250
elif answer == "b" or answer == "B":
    points += 5
elif answer == "c" or answer == "C":
    points += 10
elif answer == "d" or answer == "D":
    points += 15
elif answer == "e" or answer == "E":
    points += 20
elif answer == "f" or answer == "F":
    points += 25

# END OF SURVEY
pg.alert("Your character is.....")

if points < 4:
    pg.alert("You are a noob")
    webbrowser.open("https://www.google.com/search?q=tide+pods&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwin0PeFovHYAhWCl-AKHZc4DxYQ_AUICygC&biw=1366&bih=637#imgrc=CTrRDjlPFIL0-M:")
if points > 5 and points < 50:
    pg. alert("You are decent")
elif points >= 50:
    pg.alert("YOU ARE THE GOAT")

