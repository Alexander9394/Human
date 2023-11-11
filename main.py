from tkinter import Tk, Canvas
from grid import Grid
from Human import Human

root = Tk()
canvas = Canvas(root, width = 800, height = 600)
canvas.pack()
grid = Grid(canvas)
grid.display()
p1 = Human(canvas, 'Григорий', 100, 500, "Мужчина")
p1.display()
p2 = Human(canvas, 'Екатерина', 200, 500, "Женщина")
p2.display()
root.mainloop()
