from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here:

def PakblokenScan():
    robotArm.grab()
    return robotArm.scan()



for i in range(robotArm._maxStacks):
    if robotArm.stackEmpty():
        robotArm.moveRight()
        continue

    start_index = robotArm.stackIndex()
    robotArm.grab()
    kleur = robotArm.scan()

    if kleur == 'red':
        while robotArm.stackIndex() < robotArm._maxStacks - 1:
            robotArm.moveRight()
        robotArm.drop()
        while robotArm.stackIndex() > start_index:
            robotArm.moveLeft()
        robotArm.moveRight()
    else:
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

