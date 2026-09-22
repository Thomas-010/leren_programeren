import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data.json')

with open(FILE_PATH) as f:
    data = json.load(f)

mainCharacter = data['mainCharacter']
friends = data['friends']
adventurerGear = data['adventurerGear']
investors = data['investors']
treasure = data['treasure']

constants = data["constants"]

JOURNEY_IN_DAYS = constants['JOURNEY_IN_DAYS']
