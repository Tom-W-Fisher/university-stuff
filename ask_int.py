def ask_int(ask_string: str ="Please enter an integer.\n",
            response_string: str ="That is not an integer.") -> int:
    num = input(ask_string)
    try:
        num = int(num)
    except ValueError:
        print(response_string)
        num = ask_int(ask_string, response_string)
        
    return num

