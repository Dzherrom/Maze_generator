from tkinter import Tk, BOTH, Canvas
class Window:

    def __init__(self, width, height):
        # Window constructor
        self.root = Tk()
        self.root.title('Ventana de prueba')
        self.running = False
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    # Redraw method updates
    def redraw(self):
        self.root.update()
        self.root.update_idletasks()
    
    # Sets running state true and calls redraw method
    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
        print("window closed")

    # closes program
    def close(self):
        self.running = False


class Line:
    # stabilsh coordinates
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


    # draw line with point arguments    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color,
)
        canvas.pack(fill=BOTH, expand=1)        

