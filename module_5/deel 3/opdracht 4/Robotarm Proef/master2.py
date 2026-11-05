from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotarm = RobotArm(challenges[2],0)

# your code starts here:
kleuren = []

for stapel in range(4):
    robotarm.moveRight()

for stapel in range(6):
    robotarm.grab()
    kleuren.append(robotarm.scan())
    robotarm.drop()
    if stapel < 5:
        robotarm.moveRight()

for stapel in range(9):
    robotarm.moveLeft()

geordendeKleuren = sorted(set(kleuren), key=kleuren.count, reverse=True)

for bestemming in range(3):
    for bron in range(6):
        if kleuren[bron] == geordendeKleuren[bestemming]:
            for stap in range(4 + bron):
                robotarm.moveRight()
            robotarm.grab()

            for stap in range(4 + bron - bestemming):
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
