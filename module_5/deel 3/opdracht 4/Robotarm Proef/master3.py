from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:
colors = []
destinations = [0, 1, 8, 9]

for i in range(3, 7):
    while robotArm.stackIndex() < i:
        robotArm.moveRight()
    while robotArm.stackIndex() > i:
        robotArm.moveLeft()

    while not robotArm.stackEmpty():
        robotArm.grab()
        color = robotArm.scan()

        if color not in colors:
            colors.append(color)

        destination = destinations[colors.index(color)]

        while robotArm.stackIndex() < destination:
            robotArm.moveRight()
        while robotArm.stackIndex() > destination:
            robotArm.moveLeft()

        robotArm.drop()

        while robotArm.stackIndex() < i:
            robotArm.moveRight()
        while robotArm.stackIndex() > i:
            robotArm.moveLeft()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()
