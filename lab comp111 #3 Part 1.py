# Name: Mark Waako
# Class: Comp111 Lab A
# Assignment 9 Part 1

from tkinter import *

root = Tk()


root.title("Title")
root.configure(bg="white")

canvas1= Canvas(root, width= 600, height = 600, bg= "Grey" )
canvas1.pack()
#        cords            X  Y   x   y
canvas1.create_rectangle(450,5,600,250,fill="Light blue",outline= "blue",width=5)
canvas1.create_rectangle(5,350,150,600,fill="Light blue",outline= "blue",width=5)
canvas1.create_rectangle(5,5,150,250,fill="Light blue",outline= "blue",width=5)
canvas1.create_rectangle(450,350,600,600,fill="Light blue",outline= "blue",width=5)
canvas1.create_oval(250,250,350,350,fill="black",outline= "cyan",width=5)

root.mainloop()
