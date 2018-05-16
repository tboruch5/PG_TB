name = "Teo Boruchin"

subjects = ["English", "Spanish", "Science", "Math", "Fortnite"]

print("Hello " + name)

for i in subjects:
    print("One of my classes is " + i)


characters = ["The Flash", "Kid Flash", "Cisco", "Killer Frost", "Joe West", "Iris West", "The Thinker"]

for i in characters:
    if i == "The Flash":
        print(i + " is the fastest man alive!")
    elif i == "The Thinker":
        print(i + " is smart and an evil genius.")
    else:
        print("One of the best characters is " + i)


tv_shows = []

while True:
    print("What's a tv show you like? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        tv_shows.append(answer)

for i in tv_shows:
    print("One of your favorite tv shows is " + i)
