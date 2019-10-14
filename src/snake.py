import turtle
import time
import random

delay = 0.1

# Pontok
score = 0
high_score = 0

# Canvas
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake fej
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake kaja
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pontszam
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Pont: 0  Legjobb Pont: 0", align="center", font=("Courier", 24, "normal"))


# iranyok
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# mozgas gombok
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# alap jatek loop
while True:
    wn.update()

    # snake + sarok teszt
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # szegmensek eltuntetese
        for segment in segments:
            segment.goto(1000, 1000)

        # szegmens list torles
        segments.clear()

        # pont reset
        score = 0

        # delay reset
        delay = 0.1

        pen.clear()
        pen.write("Pont: {}  Legjobb Pont: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # kaja + snake teszt
    if head.distance(food) < 20:
        # kaja random
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # szegmens hozzaadasa
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # delay rovidites
        delay -= 0.001

        # +1 pont
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Pont: {}  Legjobb Pont: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # szegmensek mozgasa
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # a szegmenseket a fejhez viszi
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # onmagaba menes tesztelese
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # szegmensek eltuntetese
            for segment in segments:
                segment.goto(1000, 1000)

            # cleareli a szegmensek listajat
            segments.clear()

            # Pont reset
            score = 0

            # delay reset
            delay = 0.1

            # a pontszam frissitise
            pen.clear()
            pen.write("Pont: {}  Legjobb Pont: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()