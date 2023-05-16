from graphics import *
import random

def main():
    win = GraphWin("SHAPE WOW", 500, 500)
    
    for _ in range(10):
        shape = random.choice(["circle", "rectangle", "triangle"]) 
        
        if shape == "circle":
            center = Point(random.randint(50, 450), random.randint(50, 450))
            radius = random.randint(10, 50)
            color = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            circle = Circle(center, radius)
            circle.setFill(color)
            circle.draw(win)
        
        elif shape == "rectangle":
            p1 = Point(random.randint(50, 400), random.randint(50, 400))
            p2 = Point(p1.getX() + random.randint(10, 100), p1.getY() + random.randint(10, 100))
            color = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            rectangle = Rectangle(p1, p2)
            rectangle.setFill(color)
            rectangle.draw(win)
        
        elif shape == "triangle":
            p1 = Point(random.randint(50, 450), random.randint(50, 450))
            p2 = Point(p1.getX() + random.randint(-100, 100), p1.getY() + random.randint(-100, 100))
            p3 = Point(p1.getX() + random.randint(-100, 100), p1.getY() + random.randint(-100, 100))
            color = color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            triangle = Polygon(p1, p2, p3)
            triangle.setFill(color)
            triangle.draw(win)
    
    win.mainloop()

main()
