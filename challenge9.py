from graphics import *
import random

def change_color(rectangle):
    current_colour = rectangle.config.get("fill")
    shapeColour = random.choice(["red", "cyan", "green", "magenta", "blue", "orange", "yellow", "purple"]) 
    rectangle.setFill(shapeColour)

def main():
    win = GraphWin("4 rectangles yay", 400, 400)

    x1, y1 = 0, 0
    x2, y2 = win.getWidth() / 2, win.getHeight() / 2
    x3, y3 = win.getWidth(), win.getHeight()

    rect1 = Rectangle(Point(x1, y1), Point(x2, y2))
    rect1.setFill("red")
    rect1.draw(win)

    rect2 = Rectangle(Point(x2, y1), Point(x3, y2))
    rect2.setFill("green")
    rect2.draw(win)

    rect3 = Rectangle(Point(x1, y2), Point(x2, y3))
    rect3.setFill("blue")
    rect3.draw(win)

    rect4 = Rectangle(Point(x2, y2), Point(x3, y3))
    rect4.setFill("yellow")
    rect4.draw(win)

    while True:
        click_point = win.getMouse()
        if rect1.getP1().getX() <= click_point.getX() <= rect1.getP2().getX() and \
           rect1.getP1().getY() <= click_point.getY() <= rect1.getP2().getY():
            change_color(rect1)
        elif rect2.getP1().getX() <= click_point.getX() <= rect2.getP2().getX() and \
             rect2.getP1().getY() <= click_point.getY() <= rect2.getP2().getY():
            change_color(rect2)
        elif rect3.getP1().getX() <= click_point.getX() <= rect3.getP2().getX() and \
             rect3.getP1().getY() <= click_point.getY() <= rect3.getP2().getY():
            change_color(rect3)
        elif rect4.getP1().getX() <= click_point.getX() <= rect4.getP2().getX() and \
             rect4.getP1().getY() <= click_point.getY() <= rect4.getP2().getY():
            change_color(rect4)

main()
