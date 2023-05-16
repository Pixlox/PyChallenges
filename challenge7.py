from graphics import *
import random

def main():
    win = GraphWin("random circles", 500, 500)

    center_x, center_y = win.getWidth() / 2, win.getHeight() / 2
    
    for i in range(100):
        c = Circle(Point(random.randint(0, 500), random.randint(0, 500)), random.randint(30, 200))
        
        colorChosen = random.choice(["blue", "red", "yellow"])
        if colorChosen == "blue":
            c.setOutline("blue")
        elif colorChosen == "red":
            c.setOutline("red")
        elif colorChosen == "yellow":
            c.setOutline("yellow")

        c.draw(win)
        
    win.mainloop()
main()