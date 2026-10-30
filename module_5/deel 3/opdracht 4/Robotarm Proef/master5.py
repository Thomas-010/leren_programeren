from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.master import challenges

# load the robotarm with a challenge on a level (max 3)
robotarm = RobotArm(challenges[5],0)

# your code starts here:
color = []

for i in range(10):
    robotarm.grab()
    color.append(robotarm.scan())
    robotarm.drop()
    if i < 9:
        robotarm.moveRight()

dubbelkleur = next(kleur for kleur in color if color.count(kleur) == 2)
plekken = [i for i, kleur in enumerate(color) if kleur == dubbelkleur]

for _ in range(9 - plekken[1]):
    robotarm.moveLeft()

robotarm.grab()

for _ in range(plekken[1] - plekken[0]):
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
