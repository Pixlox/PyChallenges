from graphics import *
import time
import random
import math

def main():
    win = GraphWin("game one", 400, 400)

    shape = Circle(Point(200, 200), 50)
    shape.setFill("red")
    shape.draw(win)

    score = 0
    score_text = Text(Point(200, 20), "Score: " + str(score))
    score_text.draw(win)

    while True:
        new_x = random.randint(0, win.getWidth())
        new_y = random.randint(0, win.getHeight())
        dx = new_x - shape.getCenter().getX()
        dy = new_y - shape.getCenter().getY()
        shape.move(dx, dy)

        while True:
            click_point = win.getMouse()
            if clicked(shape, click_point):
                score += 1
                score_text.setText("Score: " + str(score))
                break
            else:
                score = 0
                score_text.setText("Score: " + str(score))

        time.sleep(0.5)

    win.close()

def clicked(shape, point):
    distance = math.sqrt((point.getX() - shape.getCenter().getX()) ** 2 +
                         (point.getY() - shape.getCenter().getY()) ** 2)
    return distance <= shape.getRadius()

main()
