import turtle

class LindenmayerGenerator(turtle.Turtle):
    def __init__(self, unparsed_rules: list[str], starting_str: str):
        super().__init__()
        # Initializing rules and axioms
        self.axiom: str = starting_str
        self.next_axiom: str = ""
        self.rules: dict[str, str] = {}

        # Default drawing values
        self.line_length = 10
        self.line_length_scale = 1.2
        self.line_width = 1
        self.line_width_increment = 1
        self.turn_angle = 10
        self.turn_angle_increment = 10


        # self.default_rules: list[str] = ['F', 'f', '+', '-', '|',
        #                                  '[', ']', '#', '!', '@',
        #                                  '{', '}', '<', '>', '&',
        #                                  '(', ')']

        self.parse_rules(unparsed_rules)
        print(f'\n\n******** starting_str: ' + self.axiom + '********\n\n')

    def run_generator(self):
        for i in self.axiom:
            if i in self.rules:
                self.next_axiom += self.rules[i]
            match i:
                # Move forward by line length drawing a line
                case 'F':
                    self.pendown()
                    self.forward(self.line_length)
                # Move forward by line length without drawing a line
                case 'f':
                    self.penup()
                    self.forward(self.line_length)
                # Turn left by turning angle
                case '+':
                    self.left(self.turn_angle)
                # Turn right by turning angle
                case '-':
                    self.right(self.turn_angle)
                # Reverse direction (ie: turn by 180 degrees)
                case '|':
                    self.right(180)
                # Push current drawing state onto stack
                case '[':
                    pass
                # Pop current drawing state from the stack
                case ']':
                    pass
                # Increment the line width by line width increment
                case  '#':
                    self.line_width += self.line_width_increment
                # Decrement the line width by line width increment
                case '!':
                    self.line_width -= self.line_width_increment
                # Draw a dot with line width radius
                case '@':
                    pass
                # # Open a polygon
                # case '{':
                #     pass
                # # Close a polygon and fill it with fill colour
                # case '}':
                #     pass
                # Multiply the line length by the line length scale factor
                case '<':
                    self.line_length *= self.line_length_scale
                # Divide the line length by the line length scale factor
                case '>':
                    self.line_length /= self.line_length_scale
                # # Swap the meaning of + and -
                # case '&':
                #     pass
                # Decrement turning angle by turning angle increment
                case '(':
                    self.turn_angle -= self.turn_angle_increment
                # Increment turning angle by turning angle increment
                case ')':
                    self.turn_angle += self.turn_angle_increment
                case _:
                    pass
        print(f'\n\n********** next_axiom: ' + self.next_axiom + '**********\n\n') 
        turtle.mainloop()

    def parse_rules(self, unparsed: list[str]):
        for i in unparsed:
            i = i.split("=")
            # throw error if rule name is not one letter
            self.rules[i[0]] = i[1]
