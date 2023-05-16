from graphics import *
import random

def main():
    win = GraphWin("random circles", 500, 500)

    center_x, center_y = win.getWidth() / 2, win.getHeight() / 2
    
    for i in range(100):
        c = Circle(Point(random.randint(0, 500), random.randint(0, 500)), random.randint(30, 200))
        
        randColor = random.randint(1, 3)
        if randColor == 1:
            c.setOutline("blue")
        elif randColor == 2:
            c.setOutline("red")
        elif randColor == 3:
            c.setOutline("yellow")

        c.draw(win)
        
    win.mainloop()
main()