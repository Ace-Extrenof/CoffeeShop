from os import system, name
import time
# Coffe shop sike!!!!!!!!!!!!!!!
print("Welcome to the cafe")

characters = ["waiter: ", "you :", "shady figure :", "random gurl :"]

def Clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')


def Dialogue(sentence, interval, clear):
    print(sentence)
    time.sleep(interval)
    if clear == 1:
        Clear()
    else:
        pass

def Choice(choice1, choice2, response1, response2):
    print("1. " + choice1)
    print("2. " + choice2)

    ans = input("> ")
    if ans == 1:
        Dialogue(response1, 2, 0)
    elif ans == 2:
        Dialogue(response2, 2, 0)
    else:
         Dialogue(response2, 2, 0)

def Location(place):
    places = {1: "Coffee Shop",
              2: "Downtown Subway",
              3: "Convinience Store",
              4: "Warehouse",
              5: "Underground",
              6: "Laboratory",
              7: "Diable Room",
              8: "Future",
              9: "Past",
              10: "Before The Wakening",
              11: "Hyperspace",
              12: "Hivemind",
              13: "The Codebase",
              14: "The Prism"}

    List = list(places.values())
    if place in List:
        Clear()
        print(place)

def Act1():
    Clear()
    print("░▒▓ ACT I ▓▒░")
    time.sleep(5)
    Clear()
    Dialogue("You have come to a famous coffee shop (surprising)", 3, 0)
    Dialogue("You sit on the table nearest to you, it's begun raining outside...", 2, 0)
    Dialogue("Waiter: What would you like sir?", 2, 0)
    print("[Menu: Latte, Macchiato, Mocha, Espresso, Frappe]   (write first letter capital damnit)")
    order = input("> ")
    if order not in ["Latte", "Macchiato", "Mocha", "Espresso"]:
        print("{characters[0]} Thats not in the menu sir")
        input("> ")
    else:
        print("One ", order, " coming right up!")
        time.sleep(2)

    Dialogue("A man suited in black sits next to you, his face is covered by a strange mask...", 2, 1)
    Dialogue("He looks ouside the window and then turns towards you \nShady Figure: Good weather innit?", 2, 0)
    Choice("I like the rain...", " I'm not fond of the rain...", "Shady Figure: Something just feels right about it... right?", "Shady Figure: Now now... Don't be like that, enjoy the rain...")

Act1()
