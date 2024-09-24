# Lindenmayer System Generator
This project is currently a work in progress. Everything is usable, I am just working on the UI/UX on the main menu. I will also be working on adding zooming and scrolling once your image is generated.

This is a fun side project that uses Python's `Tkinter` and `Turtle` libraries to create and visualize Lindenmayer Systems (L-Systems). These systems, often used to generate fractals, can be customized by defining a starting axiom and some rules.

## References
- [L-System User Notes](https://paulbourke.net/fractals/lsys/) by Paul Borke
- [L-System wikipedia page](https://en.wikipedia.org/wiki/L-system)

## Project Overview

A Lindenmayer System (L-System) is a mathematical framework used to model the growth processes of plants and generate fractal-like patterns. It operates on a set of rules that transform a starting string, or axiom, through recursive rewriting.

### Key Components:
1. **Alphabet**: A set of symbols (letters) used to represent elements of the system.
2. **Axiom**: The initial string that serves as the starting point for the pattern.
3. **Rewriting Rules**: Rules that specify how symbols in the axiom are replaced with new combinations of symbols.

### How It Works:
1. **Start with the axiom**.
2. **Apply the rewriting rules** to each symbol in the axiom. If a symbol matches the left-hand side (LHS) of a rule, it is replaced by the right-hand side (RHS) of that rule.
3. **Repeat the process** creating increasingly complex strings by stepping through each generation.

Through this iterative process, simple initial strings can evolve into intricate patterns, mimicking natural growth processes like those seen in plants. L-Systems are also commonly used to generate fractals.

The Lindenmayer System Generator allows users to:
- Input a starting axiom (the initial string representing the base state of the system).
- Define custom rules to evolve the system, where each rule maps a character to a sequence of other characters.
- Visualize each generation of the system step-by-step using Turtle graphics.

## Dependencies

This project relies on Python's standard libraries:

- **Tkinter**: Used for the graphical user interface.
- **Turtle**: Used to render the visual representation of the L-System.

No additional external libraries are required.

## Installation and Setup

1. Ensure you have Python installed. This project should work with Python 3.10 or higher, though it hasn't been tested with specific versions.
2. Clone the repository to your local machine:
```bash
    git clone https://github.com/electricStove/lindenmayer_system_generator.git
```
- You can also fork this repository.
3. Navigate to the project directory:
```bash
    cd /path/to/lindenmayer_system_generator/src/
```
4. Run the program by executing the `main.py` script:
```bash
    python3 main.py
```

## Usage

Once you run `main.py`, a graphical window will open. The steps to use the application are as follows:

1. **Enter Starting Axiom**: In the provided entry widget, input the starting axiom for the L-System. This should be a string composed of letters or symbols. This will be the base structure of the fractal. The generator will iterate through this string to create the fractal.
2. **Define Rules**: Click the "Add Rules" button to create new rules widgets. Each rule should consist of a one letter name, followed by an equals sign, and then the rewriting rule. E.g., `F=F+F--F+F` (This is the rewriting rule for a Koch curve fractal, the starting axiom would be `F`). While iterating through the axiom, if the generator sees a letter that corresponds to a rule, it will replace that letter with its corresponding rule for the next generation.
   1. You can add multiple rules as needed.
4. **Set Starting Variables**: Adjust the initial parameters for the system, such as line length, turn angle, and line width. These values must be integers or floats. A float must be preceded by an integer (e.g., `0.5` works but not `.5`)
5. **Generate L-System**: Once all inputs are set, the L-System will be drawn using Turtle graphics. You can step through each generation of the system to observe how it evolves over time.
6. **Step Through Generations**: Click the space key on your keyboard to step forward to the next generation/iteration of your system

### Note:
- For the **starting string** and **rule entry widgets**, only letters are allowed. Numbers cannot be entered.

## Features

- **Customizable Rules**: Define your own rules for generating the L-System.
- **Interactive GUI**: Input axioms, rules, and variables through an intuitive user interface built with Tkinter.
- **Turtle Visualizations**: Watch the L-System evolve step-by-step with each generation rendered using Turtle graphics.
- **Input Validation**: Entry widgets are restricted to ensure only valid inputs are provided.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Author

This project is maintained by [Electric Stove](https://github.com/electricStove).
