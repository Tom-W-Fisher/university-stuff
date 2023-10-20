from better_graphics import *
import math

def main():
    my_window = GraphWin("Sbeve", 1000, 800)
    
    point1 = my_window.getMouse()
    
    while True:
        point2 = my_window.getMouse()
    
        koch = KochCurve(point1, point2, 3)
        koch.draw(my_window)
        point1 = point2
    my_window.getMouse()
    my_window.close()
    
class KochCurve:
    def __init__(self, start_point, end_point, levels_below=1):
        self.levels_below = levels_below
        self.p1 = start_point
        self.p2 = end_point
        self.length = math.sqrt((start_point.getY()-end_point.getY())**2 +
                                (start_point.getX()-end_point.getX())**2)
    
        if levels_below > 0:
            self.sections = []
            section_length = self.length / 3
            
            # "thirdpoint" refers to point a third along the length of a line
            first_thirdpoint: Point = (start_point*2 + end_point) /3
            second_thirdpoint: Point = (start_point + end_point*2) /3
            self.sections.append(KochCurve(start_point, first_thirdpoint, levels_below-1))
            
            y_change = second_thirdpoint.getY() - first_thirdpoint.getY()
            x_change = second_thirdpoint.getX() - first_thirdpoint.getX()
            
            initial_angle_to_horizontal = math.atan(y_change / x_change)
            
            # This if statement makes it so the out-dent always appears on the right as you traverse the curve
            if first_thirdpoint.getX() > second_thirdpoint.getX():
                angle_to_horizontal = initial_angle_to_horizontal + 1/3 * math.pi
            else:
                angle_to_horizontal = initial_angle_to_horizontal - 1/3 * math.pi
            
            y_change = math.sin(angle_to_horizontal) * section_length
            x_change = math.cos(angle_to_horizontal) * section_length
            
            # This if statement stops things from looking messed up
            if first_thirdpoint.getX() > second_thirdpoint.getX():
                triangle_point = Point(second_thirdpoint.getX() + x_change,
                                   second_thirdpoint.getY() + y_change)
            else:
                triangle_point = Point(first_thirdpoint.getX() + x_change,
                                   first_thirdpoint.getY() + y_change)
            
            self.sections.append(KochCurve(first_thirdpoint, triangle_point, levels_below-1))
            self.sections.append(KochCurve(triangle_point, second_thirdpoint, levels_below-1))
        
            self.sections.append(KochCurve(second_thirdpoint, end_point, levels_below-1))
        else:
            self.body = Line(start_point, end_point)
    
    def draw(self, window):
        if self.levels_below == 0:
            self.body.draw(window)
        else:
            for section in self.sections:
                section.draw(window)
        
        
        
main()