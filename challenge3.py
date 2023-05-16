from graphics import *

def main():
    win = GraphWin("4 rectangle yay", 400, 400)

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

    win.mainloop()

main()
