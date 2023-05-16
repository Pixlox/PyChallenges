from graphics import *
import random

def change_colour(rectangles, clicked_rectangle):
    for rectangle in rectangles:
        if rectangle != clicked_rectangle:
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

    rectangles = [rect1, rect2, rect3, rect4]

    while True:
        click_point = win.getMouse()
        clicked_rectangle = None

        for rectangle in rectangles:
            if rectangle.getP1().getX() <= click_point.getX() <= rectangle.getP2().getX() and \
                    rectangle.getP1().getY() <= click_point.getY() <= rectangle.getP2().getY():
                clicked_rectangle = rectangle
                break

        if clicked_rectangle:
            change_colour(rectangles, clicked_rectangle)

main()
