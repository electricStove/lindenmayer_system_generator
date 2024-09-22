import turtle

_LINE_LENGTH = 2
_LINE_LENGTH_SCALE = 1.2
_LINE_WIDTH = 1
_LINE_WIDTH_INCREMENT = 1
_TURN_ANGLE = 90
_TURN_ANGLE_INCREMENT = 10
_POSITION_STACK = []

class LindenmayerGenerator(turtle.Turtle):
    def __init__(self, unparsed_rules: list[str], starting_str: str, starting_vars: dict[str, str]):
        super().__init__()
        _LINE_LENGTH = float(starting_vars["line length"])
        _LINE_LENGTH_SCALE =  float(starting_vars["line length scale"])
        _LINE_WIDTH =  float(starting_vars["line width"])
        _LINE_WIDTH_INCREMENT =  float(starting_vars["line width increment"])
        _TURN_ANGLE =  float(starting_vars["turn angle"])
        _TURN_ANGLE_INCREMENT =  float(starting_vars["turn angle increment"])
        turtle.setup()
        turtle.screensize(10000, 10000)
        turtle.tracer(0, 0)

        # Initializing rules and axioms
        self.axiom: str = starting_str
        self.next_axiom: str = ""
        self.rules: dict[str, str] = {}

        # Default drawing values
        self.line_length: float = _LINE_LENGTH
        self.line_length_scale: float = _LINE_LENGTH_SCALE
        self.line_width: float = _LINE_WIDTH
        self.line_width_increment: float = _LINE_WIDTH_INCREMENT
        self.turn_angle: float = _TURN_ANGLE
        self.turn_angle_increment: float = _TURN_ANGLE_INCREMENT
        self.position_stack: list[turtle.Vec2D] = _POSITION_STACK

        # self.default_rules: list[str] = ['F', 'f', '+', '-', '|',
        #                                  '[', ']', '#', '!', '@',
        #                                  '{', '}', '<', '>', '&',
        #                                  '(', ')']

        self.parse_rules(unparsed_rules)

    def run_generator(self):
        self.step_forward()

        turtle.listen()
        turtle.onkeypress(self.step_forward, "Right")
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
                    self.position_stack.append(self.position())
                # Pop current drawing state from the stack
                case ']':
                    self.setposition(self.position_stack.pop())
                # Increment the line width by line width increment
                case  '#':
                    self.line_width += self.line_width_increment
                # Decrement the line width by line width increment
                case '!':
                    self.line_width -= self.line_width_increment
                # Draw a dot with line width radius
                case '@':
                    self.dot(size=round(self.line_width))
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
        self.setheading(90)
        self.line_length = _LINE_LENGTH
        self.line_length_scale = _LINE_LENGTH_SCALE
        self.line_width = _LINE_WIDTH
        self.line_width_increment = _LINE_WIDTH_INCREMENT
        self.turn_angle = _TURN_ANGLE
        self.turn_angle_increment = _TURN_ANGLE_INCREMENT
        self.position_stack = _POSITION_STACK
