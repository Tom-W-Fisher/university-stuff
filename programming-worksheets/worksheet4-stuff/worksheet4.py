from graphics import *
import os

def personalGreeting():
    name = input("What's your name, traveller?\n")
    print(f"Hello {name}, nice to see you!")
    
def formalName():
    name = input("ENTER YOUR FIRST NAME\n")
    sname = input("ENTER YOUR SURNAME\n")
    print(f"{name[0]}. {sname}")
    
def kilos2Ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
    print(f"{kilos:.2f} kilos is equal to {ounces:.2f} ounces")
    
def generateEmail():
    name = input("ENTER YOUR FIRST NAME\n")
    sname = input("ENTER YOUR SURNAME\n")
    year = input("WHAT YEAR DID YOU ENTER THE UNIVERSITY?\n")
    email = f"{sname[:4]}.{name[0]}.{year[-2:]}@myport.ac.uk".lower()
    print(email)
    
def gradeTest():
    grade_string = "FFFFCCBBAAA"
    mark = int(input("ENTER TEST MARK\n"))
    print(f"GRADE ACHIEVED IS `{grade_string[mark]}`")
    
def graphicLetters():
    word = input("ENTER A WORD\n")
    win = GraphWin("WORD WRITER", 500, 500)
    message = Text(Point(250, 100), "CLICK ANYWHERE TO WRITE THE NEXT LETTER\
 OF THE WORD")
    message.draw(win)
    for letter in word:
        letter_pos = win.getMouse()
        graphic_letter = Text(letter_pos, letter)
        graphic_letter.setSize(30)
        graphic_letter.draw(win)
      
    message.setText("NOW CLICK TO CLOSE")
    win.getMouse()
    win.close()
    
def singASong():
    # a pretty crappy song
    word = input("ENTER A WORD\n")
    lines = int(input("ENTER THE NUMBER OF LINES\n"))
    words_per_line = int(input("HOW MANY TIMES SHOULD THE WORD APPEAR EACH LINE ?\n"))
    
    print(((word+" ")*words_per_line +"\n")*lines)
    
def exchangeTable():
    print("EUROS | POUNDS")
    print("--------------")
    for euro in range(0, 21):
        pound = euro / 1.17
        print(f"{euro:6}|{pound:6.2f}")

def makeInitialism():
    phrase = input("ENTER A MULTI-WORD PHRASE\n")
    phrase = phrase.upper().split()
    initialism = "".join([word[0] for word in phrase])
    print(initialism)
    
def nameToNumber():
    name = input("ENTER YOUR NAME\n")
    name = name.lower()
    value = sum([ord(letter)-96 for letter in name])
    print(f"THE VALUE OF YOUR NAME IS {value}. DISSAPOINTING.")
    
def fileInCaps():
    file_name = input("ENTER THE NAME OF A FILE\n")
    try:
        with open(file_name, "r") as file:
            print(file.read().upper())
    except FileNotFoundError:
        print("THAT FILE DOES NOT EXIST IN THIS DIRECTORY.")
        
def totalSpending():
    with open("random_numbers.txt", "r") as spending_file:
        total_spending = sum(map(
            lambda x: float(x), spending_file.read().strip().split("\n")))
        print(total_spending)