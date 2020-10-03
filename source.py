from tkinter import *

width=400
height=400

root = Tk('root')

root.geometry(f'{width}x{height}+{root.winfo_screenwidth() // 2 - width // 2}+{root.winfo_screenheight() // 2 - height // 2}')
#root.resizable(False,False)

canv = Canvas(root, width=width, height=height)
canv.pack()

for y in range(40):
    for x in range(40):
        canv.create_line(x*10,y*10,x*10+10,y*10)
        canv.create_line(x*10,y*10,x*10,y*10+10)
root.mainloop()