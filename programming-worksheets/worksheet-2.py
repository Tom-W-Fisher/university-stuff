import math

def speedCalculator():
    distance = int(input("Please input the number of kilometers travelled (\
must be integer and not include any letters):\n"))
    duration = int(input("Please input the duration of the journey in hours (\
must be integer and not include any letters):\n"))
    speed = distance / duration
    print("Average speed was " + str(round(speed, 2)) + "kmh. (2 d.p.)")
   
def circumferenceOfCircle():
    radius = float(input("Please input the radius of the circle (\
must not include any letters):\n"))
    circumference = 2 * radius * math.pi
    print("The circumference is " + str(round(circumference, 2)) + " (2 d.p.)")
   
def areaOfCircle():
    radius = float(input("Please input the radius of the circle (\
must not include any letters):\n"))
    area = radius ** 2 * math.pi
    print("The area is " + str(round(area, 2)) + " (2 d.p.)")
   
def costOfPizza():
    radius = float(input("Please input the radius of the pizza in cm (\
must not include any letters):\n"))
    area = radius ** 2 * math.pi
    cost = area / 3.5 / 100 # Cost in £. 3.5p per cm^2 of pizza
    print("The cost is £" + str(round(cost, 2)))

def slopeOfLine():
    x1 = float(input("What is the value of x1?\n"))
    y1 = float(input("What is the value of y1?\n"))
    x2 = float(input("What is the value of x2?\n"))
    y2 = float(input("What is the value of y2?\n"))
   
    dy = y2 - y1
    dx = x2 - x1
    grad = dy/dx # gradient, assuming straight line
   
    print("The slope is " + str(round(grad, 2)) + " (2 d.p.)")
   
def distanceBetweenPoints():
    x1 = float(input("What is the value of x1?\n"))
    y1 = float(input("What is the value of y1?\n"))
    x2 = float(input("What is the value of x2?\n"))
    y2 = float(input("What is the value of y2?\n"))
   
    dy = y2 - y1
    dx = x2 - x1
    distance = math.sqrt(dy**2 + dx**2)
   
    print("The distance is " + str(round(distance, 2)) + " (2 d.p.)")
   
def travelStatistics():
    speed = float(input("Please input the speed in kmh (\
must not include any letters):\n"))
    duration = float(input("Please input the duration of the journey in hours (\
must not include any letters):\n"))
    distance = speed * duration
    print("Distance travelled was " + str(round(distance, 2)) + "km. (2 d.p.)")
    fuel = distance / 5
    print("Fuel used was " + str(round(fuel, 2)) + " litres. (2 d.p.)")
 
def sumOfSquares():
    n = int(input("Please input an integer n\n"))
    total = 0
    for i in range(n+1):
        total += i ** 2
    print("Sum of squares of 1:" + str(n) + " is " + str(total))
 
def CoolerSumOfSquares():
    n = int(input("Please input an integer n:\n"))
    total = sum([i**2 for i in range(n+1)])
    print("Sum of squares of 1:" + str(n) + " is " + str(total))
   
def averageOfNumbers():
    total = 0
    n = int(input("How many numbers do you want to average?\n"))
    for i in range(n):
        total += int(input("Please enter number " + str(i+1) +":\n"))
       
    avg = total / n
    print("Average is: " + str(round(avg, 2)) + " (2 d.p.)")
   
def fibonacci():
    n = int(input("Please input an integer n:\n"))
    prev = 1
    current = 1
    next = 1
    for i in range(2, n):
        next = current + prev
        prev = current
        current = next
       
    print("Fibonacci number " + str(n) + " is " + str(next))
   
def cooler_fibonacci(n: int) -> int:
    """Recursively calculates the nth fibonacci number."""
    if n < 1:
        raise ValueError("Can't calculate fibonacci number of a negative.")
    elif n == 1 or n == 2:
        return 1
    else:
        return cooler_fibonacci(n-2) + cooler_fibonacci(n-1)
   
def selectCoins():
    money = int(input("Please enter amount of money in pence. \n\
(will be rounded down to nearest whole number, do not include the \"p\".):\n"))
    
    two_pounds = money // 200
    money %= 200
    one_pounds = money // 100
    money %= 100
    fifty_pences = money // 50
    money %= 50
    twenty_pences = money // 20
    money %= 20
    ten_pences = money // 10
    money %= 10
    five_pences = money // 5
    money %= 5
    two_pences = money // 2
    money %= 2
    
    
    print(
    str(two_pounds) + " × £2, " +
    str(one_pounds) + " × £1, " +
    str(fifty_pences) + " × 50p, " +
    str(twenty_pences) + " × 20p, " +
    str(ten_pences) + " × 10p, " +
    str(five_pences) + " × 5p, " +
    str(two_pences) + " × 2p, " +
    str(money) + " × 1p"
    )

def selectCoins2():
    # Coins is 2d array. Each inner array represents 1 coin.
    # Each inner array has 2 elements, in order: Coin name and Coin
    # ... value in pence
    coins = [
        ["£2", 200],
        ["£1", 100],
        ["50p", 50],
        ["20p", 20],
        ["10p", 10],
        ["5p", 5],
        ["2p", 2],
        ["1p", 1]]
    coin_count = [0]*len(coins)
    
    money = int(input("Please enter amount of money in pence. \n\
(will be rounded down to nearest whole number, do not include the \"p\".):\n"))

    out_str = ""
    for coin in coins:
        out_str += str(money // coin[1]) + "×" + coin[0] + ", "
        money %= coin[1]
        
    print(out_str)
        