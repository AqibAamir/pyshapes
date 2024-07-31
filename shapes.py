import turtle
import random

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_circle(t, radius):
    t.circle(radius)

def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

def draw_hexagon(t, size):
    for _ in range(6):
        t.forward(size)
        t.right(60)

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.right(120)

def draw_spiral(t, line_length, angle):
    colors = ["red", "green", "blue", "Orange", "purple", "pink", "yellow", "cyan"]
    for i in range(line_length):
        t.color(random.choice(colors))
        t.forward(i)
        t.right(angle)

def draw_pattern(t, num_squares, size_increment):
    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan"]
    for i in range(num_squares):
        t.color(random.choice(colors))
        draw_square(t, size_increment * i)
        t.right(360 / num_squares)

def draw_random_pattern(t, num_shapes):
    for _ in range(num_shapes):
        shape = random.choice(["square", "circle", "star", "hexagon", "triangle"])
        size = random.randint(20, 100)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t.penup()
        t.goto(x, y)
        t.pendown()
        if shape == "square":
            draw_square(t, size)
        elif shape == "circle":
            draw_circle(t, size)
        elif shape == "star":
            draw_star(t, size)
        elif shape == "hexagon":
            draw_hexagon(t, size)
        elif shape == "triangle":
            draw_triangle(t, size)

def user_input_pattern(t):
    pattern = turtle.textinput("Pattern Input", "Enter pattern (square/circle/star/hexagon/triangle/spiral): ")
    size = int(turtle.numinput("Size Input", "Enter size: ", minval=10, maxval=200))
