import tkinter as tk
from turtle import TurtleScreen
from lindenmayer_generator import LindenmayerGenerator

class MainMenu(tk.Tk):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.num_rules = 0
        self.rule_entries = []

        self.title("Lindenmayer System Main Menu")
        self.minsize(width, height)

        self.create_buttons()

        self.starting_entry = tk.Entry(width=50)
        self.starting_entry.grid(column=10, row=1, sticky='nsew')

    def create_buttons(self):
        run_button = tk.Button(text="Generate!", command=self.generate_lindenmayer)
        run_button.grid(row=0, column=10, sticky='nsew')

        new_rule_button = tk.Button(text="Add new rule.", command=self.add_new_rule)
        new_rule_button.grid(row=0, column=0, sticky='nsew')

    def add_new_rule(self):
        self.num_rules += 1
        new_entry = tk.Entry(width=20)
        new_entry.grid(column=0, row=self.num_rules, sticky='nsew')
        self.rule_entries.append(new_entry)

    def generate_lindenmayer(self):
        # The next line is needed to prevent a Terminator error after closing and rerunning generator
        TurtleScreen._RUNNING=True
        generator = LindenmayerGenerator(self.get_rules(), self.starting_entry.get())
        generator.run_generator()

    def get_rules(self) -> list[str]:
        return [self.rule_entries[i].get() for i in range(len(self.rule_entries))]
        
