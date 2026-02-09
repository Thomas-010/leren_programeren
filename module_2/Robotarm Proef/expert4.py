from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
robotArm.speed = 2

for i in range(7):
    for blok in range(6):
        if robotArm.stackEmpty():
            break
        robotArm.grab()
        kleur = robotArm.scan()
        
        if kleur == 'red':
            for stap in range(7 - robotArm.stackIndex()):
                robotArm.moveRight()
        elif kleur == 'green':
            for stap in range(8 - robotArm.stackIndex()):
                robotArm.moveRight()
        elif kleur == 'blue':
            for stap in range(9 - robotArm.stackIndex()):
                robotArm.moveRight()
        
        robotArm.drop()
        
        for stap in range(robotArm.stackIndex() - i):
            robotArm.moveLeft()
    
    if i < 6:
        robotArm.moveRight()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()

