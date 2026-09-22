import sys, os
from test_lib import test, report

# voeg de hoofdmap ('proef') toe aan het systeem pad
basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(basepath)

# importeer de constante uit de config.py file
from config import JOURNEY_IN_DAYS

# TODO: Schrijf hieronder de test van opdracht 4

expected = 11
result = JOURNEY_IN_DAYS
test('Journey takes the correct amount of days', expected, result)



# Niets hieronder aanpassen

if __name__ == "__main__":
    report()