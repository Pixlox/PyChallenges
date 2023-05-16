from graphics import *
import random

def main():
    win = GraphWin("random circles", 500, 500)

    center_x, center_y = win.getWidth() / 2, win.getHeight() / 2
    
    c = Circle(Point(center_x, center_y), random.randint(30, 200))

    c.draw(win)
    win.mainloop()
main()