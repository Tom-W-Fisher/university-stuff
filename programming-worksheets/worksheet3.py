from graphics import *


def helloGraphics():
    win = GraphWin()
    message = Text(Point(100, 100), "Hello graphics!")
    message.draw(win)
    win.getMouse()


def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(70, 90), Point(130, 90))
    arms.draw(win)
    left_leg = Line(Point(70, 160), Point(100, 120))
    right_leg = Line(Point(130, 160), Point(100, 120))
    left_leg.draw(win)
    right_leg.draw(win)


def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100, 100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")

def drawCircle():
    radius = float(input("Please enter the radius of the circle: \n"))
    win = GraphWin("Circle", radius * 3, radius * 3)
    circle = Circle(Point(radius * 1.5, radius * 1.5), radius)
    circle.draw(win)
    
def drawArcheryTarget():
    win = GraphWin("Target", 300, 300)
    
    inner_circle = Circle(Point(150, 150), 40)
    inner_circle.setFill("yellow")
    middle_circle = Circle(Point(150, 150), 80)
    middle_circle.setFill("red")
    outer_circle = Circle(Point(150, 150), 120)
    outer_circle.setFill("blue")
    
    outer_circle.draw(win)
    middle_circle.draw(win)
    inner_circle.draw(win)
    
def drawRectangle():
    height = float(input("Please enter the height of the rectangle: \n"))
    width = float(input("Please enter the width of the rectangle: \n"))
    
    win = GraphWin("Rectangle", 200, 200)
    rectangle = Rectangle(
        Point(100-width/2, 100-height/2),
        Point(100+width/2, 100+height/2)
        )
    rectangle.draw(win)
    
def blueCircle():
    win = GraphWin("Blue Circle", 300, 300)
    
    print("Click somewhere")
    while True:
        point = win.getMouse()
        circle = Circle(point, 50)
        circle.setFill("blue")
        circle.draw(win)

def tenLines():
    win = GraphWin("Line drawer", 500, 500)
    message = Text(Point(100, 100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    for i in range(10):
        message.setText(f"Click on a {i+2}th point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        p1 = p2
        line.draw(win)
    message.setText("")

def tenStrings():
    win = GraphWin("Ten Strings", 500, 500)
    
    input_box = Entry(Point(200,10), 40)
    input_box.setText("Your message here. Click to place.")
    remaining_messages = 10
    info_box = Text(Point(140, 40), f"You have {remaining_messages} remaining \
messages.")
    
    input_box.draw(win)
    info_box.draw(win)
    for i in range(10):
        message_location = win.getMouse()
        message = Text(message_location, input_box.getText())
        message.draw(win)
        remaining_messages -= 1
        info_box.setText(f"You have {remaining_messages} remaining \
messages.")
        
def tenColouredRectanges():
    win = GraphWin("Ten Strings", 500, 500)
    
    input_box = Entry(Point(200,10), 40)
    input_box.setText("Blue")
    input_box.draw(win)
    
    for i in range(10):
        p1 = win.getMouse()
        p2 = win.getMouse()
        rectangle = Rectangle(p1, p2)
        rectangle.setFill(input_box.getText())
        rectangle.draw(win)

def fiveClickStickFigure():
    win = GraphWin("Five Click Stick Figure", 500, 500)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = ((p2.x - p1.x)**2 + (p2.y - p1.y)**2) ** 0.5
    circle = Circle(p1, radius)
    circle.draw(win)
    
    p3 = win.getMouse()
    body = Line(
        Point(p1.x, p1.y + radius),
        Point(p1.x, p3.y))
    body.draw(win)
    
    p4 = win.getMouse()
    arms = Line(
        Point(p4.x, p4.y),
        Point(p1.x + (p1.x - p4.x), p4.y)
        )
    arms.draw(win)
    
    p5 = win.getMouse()
    left_leg = Line(p5, Point(p1.x, p3.y))
    right_leg = Line(
        Point(p1.x + (p1.x - p5.x), p5.y),
        Point(p1.x, p3.y)
        )
    left_leg.draw(win)
    right_leg.draw(win)