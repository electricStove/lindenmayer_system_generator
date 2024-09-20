import turtle

class LindenmayerGenerator(turtle.Turtle):
    def __init__(self, unparsed_rules: list[str], starting_str: str):
        super().__init__()
        self.starting_string = starting_str
        self.default_rules: list[str] = ['F', 'f', '+', '-',
                                         '|', '[', ']', '#',
                                         '!', '@', '{', '}',
                                         '<', '>', '&', '(', ')']
        self.rules: dict[str, str] = {}
        self.parse_rules(unparsed_rules)
        print(f'\n\n******** starting_str: ' + self.starting_string + '********\n\n')

    def run_generator(self):
        for i in self.rules.values():
            if i in self.default_rules:
                print(f'{i} is in default_rules')
            else:
                print(f'{i} is a user defined rule')
        turtle.mainloop()

    def parse_rules(self, unparsed: list[str]):
        for i in unparsed:
            i = i.split("=")
            # throw error if rule name is not one letter
            #       or if rule name is in default_rules
            self.rules[i[0]] = i[1]
