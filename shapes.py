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
    if pattern == "square":
        draw_square(t, size)
    elif pattern == "circle":
        draw_circle(t, size)
    elif pattern == "star":
        draw_star(t, size)
    elif pattern == "hexagon":
        draw_hexagon(t, size)
    elif pattern == "triangle":
        draw_triangle(t, size)
    elif pattern == "spiral":
        angle = int(turtle.numinput("Angle Input", "Enter angle for spiral: ", minval=10, maxval=360))
        draw_spiral(t, size, angle)

def draw_mandala(t, num_shapes, size):
    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan"]
    for i in range(num_shapes):
        t.color(random.choice(colors))
        draw_circle(t, size)
        t.right(360 / num_shapes)

def draw_flower(t, petal_count, petal_size):
    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan"]
    for _ in range(petal_count):
        t.color(random.choice(colors))
        t.circle(petal_size, 60)
        t.left(120)
        t.circle(petal_size, 60)
        t.left(60)

def draw_sunburst(t, ray_count, ray_length):
    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan"]
    for _ in range(ray_count):
        t.color(random.choice(colors))
        t.forward(ray_length)
        t.backward(ray_length)
        t.right(360 / ray_count)

def draw_sine_wave(t, amplitude, frequency, length):
    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan"]
    t.color(random.choice(colors))
    for x in range(length):
        y = amplitude * turtle.sin(frequency * x)
        t.goto(x - length // 2, y)

def draw_complex_pattern(t):
    draw_random_pattern(t, 5)
    user_input_pattern(t)
    draw_mandala(t, 12, 50)
    draw_flower(t, 8, 100)
    draw_sunburst(t, 20, 150)
    draw_sine_wave(t, 100, 0.1, 500)

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    return t

def draw_grid(t, step):
    t.color("gray")
    for x in range(-200, 201, step):
        t.penup()
        t.goto(x, -200)
        t.pendown()
        t.goto(x, 200)
    for y in range(-200, 201, step):
        t.penup()
        t.goto(-200, y)
        t.pendown()
        t.goto(200, y)

def draw_random_lines(t, num_lines):
    for _ in range(num_lines):
        x1 = random.randint(-200, 200)
        y1 = random.randint(-200, 200)
        x2 = random.randint(-200, 200)
        y2 = random.randint(-200, 200)
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

def draw_concentric_circles(t, num_circles, radius_step):
    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan"]
    for i in range(num_circles):
        t.color(random.choice(colors))
        draw_circle(t, radius_step * i)

def draw_rainbow(t, radius):
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in colors:
        t.color(color)
        t.begin_fill()
        draw_circle(t, radius)
        t.end_fill()
        radius -= 10

def draw_lsystem(t, axiom, rules, iterations, angle, length):
    stack = []
    for _ in range(iterations):
        new_axiom = ""
        for char in axiom:
            new_axiom += rules.get(char, char)
        axiom = new_axiom
    for char in axiom:
        if char == "F":
            t.forward(length)
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)

elif char == "[":
            stack.append((t.position(), t.heading()))
        elif char == "]":
            position, heading = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()

def draw_tree(t, branch_length, level):
    if level > 0:
        t.forward(branch_length)
        t.right(20)
        draw_tree(t, branch_length - 10, level - 1)
        t.left(40)
        draw_tree(t, branch_length - 10, level - 1)
        t.right(20)
        t.backward(branch_length)

def draw_koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_snowflake(t, length, level-1)
        t.left(60)
        draw_koch_snowflake(t, length, level-1)
        t.right(120)
        draw_koch_snowflake(t, length, level-1)
        t.left(60)
        draw_koch_snowflake(t, length, level-1)

def draw_fractal_tree(t, branch_length, angle, level):
    if level > 0:
        t.forward(branch_length)
        t.left(angle)
        draw_fractal_tree(t, branch_length * 0.67, angle, level - 1)
        t.right(angle * 2)
        draw_fractal_tree(t, branch_length * 0.67, angle, level - 1)
        t.left(angle)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Colorful Turtle Patterns")


    t = setup_turtle()

    num_squares = 36
    size_increment = 10

    for _ in range(5):
        draw_pattern(t, num_squares, size_increment)
        t.right(10)

    draw_grid(t, 50)
    draw_random_lines(t, 10)
    draw_concentric_circles(t, 10, 20)
    draw_rainbow(t, 100)

    axiom = "F"
    rules = {"F": "F+F-F-F+F"}
    draw_lsystem(t, axiom, rules, 4, 90, 5)

    draw_tree(t, 100, 5)
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    draw_koch_snowflake(t, 300, 4)

    t.penup()
    t.goto(150, -200)
    t.pendown()
    draw_fractal_tree(t, 100, 30, 5)

    draw_complex_pattern(t)

    turtle.done()

if __name__ == "__main__":
    main()

