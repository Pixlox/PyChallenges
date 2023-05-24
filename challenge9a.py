from graphics import *
import time
import random

def main():
    win = GraphWin("sleep timer shape", 400, 400)

    shape = Circle(Point(200, 200), 50)
    shape.setFill("red")
    shape.draw(win)

    while True:
        new_x = random.randint(0, win.getWidth())
        new_y = random.randint(0, win.getHeight())
        dx = new_x - shape.getCenter().getX()
        dy = new_y - shape.getCenter().getY()
        shape.move(dx, dy)

        time.sleep(0.5)

main()
