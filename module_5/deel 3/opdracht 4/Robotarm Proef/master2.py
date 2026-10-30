from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:
colors = []

for i in range(4):
    robotArm.moveRight()

for d in range(6):
    robotArm.grab()
    colors.append(robotArm.scan())
    robotArm.drop()
    if robotArm.stackIndex() < 9:
        robotArm.moveRight()

orderedColors = sorted(set(colors), key=colors.count, reverse=True)

for i in range(9):
    robotArm.moveLeft()

for destination, color in enumerate(orderedColors):
    for source in range(4, 10):
        if colors[source - 4] == color:
            while robotArm.stackIndex() < source:
                robotArm.moveRight()
            while robotArm.stackIndex() > source:
                robotArm.moveLeft()

            robotArm.grab()

            while robotArm.stackIndex() > destination:
                robotArm.moveLeft()

            robotArm.drop()


# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()
