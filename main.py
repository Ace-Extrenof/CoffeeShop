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

def Act1():
    Clear()
    print("ACT 1")
    time.sleep(5)
    Clear()
    Dialogue("You have come to a famous coffee shop (surprising)", 3, 0)
    Dialogue("You sit on the table nearest to you, it's begun raining outside...", 2, 0)
    Dialogue("{characters[0]} What would you like sir?", 2, 0)
