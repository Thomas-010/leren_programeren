from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotarm = RobotArm(challenges[5],0)

# your code starts here:
kleuren = []

for stapel in range(10):
    robotarm.grab()
    kleuren.append(robotarm.scan())
    robotarm.drop()
    if stapel < 9:
        robotarm.moveRight()

dubbeleKleur = None
for kleur in kleuren:
    if kleuren.count(kleur) == 2:
        dubbeleKleur = kleur
        
eerstePlek = None
tweedePlek = None
for stapel in range(10):
    if kleuren[stapel] == dubbeleKleur:
        if eerstePlek is None:
            eerstePlek = stapel
        else:
            tweedePlek = stapel

for stapel in range(9):
    robotarm.moveLeft()

for stapel in range(tweedePlek):
    robotarm.moveRight()
robotarm.grab()

for stap in range(tweedePlek - eerstePlek):
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
