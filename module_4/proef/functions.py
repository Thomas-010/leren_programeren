import time
from termcolor import colored
from config import *
import math

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10
    
def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    totalGold = (
        copper2gold(personCash.get('copper', 0))
        + silver2gold(personCash.get('silver', 0))
        + personCash.get('gold', 0)
        + platinum2gold(personCash.get('platinum', 0))
    )
    return round(totalGold, 2)

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    totalCopperPerDay = (people * COST_FOOD_HUMAN_COPPER_PER_DAY) + (horses * COST_FOOD_HORSE_COPPER_PER_DAY)
    totalCopper = totalCopperPerDay * JOURNEY_IN_DAYS
    return round(copper2gold(totalCopper), 2)
##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    result = []
    for item in list:
        if item.get(key) == value:
            result.append(item)
    return result

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    sharedFriends = getShareWithFriends(friends)
    return getAdventuringPeople(sharedFriends)

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    weeksNeeded = math.ceil(JOURNEY_IN_DAYS / 7)
    horseCostInGold = silver2gold(horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS)
    tentCostInGold = tents * COST_TENT_GOLD_PER_WEEK * weeksNeeded
    return round(horseCostInGold + tentCostInGold, 2)
##################### O08 #####################

def getItemsAsText(items:list) -> str:
    tekst = [f"{item['amount']}{item['unit']} {item['name']}" for item in items]
    if len(tekst) == 0:
        return ''
    if len(tekst) == 1:
        return tekst[0]
    return ', '.join(tekst[:-1]) + ' & ' + tekst[-1]

def getItemsValueInGold(items:list) -> float:
    total = 0.0
    for item in items:
        priceAmount = item['price']['amount']
        priceType = item['price']['type']
        itemTotal = item['amount'] * priceAmount

        if priceType == 'copper':
            itemTotal = copper2gold(itemTotal)
        elif priceType == 'silver':
            itemTotal = silver2gold(itemTotal)
        elif priceType == 'platinum':
            itemTotal = platinum2gold(itemTotal)

        total += itemTotal
    return round(total, 2)

      

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total = 0.0
    for person in people:
        total += getPersonCashInGold(person['cash'])
    return round(total, 2)

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()