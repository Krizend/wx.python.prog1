from tkinter import *

width=400
height=400

root = Tk('root')

root.geometry(f'{width}x{height}+{root.winfo_screenwidth() // 2 - width // 2}+{root.winfo_screenheight() // 2 - height // 2}')
root.resizable(False,False)

canv = Canvas(root, width=width, height=height, borderwidth=0)
canv.pack()

def motion_(event):
    x, y = event.x, event.y
    r=60
    canv.create_oval(x-r, y-r, x+r, y+r, tags="draw")
    #canv.create_oval(x, y, 5, 5, tags="draw")


def clear_(event):
    canv.delete("draw")
    #canv.delete(ALL)

for y in range(0, 400, 10):
    for x in range(0, 400, 10):
        canv.create_line(x,y,x+10,y)
        canv.create_line(x,y,x,y+10)

root.bind('<B1-Motion>', motion_)
root.bind('<Button-1>', motion_)
root.bind('<c>', clear_)
root.mainloop()
