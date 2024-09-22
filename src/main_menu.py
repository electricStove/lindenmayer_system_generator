import tkinter as tk
from turtle import TurtleScreen
from lindenmayer_generator import LindenmayerGenerator

class MainMenu(tk.Tk):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.num_rules = 0
        self.rule_entries: list[tk.Entry] = []

        self.title("Lindenmayer System Main Menu")
        self.minsize(width, height)

        # This ensures that no numbers are entered into the Entry widget
        self.validate_no_numbers = (self.register(lambda input_value: input_value == "" or not input_value.isdigit()), '%S')
        # This only allows number input and 1 decimal to be added to the entry widget
        self.validate_number_only = (self.register(lambda input_value: input_value == "" or input_value.replace(".", "", 1).isdigit() and (input_value.count('.') <= 1)), '%P')

        self.starting_entry, self.starting_variables = self.create_UI()

    # Handle creating of all UI (labels, entries, buttons)
    def create_UI(self) -> tuple[ tk.Entry, dict[str, tk.Entry] ]:
        label_list = ["line length", "line length scale", "line width", "line width increment", "turn angle", "turn angle increment"]
        default_values = [1, 1.2, 1, 1, 90, 10]
        entry_dict: dict[str, tk.Entry] = {}
        # Labels
        for i in range(len(label_list)):
            curr_label = tk.Label(text=(label_list[i] + " ="), anchor='ne')
            curr_label.grid(column=3, row=i, sticky='nsew')

            curr_entry = tk.Entry(width=10, validate='key', validatecommand=self.validate_number_only) 
            curr_entry.insert(0, str(default_values[i]))
            curr_entry.grid(column=4, row=i)
            entry_dict[label_list[i]] = curr_entry

        # Entries
        start_axiom_entry = tk.Entry(width=50, validate='key', validatecommand=self.validate_no_numbers)
        start_axiom_entry.grid(column=2, row=1, padx=10)#, sticky='nsew')

        # Buttons
        new_rule_button = tk.Button(width=10, text="Add new rule", command=self.add_new_rule)
        new_rule_button.grid(column=0, row=0)#, sticky='nsew')

        delete_rule_button = tk.Button(width=10, text="Delete rule", command=self.delete_rule)
        delete_rule_button.grid(column=1, row=0)#, sticky='nsew')

        generate_button = tk.Button(text="Generate!", command=self.generate_lindenmayer)
        generate_button.grid(column=2, row=0, sticky='nsew', padx=10)

        return start_axiom_entry, entry_dict

    # Create a new text entry box under the new rule button
    # Append the entry box object to rule_entry list for later access
    def add_new_rule(self):
        self.num_rules += 1
        new_entry = tk.Entry(width=20, validate='key', validatecommand=self.validate_no_numbers)
        new_entry.grid(column=0, row=self.num_rules, columnspan=2, sticky='nsew')
        self.rule_entries.append(new_entry)

    def delete_rule(self):
        if self.num_rules == 0:
            return
        self.num_rules -= 1
        entry_to_delete = self.rule_entries.pop()
        entry_to_delete.destroy()

    # Create and run the lindenmayer system
    # The LindenmayerGenerator class is a subclass of turtle so it pops out a new window
    def generate_lindenmayer(self):
        # The next line is needed to prevent a Terminator error after closing and rerunning generator
        TurtleScreen._RUNNING=True
        generator = LindenmayerGenerator(self.get_rules(), self.starting_entry.get(), self.get_starting_variables())
        generator.run_generator()

    # Get the strings from every entry box in rule_entries and return it as a list
    def get_rules(self) -> list[str]:
        return [self.rule_entries[i].get() for i in range(len(self.rule_entries))]

    def get_starting_variables(self) -> dict[str, str]:
        return {i : self.starting_variables[i].get() for i in self.starting_variables}
