import tkinter as tk
import turtle

window = tk.Tk()
window.title("DENIS PIDOR")

entry = tk.Entry(window, width=20, font=("Arial", 16), justify="center")
entry.grid(row=0, column=0, columnspan=4)

def check_text():
    if entry.get() == "pidor":
        print("nice")
        screen = turtle.Screen()
        screen.bgcolor("white")
        t = turtle.Turtle()
        t.speed(3)
        t.color("red")


        t.begin_fill()
        t.left(50)
        t.forward(100)
        t.circle(50, 200)
        t.right(140)
        t.circle(50, 200)
        t.forward(100)
        t.end_fill()
        turtle.bye()
    else:
        {}


check_button = tk.Button(window, text="SOSI", command=check_text, font=("Arial", 14))
check_button.grid(row=1, column=0, columnspan=4)

window.mainloop()