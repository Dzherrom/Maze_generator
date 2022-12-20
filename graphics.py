from tkinter import Tk, BOTH, Canvas
class Window:

    def __init__(self, width, height):
        # Window constructor
        self.root = Tk()
        self.root.title('Ventana de prueba')
        self.running = False
        self.canvas = Canvas(self.root, bg="blue", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
    def draw_line(self, line, fill_color="black"):
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

class Point:
    
    #stablish coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    # stabilsh points 
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    # draw line with point arguments    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y,
         fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)        