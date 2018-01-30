from turtle import Turtle, mainloop
def tree(plist, l, a, f):
    '''plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened from level to level.'''
    if l > 5:
        lst = []
        for p in plist:
            p.forward(l)    # 沿着当前的方向画画
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst, l*f, a, f)
def maketree(x, y):
    p = Turtle()
    p.color("green")
    p.pensize(5)
    p.setundobuffer(None)
    p.hideturtle()
    # Make the turtle invisible.It's a good idea to do this while
    # you're in the middle of doing some complex drawing,
    # because hiding the turtle speeds up the drawing observably.
    p.speed(10)
    p.getscreen().tracer(30, 0)
    p.left(90)          # Turn turtle left by angle units.
    p.penup()           # Pull the pen up - no drawing when moving
    p.goto(x, y)        # Move turtle to an absolute position.
    # If the pen is down, drawn line.Do not change the turtle's orientation.
    p.pendown()         # Pull the pen down - drawing when moving.

    # t = tree([p], 200, 65, 0.6375)
    t = tree([p], 110, 65, 0.6375)
    print(len(p.getscreen().turtles())) # 用了多少个turtle绘制
def main():
    maketree(-200, -200)
    maketree(0, 0)
    maketree(200, -200)
main()