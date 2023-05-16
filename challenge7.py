from graphics import *

def main():
    # Name to be shown
    name = "Omar"

    win = GraphWin("Moving Text", 400, 400)
    text = Text(Point(200, 200), name)
    text.setSize(20)
    text.draw(win)

    while True:
        click_point = win.getMouse()
        if (text.getAnchor().getX() - 50 <= click_point.getX() <= text.getAnchor().getX() + 50) and \
           (text.getAnchor().getY() - 10 <= click_point.getY() <= text.getAnchor().getY() + 10):
            text.move(click_point.getX() - text.getAnchor().getX(), click_point.getY() - text.getAnchor().getY())

    win.close()

main()
