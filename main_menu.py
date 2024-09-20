import tkinter as tk

class MainMenu():
    def __init__(self, width: int, height: int):
        self.window = tk.Tk()
        self.window.title("Lindenmayer System Main Menu")
        self.window.minsize(width, height)

        self.create_buttons()

    def create_buttons(self):
        run_button = tk.Button(text="Generate!")#, command=generate_lindenmayer)
        run_button.pack()

        new_rule_button = tk.Button(text="Add new rule.")#, command=add_new_rule)
        new_rule_button.pack()
