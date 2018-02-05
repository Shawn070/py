from math import pi, sin, cos, radians

def getInputs():
    a = eval(input("Enter the launch angle (in degrees):"))
    v = eval(input("Enter the initial velocity (in meters/sec):"))
    h = eval(input("Enter the initial height (in meters):"))
    t = eval(input("Enter the time inerval:"))
    return a, v, h, t

def getXYComponets(vel, angle):
    theta = radians(angle)
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    return xvel, yvel

def updatePosition(time, xpos, ypos, xvel, yvel):
    xpos = xpos + time * xvel
    yvel1 = yvel - time * 9.8
    ypos = ypos + time * (yvel + yvel1)/2.0
    yvel = yvel1
    return xpos, ypos, yvel    

def main():
    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponets(vel, angle)
    while ypos >= 0:
        xpos, ypos, yvel = updatePosition(time, xpos, ypos, xvel, yvel)
    print("\nDistance traveled:{0:0.1f}meters.".format(xpos))

main()