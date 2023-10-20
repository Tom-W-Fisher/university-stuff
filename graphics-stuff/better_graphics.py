from graphics import *

class Point(Point):
    def __add__(self, other_point):
        if type(other_point) != Point:
            raise TypeError("Can only add points to points. Object of type "
                             + str(type(other_point)) + " was given.")
        return Point(self.getX() + other_point.getX(), self.getY() + other_point.getY())
    
    def __sub__(self, other_point):
        if type(other_point) != Point:
            raise TypeError("Can only subtract points from points. Object of type "
                             + str(type(other_point)) + " was given.")
        return Point(self.getX() - other_point.getX(), self.getY() - other_point.getY())
    
    def __mul__(self,some_int: int):
        if type(some_int) not in (int, float):
            raise TypeError("Can only multiply points by numerics (int & float)"
                             + ". Object of type "
                             + str(type(other_point)) + " was given.")
        return Point(self.getX()*some_int, self.getY()*some_int)
    
    def __truediv__(self, some_int: int):
        if type(some_int) not in (int, float):
            raise TypeError("Can only divide points by numerics (int & float)"
                             + ". Object of type "
                             + str(type(other_point)) + " was given.")
        return Point(self.getX()/some_int, self.getY()/some_int)
    
    def __floordiv__(self, some_int: int):
        if type(some_int) not in (int, float):
            raise TypeError("Can only divide points by numerics (int & float)"
                             + ". Object of type "
                             + str(type(other_point)) + " was given.")
        return Point(self.getX()//some_int, self.getY()//some_int)


class GraphWin(GraphWin):
    def getMouse(self):
        """Wait for mouse click and return Point object representing
        the click"""
        self.update()      # flush any prior clicks
        self.mouseX = None
        self.mouseY = None
        while self.mouseX == None or self.mouseY == None:
            self.update()
            if self.isClosed(): raise GraphicsError("getMouse in closed window")
            time.sleep(.1) # give up thread
        x,y = self.toWorld(self.mouseX, self.mouseY)
        self.mouseX = None
        self.mouseY = None
        return Point(x,y)
    
    