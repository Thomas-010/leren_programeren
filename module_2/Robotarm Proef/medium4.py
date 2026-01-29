from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
robotArm.grab()
for y in range(4):
    for x in range(2):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(2):
        robotArm.moveLeft()
    robotArm.grab()

for t in range(2):
    robotArm.moveRight() 

for l in range(5):
    
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()



# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()