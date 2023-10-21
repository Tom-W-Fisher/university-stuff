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
    with open("spending.txt", "r") as spending_file:
        total_spending = sum(map(
            lambda x: float(x), spending_file.read().strip().split("\n")))
        print(total_spending)
        
def rainfallChart():
    with open("rainfall.txt", "r") as rainfall_file:
        city_rainfalls = rainfall_file.read()[:-1].split("\n")
        # readlines, as a result of some strange design choice, returns each
        # line with a closing newline (\n) escape sequence.
        # so .read().split("\n") is used instead.
        
    for city in city_rainfalls:
        city = city.split()
        city[1] = int(city[1]) * "*"
        city = f"{city[0]:<12} {city[1]}"
        print(city)
            
def graphicalRainfallChart():
    with open("rainfall.txt", "r") as rainfall_file:
        city_rainfalls = rainfall_file.read()[:-1].split("\n")
        # `readlines`, as a result of some strange design choice, returns each
        # line with a closing newline (\n) escape sequence.
        # so `.read().split("\n")` is used instead.
    
    longest_city = 0
    highest_rainfall = 0
    city_count = 0
    for i, city in enumerate(city_rainfalls):
        city_count += 1
        city = city.split()
        if len(city[0]) > longest_city:
            longest_city = len(city[0])
        city[1] = int(city[1])
        if city[1] > highest_rainfall:
            highest_rainfall = city[1]
        city_rainfalls[i] = city
        
    width_per_mm = 10
    x_buffer = 20
    y_buffer = 10
    y_bar_buffer = 10
    y_bar_size = 30
    bar_text_gap = 10
    win = GraphWin("UK Cities Rainfall Bar Chart",
                   2*x_buffer + highest_rainfall*width_per_mm + longest_city*10 + bar_text_gap,
                   2*y_buffer + (y_bar_buffer+y_bar_size)*city_count - y_bar_buffer)
    
    for i, city in enumerate(city_rainfalls):
        city_name = left_align_text(
            Point(x_buffer, y_buffer + y_bar_size/2 +(y_bar_buffer+y_bar_size)*i + 5),
             city[0])
        city_name.setFace("courier")
        city_name.draw(win)
        
        rain_rectangle = Rectangle(
            Point(x_buffer + longest_city * 10 + bar_text_gap,
                  y_buffer + i*(y_bar_buffer+y_bar_size)),
            Point(x_buffer + longest_city * 10 + width_per_mm * city[1] + bar_text_gap,
                  y_buffer + i*(y_bar_buffer+y_bar_size) + y_bar_size))
        
        rain_rectangle.setFill("blue")
        rain_rectangle.draw(win)
        
def left_align_text(left_edge: Point, text: str) -> Text:
    return Text(Point(left_edge.x + len(text)*5, left_edge.y), text)
    # 5 is the magic number i think
            
               
def rainfallInInches():
    with open("rainfall.txt", "r+") as rainfall_file:
        rainfall_values = rainfall_file.read()[:-1].split("\n")
        
    for i, city in enumerate(rainfall_values):
        city = city.split()
        city[1] = int(city[1]) / 25.4
        city = f"{city[0]} {city[1]:.2f}"
        rainfall_values[i] = city
        
    rainfall_values = "\n".join(rainfall_values)
    with open("rainfall-inches.txt", "w") as rainfall_file:
        rainfall_file.write(rainfall_values)
        
def wc(file_name):
    try:
        with open(file_name, "r") as file:
            all_text = file.read()
            char_count = len(all_text)
            line_count = len(all_text.split("\n"))
            word_count = len(all_text.split())
            print(f"Newlines:{line_count}\nWords:{word_count}\nCharacters:{char_count}")
    except FileNotFoundError:
        print(f"wc: no such file: {file_name}")
        
def cd(new_dir):
    try:
        os.chdir(new_dir)
    except FileNotFoundError:
        print(f"cd: no such directory: {new_dir}")
        
def cat(file_name):
    try:
        with open(file_name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"cat: no such file: {file_name}")
        
def ls(path=None):
    if path:
        try:
            print("\n".join(os.listdir(path)))
        except FileNotFoundError:
            print(f"ls: No such directory: {path}")
    else:
        print("\n".join(os.listdir()))
        
def terminal_help(command=None):
    if command:
        match command:
            case "ls":
                print("`ls` lists the items in a directory. \
If no argument is given, it prints the contents of the current directory. If it \
is given the path of a directory, it will print out the contents of that directory \
instead.")
            case "pwd":
                print("Prints the path of the current directory. \
(Present Working Directory)")
            case "cd":
                print("Changes the current directory. Takes one argument: \
directory to be changed to. This directory must be a subdirectory of the current \
directory, or the path to the directory (either from root or the current directory \
must be specified. \n Type 'cd ..' to move to the parent of the current directory. \
('cd' stands for 'Change Directory')")
            case "cat":
                print("Prints the contents of a file. Takes one argument: the \
name of the file to be printed. If the file is not in the current directory, \
the path to the file (from current file or from root file) must be specified.")
            case "help":
                print("Can be used without an argument for general help. Can be used \
with 1 argument, the name of a command, for more information on the command.")
            case "wc":
                print("Prints the number of newlines, the number of words, and \
the number of characters in a file. (wc stands for word count). Takes one argument: \
the file to use.")
            case _:
                print("Command not recognised. Printing default help:")
                terminal_help()
    else:
        print("Available commands are:\n- ls\n- pwd\n- cd\n- cat\n- help\n- wc \
\nUse 'help' followed by the name of a command for more information. \
Type CTRL-C to exit.")

def terminal_emulator():
    print("Welcome to a very barebones terminal. Type 'help' for help, and CTRL-C to leave.")
    command_dict = {"ls": ls,
                    "pwd": lambda: print(os.getcwd()),
                    "cd": lambda new_dir: cd(new_dir),
                    "cat": lambda file_name: cat(file_name),
                    "help": terminal_help,
                    "wc": lambda file_name: wc(file_name)}
    while True:
        path = os.getcwd()
        path = "/".join([word[0] for word in path.split("/")[1:]]) + path.split("/")[-1][1:]
        try:
            user_input = input(f"{path} $").split()
        except KeyboardInterrupt:
            print("\nExiting terminal.")
            break
        
        if len(user_input) == 0:
            continue
        elif len(user_input) > 2:
            print("Invalid input: more than 2 items detected.")
            continue
        command = user_input[0]
        if command in command_dict:
            if len(user_input) == 1:
                try:
                    command_dict[command]()
                except TypeError:
                    print("That command needs an argument.")
            else:
                try:
                    command_dict[command](user_input[1])
                except TypeError:
                    print("That command doesn't take an argument.")
        else:
            print("Command not recognised. Type 'help' for a list of available commands.")