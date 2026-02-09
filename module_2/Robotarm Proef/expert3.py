from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:
def stopwanneerklaar():
    if robotArm._solutionDone:
        robotArm.report()
        robotArm.help()
        exit()
robotArm.speed = 2
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
stopwanneerklaar()

for i in range(1):
    robotArm.moveLeft()
    robotArm.grab()

for t in range(2):
    robotArm.moveRight()
robotArm.drop()
stopwanneerklaar()
for u in range(1):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()

for o in range(3):
    robotArm.moveRight()
robotArm.drop()
stopwanneerklaar()

for x in range(3):
    robotArm.moveLeft()
robotArm.grab()

for o in range(4):
    robotArm.moveRight()
robotArm.drop()
stopwanneerklaar()

for x in range(4):
    robotArm.moveLeft()
robotArm.grab()

for o in range(5):
    robotArm.moveRight()
robotArm.drop()
stopwanneerklaar()

for x in range(5):
    robotArm.moveLeft()
robotArm.grab()
for o in range(6):
    robotArm.moveRight()
robotArm.drop()
stopwanneerklaar()

for x in range(6):
    robotArm.moveLeft()
robotArm.grab()
for o in range(7):
    robotArm.moveRight()
robotArm.drop()
stopwanneerklaar()
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

