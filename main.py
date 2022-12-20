from graphics import Window, Line, Point

def run():
    win = Window(800, 600)
    l = Line(point1=(50,50), point2=(400, 400))
    win.draw_line(l, "red")
    win.wait_for_close()

if __name__ == '__main__':
    run()