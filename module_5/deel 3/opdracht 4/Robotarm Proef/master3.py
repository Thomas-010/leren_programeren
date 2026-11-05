from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotarm = RobotArm(challenges[3],0)

# your code starts here:
bestemmingen = [0, 1, 8, 9]
kleuren = []

for bron in range(3, 7):
    while robotarm.stackIndex() < bron:
        robotarm.moveRight()
    while robotarm.stackIndex() > bron:
        robotarm.moveLeft()

    while not robotarm.stackEmpty():
        robotarm.grab()
        kleur = robotarm.scan()

        if kleur not in kleuren:
            kleuren.append(kleur)

        bestemming = bestemmingen[kleuren.index(kleur)]

        while robotarm.stackIndex() < bestemming:
            robotarm.moveRight()
        while robotarm.stackIndex() > bestemming:
            robotarm.moveLeft()

        robotarm.drop()

        while robotarm.stackIndex() < bron:
            robotarm.moveRight()
        while robotarm.stackIndex() > bron:
            robotarm.moveLeft()

# your code ends here

# report the results of the mission
robotarm.report()

# want help? Unlock code below!
robotarm.help()

# want to inspect a solution? Unlock code below!
# robotarm.showSolution()
# robotarm.wait()
