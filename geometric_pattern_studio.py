
import turtle
import easygui

# Function to draw a square
def draw_square(pen, size):
    for i in range(4):
        pen.forward(size)
        pen.left(90)


# Function to draw an equilateral triangle
def draw_triangle(pen, size):
    for i in range(3):
        pen.forward(size)
        pen.left(120)


# Function to draw a circle
def draw_circle(pen, size):
    pen.circle(size)


# Function to draw a custom five-pointed star
def draw_star(pen, size):
    for i in range(5):
        pen.forward(size)
        pen.right(144)


# Display graphical menu
shape = easygui.buttonbox(
    "Welcome to Geometric Pattern Studio!\nChoose a shape to draw:",
    "Geometric Pattern Studio",
    choices=[
        "Square",
        "Equilateral Triangle",
        "Circle",
        "Custom Star"
    ]
)

# Exit if the user closes the menu
if shape is None:
    raise SystemExit

# Take dimension input between 50 and 250
size = easygui.integerbox(
    "Enter the side length or radius (50 to 250):",
    "Shape Dimensions",
    lowerbound=50,
    upperbound=250
)

if size is None:
    raise SystemExit

# Select a color
color = easygui.choicebox(
    "Choose a color for your shape:",
    "Select Color",
    choices=["blue", "red", "yellow"]
)

if color is None:
    raise SystemExit

# Create the turtle drawing canvas
screen = turtle.Screen()
screen.setup(width=700, height=600)
screen.title("Geometric Pattern Studio")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(5)
pen.pensize(3)
pen.color(color)
pen.penup()

# Position the turtle to keep the drawing near the center
if shape == "Square":
    pen.goto(-size / 2, -size / 2)
elif shape == "Equilateral Triangle":
    pen.goto(-size / 2, -size / 3)
elif shape == "Circle":
    pen.goto(0, -size / 2)
elif shape == "Custom Star":
    pen.goto(-size / 2, 0)

pen.pendown()

# Call the appropriate drawing function
if shape == "Square":
    draw_square(pen, size)
elif shape == "Equilateral Triangle":
    draw_triangle(pen, size)
elif shape == "Circle":
    draw_circle(pen, size)
elif shape == "Custom Star":
    draw_star(pen, size)

# Display the completed drawing
screen.update()

# Show completion message
easygui.msgbox(
    f"Your {shape.lower()} has been drawn successfully!",
    "Drawing Complete"
)

# Close the turtle window safely
turtle.bye()
