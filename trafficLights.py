import turtle  # Tess becomes a traffic light.


turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:   # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

# function created to keep automatic repetition apart from the main "advance state" function
def advance_state_machine_auto():
    advance_state_machine()
    wn.ontimer(advance_state_machine_auto, 5000)


def turn_red():
    tess.fillcolor("red")


def turn_green():
    tess.fillcolor("green")


def turn_blue():
    tess.fillcolor("blue")


def turn_size_up():
    temp = tess.pensize()
    if temp < 20:
        tess.pensize(temp + 1)


def turn_size_down():
    temp = tess.pensize()
    if temp > 1:
        tess.pensize(temp - 1)


# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")
wn.onkey(turn_red, "r")
wn.onkey(turn_green, "g")
wn.onkey(turn_blue, "b")
wn.onkey(turn_size_up, "+")
wn.onkey(turn_size_down, "-")

wn.ontimer(advance_state_machine_auto, 2000)
wn.listen()
wn.mainloop()
