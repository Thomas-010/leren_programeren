from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotarm = RobotArm(challenges[4],0)

# your code starts here:
kleuren = []

for stapel in range(4):
    robotarm.grab()
    kleuren.append(robotarm.scan())

    robotarm.moveRight()
    for stap in range(stapel):
        robotarm.moveRight()
    robotarm.drop()

    for stap in range(stapel + 1):
        robotarm.moveLeft()

for stapel in range(3, -1, -1):
    for stap in range(stapel + 1):
        robotarm.moveRight()
    robotarm.grab()

    for stap in range(stapel + 1):
        robotarm.moveLeft()
    robotarm.drop()

losseKleuren = []
for stapel in range(4):
    while robotarm.stackIndex() < 6 + stapel:
        robotarm.moveRight()

    robotarm.grab()
    losseKleuren.append(robotarm.scan())
    robotarm.drop()

    while robotarm.stackIndex() > 0:
        robotarm.moveLeft()

for kleur in reversed(kleuren):
    bronStapel = 6 + losseKleuren.index(kleur)

    while robotarm.stackIndex() < bronStapel:
        robotarm.moveRight()
    while robotarm.stackIndex() > bronStapel:
        robotarm.moveLeft()

    robotarm.grab()

    while robotarm.stackIndex() > 1:
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
