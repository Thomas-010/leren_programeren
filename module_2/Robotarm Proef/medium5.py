from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
for i in range(4):
    robotArm.moveRight()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for o in range(2):
    robotArm.moveLeft()

robotArm.grab()
for p in range(3):
    robotArm.moveRight()
robotArm.drop()

for f in range(4):
    robotArm.moveLeft()
robotArm.grab()

for g in range(5):
    robotArm.moveRight()
robotArm.drop()

for h in range(6):
    robotArm.moveLeft()
robotArm.grab()

for j in range(7):
    robotArm.moveRight()
robotArm.drop()

for t in range(8):
    robotArm.moveLeft()
robotArm.grab()

for q in range (9):
    robotArm.moveRight()
robotArm.drop()
# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()