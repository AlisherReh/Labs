import tkinter as tk

# создаем окно
root = tk.Tk()

# создаем поле для рисования
canvas = tk.Canvas(root, width=600, height=220, bg="black")
canvas.pack()

# рисуем букву "A"
canvas.create_line(50, 100, 50, 150, fill="white")
canvas.create_line(50, 100, 100, 50, fill="white")
canvas.create_line(100, 50, 100, 150, fill="white")
canvas.create_line(50, 100, 100, 100, fill="white")

# рисуем букву "l"
canvas.create_line(120, 50, 120, 150, fill="white")
canvas.create_line(120, 150, 170, 150, fill="white")

# рисуем букву "i"
canvas.create_oval(180, 50, 200, 70, fill="white")
canvas.create_line(190, 70, 190, 150, fill="white")

# рисуем букву "s"
canvas.create_arc(230, 50, 300, 140, start=30, extent=180, fill="white")
canvas.create_arc(210, 70, 280, 160, start=30, extent=-180, fill="white")

# рисуем букву "h"
canvas.create_line(330, 50, 330, 150, fill="white")
canvas.create_line(330, 100, 380, 100, fill="white")
canvas.create_line(380, 50, 380, 150, fill="white")

# рисуем букву "e"
canvas.create_line(410, 50, 410, 150, fill="white")
canvas.create_line(410, 100, 450, 100, fill="white")
canvas.create_line(410, 50, 450, 50, fill="white")
canvas.create_line(410, 150, 450, 150, fill="white")

# рисуем букву "r"
canvas.create_line(480, 50, 480, 150, fill="white")
canvas.create_line(480, 50, 530, 50, fill="white")
canvas.create_line(480, 100, 530, 50, fill="white")
canvas.create_line(480, 100, 530, 150, fill="white")
# запускаем главный цикл
root.mainloop()
