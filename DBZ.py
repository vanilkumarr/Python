from tkinter import *
import time,random
WIDTH=900
HEIGHT=600

xvel=2
yvel=1



window=Tk()

canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

bg=PhotoImage(file="dd2jp4h-1cad541d-b8e8-4f50-ae6f-a986082910b0.png")
canvas.create_image(0,0,image=bg,anchor=NW)

image1=PhotoImage(file="1.png")
myimage=canvas.create_image(0,0,image=image1,anchor=NW)

image_width=image1.width()
image_height=image1.height()
while True:
    coordinates=canvas.coords(myimage)
    print(coordinates)
    if coordinates[0]>=WIDTH-image_width or coordinates[0]<0:
        xvel=-xvel
    if coordinates[1]>=HEIGHT-image_height or coordinates[1]<0:
        yvel=-yvel   
    canvas.move(myimage,xvel,yvel)

    window.update()
    time.sleep(0.01)


window.mainloop()