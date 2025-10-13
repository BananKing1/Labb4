"""
Modify the cannonball simulation (see book p. 318) so that it also calculates the maximum height
achieved by the cannonball.
"""

from math import sin, cos, radians

def main():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the initial velocity (in meters/sec: "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))

	# convert angle to radians
    theta = radians(angle)

	# set the initial position and velocities in x and y directions
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    max_height = ypos
        
	# loop until the ball hits the ground
    while ypos >= 0.0:
	# calculate position and velocity in time seconds
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1) / 2.0
        yvel = yvel1

	# Max height, while-loop updates ypos and is statement checks for new max_height
        if ypos > max_height:
            max_height = ypos


    print("\nDinstance traveled: {0:0.1f} meters".format(xpos))
    print("max height:", max_height)

    
main()
