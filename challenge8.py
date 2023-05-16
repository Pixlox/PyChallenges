from graphics import *

def main():
    win = GraphWin("Text Entry", 400, 400)

    entry = Entry(Point(200, 50), 20)
    entry.draw(win)

    text_box = Text(Point(200, 200), "")
    text_box.setSize(14)
    text_box.draw(win)

    while True:
        key = win.getKey()

        if key == "Return":
            break

        elif key == "BackSpace":
            text = text_box.getText()
            text_box.setText(text[:-1]) 

        # Checking if Backspace because it doesn't handle well with Backspace, exclamation, question, etc.
        # Also this is kinda bad implementation not gonna lie

        elif key.isprintable() or key == " ":
            text_box.setText(text_box.getText() + key)  

    win.close()

main()
