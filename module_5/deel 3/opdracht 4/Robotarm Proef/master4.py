from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotarm = RobotArm(challenges[4],0)

# your code starts here:
color = []

for i in range(4):
    robotarm.grab()
    color.append(robotarm.scan())
    robotarm.moveRight()
    for _ in range(i):
        robotarm.moveRight()
    robotarm.drop()
    for _ in range(1 + i):
        robotarm.moveLeft()

for i in range(3, -1, -1):
    for _ in range(1 + i):
        robotarm.moveRight()
    robotarm.grab()
    for _ in range(1 + i):
        robotarm.moveLeft()
    robotarm.drop()

losse_kleuren = []
for i in range(4):
    while robotarm.stackIndex() < 6 + i:
        robotarm.moveRight()
    robotarm.grab()
    losse_kleuren.append(robotarm.scan())
    robotarm.drop()
    while robotarm.stackIndex() > 0:
        robotarm.moveLeft()

for color in reversed(color):
    bronstapel = 6 + losse_kleuren.index(color)
    while robotarm.stackIndex() < bronstapel:
        robotarm.moveRight()
    while robotarm.stackIndex() > bronstapel:
        robotarm.moveLeft()
    robotarm.grab()
    while robotarm.stackIndex() > 1:
        robotarm.moveLeft()
    robotarm.drop()

# your code ends here

# report the results of the mission
robotarm.report()

# want help? Unlock code below!
robotarm.help()

# want to inspect a solution? Unlock code below!
# robotarm.showSolution()
# robotarm.wait()
