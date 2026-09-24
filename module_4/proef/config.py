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
COST_FOOD_HUMAN_COPPER_PER_DAY = constants['COST_FOOD_HUMAN_COPPER_PER_DAY']
COST_FOOD_HORSE_COPPER_PER_DAY = constants['COST_FOOD_HORSE_COPPER_PER_DAY']
