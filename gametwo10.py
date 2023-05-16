from graphics import *
import time
import random

def main():
    win = GraphWin("shape go left right up down", 400, 400)
    shape = Circle(Point(200, 200), 20)
    shape.setFill("red")
    shape.draw(win)

    target_x = random.randint(10, 390)
    target_y = random.randint(10, 390)
    target = Circle(Point(target_x, target_y), 10)
    controlsMessage = Text(Point(200, 50), "Controls: WASD \nGet to the green point.")
    controlsMessage.setSize(18)
    controlsMessage.draw(win)
    target.setFill("green")
    target.draw(win)

    start_time = time.time()
    time_limit = 10

    while True:
        key = win.checkKey()
        if key == "w":
            shape.move(0, -10)
        elif key == "s":
            shape.move(0, 10)
        elif key == "a":
            shape.move(-10, 0)
        elif key == "d":
            shape.move(10, 0)

        current_time = time.time()
        time_elapsed = current_time - start_time
        if time_elapsed > time_limit:
            message = Text(Point(200, 200), "times up, you lose :(")
            message.setSize(36)
            message.draw(win)
            win.getMouse()
            break

        shape_center = shape.getCenter()
        target_center = target.getCenter()
        if abs(shape_center.getX() - target_center.getX()) < 10 and abs(shape_center.getY() - target_center.getY()) < 10:
            message = Text(Point(200, 200), "you won yay :D")
            message.setSize(36)
            message.draw(win)
            win.getMouse()
            break

main()
