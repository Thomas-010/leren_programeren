from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here:

for i in range(3):
    robotArm.moveRight()

robotArm.grab()

for t in range(5):
    robotArm.moveRight()
    
robotArm.drop()
for u in range(5):
    robotArm.moveLeft()

robotArm.grab()

for o in range(5):
    robotArm.moveRight()

robotArm.drop()

for x in range(5):
    robotArm.moveLeft()
robotArm.grab()

for o in range(5):
    robotArm.moveRight()

robotArm.drop()

for x in range(5):
    robotArm.moveLeft()
robotArm.grab()

for o in range(5):
    robotArm.moveRight()
robotArm.drop()

for x in range(6):
    robotArm.moveLeft()
robotArm.grab()
for o in range(5):
    robotArm.moveRight()
robotArm.drop()
for x in range(5):
    robotArm.moveLeft()
robotArm.grab()
for o in range(5):
    robotArm.moveRight()
robotArm.drop()
for x in range(5):
    robotArm.moveLeft()
robotArm.grab()
for o in range(5):
    robotArm.moveRight()
robotArm.drop()
for x in range(6):
    robotArm.moveLeft()
robotArm.grab()
for o in range(5):
    robotArm.moveRight()
robotArm.drop()
for x in range(5):
    robotArm.moveLeft()
robotArm.grab()
for o in range(5):
    robotArm.moveRight()
robotArm.drop()
for x in range(6):
    robotArm.moveLeft()
robotArm.grab()
for o in range(5):
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

