from tkinter import Tk, BOTH, Canvas

class window:

    def __init__(self, width, height):
        # Window constructor
        self.root = Tk()
        self.root.title('Ventana de prueba')
        self.running = False
        self.cv = Canvas(self.root, bg="blue", height=height, width=width)
        self.cv.pack(fill=BOTH, expand=1)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
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

    def close(self):
        self.running = False
            