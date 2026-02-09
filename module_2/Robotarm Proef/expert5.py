from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
def stopwanneerklaar():
    if robotArm._solutionDone:
        exit()

robotArm.speed = 2
robotArm.moveRight()

tellen = {}

for i in range(1, 10):
    for x in range(1):
        if robotArm.stackEmpty():
            break
        robotArm.grab()
        kleur = robotArm.scan()
        tellen[kleur] = tellen.get(kleur, 0) + 1
        robotArm.drop()
        stopwanneerklaar()
    
    if i < 9:
        robotArm.moveRight()

meest_kleur = None
meeste_count = 0
for kleur, count in tellen.items():
    if count > meeste_count:
        meeste_count = count
        meest_kleur = kleur

for i in range(9):
    robotArm.moveLeft()
robotArm.moveRight()

for i in range(1, 10):
    for x in range(8):
        if robotArm.stackEmpty():
            break
        robotArm.grab()
        if robotArm.scan() == meest_kleur:
            for x in range(i):
                robotArm.moveLeft()
            robotArm.drop()
            stopwanneerklaar()
            for x in range(i):
                robotArm.moveRight()
        else:
            robotArm.drop()
            stopwanneerklaar()
            break 
    
    if i < 9:
        robotArm.moveRight()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

