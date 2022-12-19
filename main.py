from graphics import window

def run():
    win = window(500, 500)
    draw_line()
    draw_line()
    win.wait_for_close()

if __name__ == '__main__':
    run()