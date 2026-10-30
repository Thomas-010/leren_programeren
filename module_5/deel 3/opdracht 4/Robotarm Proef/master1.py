from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here:
colors = []

for stack in range(10):
    robotArm.grab()
    colors.append(robotArm.scan())
    robotArm.drop()
    if stack < 9:
        robotArm.moveRight()

differentStack = next(
    index for index, color in enumerate(colors)
    if colors.count(color) == 1
)

for _ in range(9 - differentStack):
    robotArm.moveLeft()

robotArm.grab()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()
