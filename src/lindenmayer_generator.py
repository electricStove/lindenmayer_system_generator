import turtle

class LindenmayerGenerator(turtle.Turtle):
    def __init__(self, unparsed_rules: list[str], starting_str: str, starting_vars: dict[str, str]):
        super().__init__()
        turtle.setup()
        turtle.screensize(10000, 10000)
        turtle.tracer(0, 0)

        # Initializing rules and axioms
        self.starting_vars = starting_vars
        self.axiom: str = starting_str
        self.next_axiom: str = ""
        self.rules: dict[str, str] = {}

        # Default drawing values
        self.line_length: float = float(self.starting_vars["line length"])
        self.line_length_scale: float =  float(self.starting_vars["line length scale"])
        self.line_width: float =  float(self.starting_vars["line width"])
        self.line_width_increment: float =  float(self.starting_vars["line width increment"])
        self.turn_angle: float =  float(self.starting_vars["turn angle"])
        self.turn_angle_increment: float =  float(self.starting_vars["turn angle increment"])
        self.state_stack: list[tuple[turtle.Vec2D, float]] = []

        # Turn the list of rules into a dictionary with the key as the name and value as the rewriting rule
        self.parse_rules(unparsed_rules)

    def run_generator(self):
        self.step_forward()

        turtle.listen()
        turtle.onkeypress(self.step_forward, "space")
        turtle.onkeypress(self.step_forward, "w")
        turtle.mainloop()

    def step_forward(self):
        self.reset_screen()
        for i in self.axiom:
            if i in self.rules:
                self.next_axiom += self.rules[i]
            else:
                self.next_axiom += i
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
                    self.right(self.turn_angle)
                # Turn right by turning angle
                case '-':
                    self.left(self.turn_angle)
                # Reverse direction (ie: turn by 180 degrees)
                case '|':
                    self.right(180)
                # Push current drawing state onto stack
                case '[':
                    self.state_stack.append((self.position(), self.heading()))
                # Pop current drawing state from the stack
                case ']':
                    prev_state = self.state_stack.pop()
                    self.setposition(prev_state[0])
                    self.setheading(prev_state[1])
                # Increment the line width by line width increment
                case  '#':
                    self.line_width += self.line_width_increment
                # Decrement the line width by line width increment
                case '!':
                    self.line_width -= self.line_width_increment
                # Draw a dot with line width radius
                case '@':
                    self.dot(size=round(self.line_width))
                # Multiply the line length by the line length scale factor
                case '<':
                    self.line_length *= self.line_length_scale
                # Divide the line length by the line length scale factor
                case '>':
                    self.line_length /= self.line_length_scale
                # Swap the meaning of + and -
                case '&':
                    self.turn_angle = -self.turn_angle
                    self.turn_angle_increment = -self.turn_angle_increment
                # Decrement turning angle by turning angle increment
                case '(':
                    self.turn_angle -= self.turn_angle_increment
                # Increment turning angle by turning angle increment
                case ')':
                    self.turn_angle += self.turn_angle_increment
                case _:
                    pass
        turtle.update()
        self.axiom = self.next_axiom
        self.next_axiom = ""

    def parse_rules(self, unparsed: list[str]):
        for i in unparsed:
            i = i.split("=")
            # throw error if rule name is not one letter
            self.rules[i[0]] = i[1]

    def reset_screen(self):
        self.reset()
        self.hideturtle()
        self.speed(0)
        self.setheading(0)
        self.line_length = float(self.starting_vars["line length"])
        self.line_length_scale =  float(self.starting_vars["line length scale"])
        self.line_width =  float(self.starting_vars["line width"])
        self.line_width_increment =  float(self.starting_vars["line width increment"])
        self.turn_angle =  float(self.starting_vars["turn angle"])
        self.turn_angle_increment =  float(self.starting_vars["turn angle increment"])
        self.state_stack = []
