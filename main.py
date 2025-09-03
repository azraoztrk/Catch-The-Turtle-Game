import turtle
import random

screen=turtle.Screen()
screen.bgcolor("light pink")
screen.title("Catch The Turtle")
FONT=('Arial', 30, 'normal')
game_over = False
score=0
turtle_list=[]

count_down_turtle = turtle.Turtle()

turtle_instance = turtle.Turtle()

def score_arrangement():
    turtle_instance.hideturtle()
    turtle_instance.penup()
    screen_height = (screen.window_height() / 2) - 40
    turtle_instance.goto(0, screen_height)
    turtle_instance.write('Score: 0', move=False, align='center', font=FONT)

grid_size = 10

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        turtle_instance.clear()
        turtle_instance.write("Score: {}".format(score), move=False, align="center", font=FONT)
        print(x, y)

    t.onclick(handle_click)
    t.penup()
    t.color("dark green")
    t.shape("turtle")
    t.shapesize(2, 2)
    t.goto(x * grid_size, y * grid_size)
    t.pendown()
    turtle_list.append(t)

x_coordinates=[-20, -10, 0, 10 ,20]
y_coordinates=[20, 10, 0, -10]

def setup_turtle():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, y - 30)
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write("Time: {}".format(time),move=False,align="center",font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write("Game Over!", align='center', font=FONT)

def start_game_up():
    global game_over
    game_over = False
    screen.tracer(0)
    score_arrangement()
    setup_turtle()
    hide_turtles()
    show_turtles_randomly()
    screen.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game_up()
turtle.mainloop()