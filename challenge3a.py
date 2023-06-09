from graphics import *

def main():
    win = GraphWin("python deathly hallows", 400, 400)

    center_x, center_y = win.getWidth() / 2, win.getHeight() / 2

    triangle_size = 200
    triangle_height = triangle_size * (3 ** 0.5) / 2

    triangle_p1 = Point(center_x, center_y - (triangle_height / 3))
    triangle_p2 = Point(center_x - triangle_size / 2, center_y + (2 * triangle_height) / 3)
    triangle_p3 = Point(center_x + triangle_size / 2, center_y + (2 * triangle_height) / 3)

    triangle = Polygon(triangle_p1, triangle_p2, triangle_p3)
    triangle.setWidth(2)
    triangle.setOutline("black")
    
    triangle.draw(win)

    circle_radius = triangle_size / 3.6
    circle_center = Point(center_x, center_y + 30 + triangle_height / 6)

    circle = Circle(circle_center, circle_radius)
    circle.setWidth(2)
    circle.setOutline("black")
    circle.draw(win)

    line_start = Point(center_x, center_y + 32 - triangle_height / 2)
    line_end = Point(center_x, center_y + 30 + triangle_height / 2)

    line = Line(line_start, line_end)
    line.setWidth(2)
    line.setOutline("black")
    line.draw(win)

    win.mainloop()

main()