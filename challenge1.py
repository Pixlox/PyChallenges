from graphics import *

def main():
	win = GraphWin("Circle", 100, 100)
	c = Circle(Point(50, 50), 10)
	c.draw(win)
	win.getMouse()
	win.Close()

main()
