import sys
import tkinter as tk
# from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
import turtle

def generate_lindenmayer():
    t = turtle.Turtle()
    t.forward(100)
    turtle.mainloop()
    
def add_new_rule():
    new_entry = tk.Entry(width=20)
    new_entry.pack()

window = tk.Tk()
window.title("Lindenmayer System Generator")
window.minsize(width=1000, height=500)

run_button = tk.Button(text="Generate!", command=generate_lindenmayer)
run_button.pack()

new_rule_button = tk.Button(text="Add new rule.", command=add_new_rule)
new_rule_button.pack()

window.mainloop()
