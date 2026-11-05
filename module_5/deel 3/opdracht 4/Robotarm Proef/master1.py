from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotarm = RobotArm(challenges[1],0)

# your code starts here:
kleuren = []

for stapel in range(10):
    robotarm.grab()
    kleuren.append(robotarm.scan())
    robotarm.drop()
    if stapel < 9:
        robotarm.moveRight()

afwijkendeKleur = None
afwijkendePlek = None

for plek in range(10):
    kleur = kleuren[plek]
    if kleuren.count(kleur) == 1:
        afwijkendeKleur = kleur
        afwijkendePlek = plek
        break

for stapel in range(9 - afwijkendePlek):
    robotarm.moveLeft()

robotarm.grab()

# your code ends here

# report the results of the mission
robotarm.report()

# want help? Unlock code below!
robotarm.help()

# want to inspect a solution? Unlock code below!
# robotarm.showSolution()
# robotarm.wait()
