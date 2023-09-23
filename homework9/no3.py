import tkinter as tk

class CircleDrawer:
    def __init__(self, root, canvas_width=400, canvas_height=400, circle_radius=30):
        self.root = root
        self.root.title("Circle Drawer")
        
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.pack()
        
        self.circle_radius = circle_radius
        
        # Bind left mouse click to create_circle method
        self.canvas.bind("<Button-1>", self.create_circle)
        
        # Bind right mouse click to remove_circle method
        self.canvas.bind("<Button-3>", self.remove_circle)
    
    def create_circle(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - self.circle_radius, y - self.circle_radius, x + self.circle_radius, y + self.circle_radius)
    
    def remove_circle(self, event):
        x, y = event.x, event.y
        # Find all items within a small radius of the right-click position
        items = self.canvas.find_overlapping(x - self.circle_radius, y - self.circle_radius, x + self.circle_radius, y + self.circle_radius)
        for item in items:
            self.canvas.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = CircleDrawer(root)
    root.mainloop()
