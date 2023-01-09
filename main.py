from graphics import Window, Line

def run():
    win = Window(800, 600)
    l = Line(50, 400, 20, 350)
    win.draw_line(l, "red")
    win.wait_for_close()

if __name__ == '__main__':
    run()