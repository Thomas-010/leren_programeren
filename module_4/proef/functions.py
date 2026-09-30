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
    return [investor for investor in investors if investor['profitReturn'] <= 10]


def getAdventuringInvestors(investors:list) -> list:
    interestingInvestors = getInterestingInvestors(investors)
    return getFromListByKeyIs(interestingInvestors, 'adventuring', True)

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    adventuringInvestors = getAdventuringInvestors(investors)
    count = len(adventuringInvestors)

    if count == 0 or len(gear) == 0:
        return 0.0

    foodCostPerInvestor = getJourneyFoodCostsInGold(1, 1)
    rentalCostPerInvestor = getTotalRentalCost(1, 1)
    gearCostPerInvestor = getItemsValueInGold(gear)

    totalPerInvestor = foodCostPerInvestor + rentalCostPerInvestor + gearCostPerInvestor
    return round(totalPerInvestor * count, 2)

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    costPerNight = getJourneyInnCostsInGold(1, people, horses)

    if costPerNight <= 0:
        return 0

    maxAffordable = math.floor(leftoverGold / costPerNight)
    maxAvailableNights = JOURNEY_IN_DAYS - 1

    return max(0, min(maxAffordable, maxAvailableNights))


def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    silverCost = people * COST_INN_HUMAN_SILVER_PER_NIGHT
    copperCost = horses * COST_INN_HORSE_COPPER_PER_NIGHT
    costPerNight = silver2gold(silverCost) + copper2gold(copperCost)
    return round(costPerNight * nightsInInn, 2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    interestingInvestors = getInterestingInvestors(investors)
    return [round(profitGold * investor['profitReturn'] / 100, 2) for investor in interestingInvestors]

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    if fellowship <= 0:
        return 0.0

    leftoverGold = profitGold - sum(investorsCuts)
    leftoverGold = max(0.0, leftoverGold)

    return round(leftoverGold / fellowship, 2)

##################### O14 #####################

def getEarnings(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    startGold = getPersonCashInGold(mainCharacter['cash'])

    adventuringFriends = getAdventuringFriends(friends)
    adventuringInvestors = getAdventuringInvestors(investors)
    fellowshipSize = 1 + len(adventuringFriends) + len(adventuringInvestors)

    investorsCuts = getInvestorsCuts(profitGold, investors)
    adventurerCut = getAdventurerCut(profitGold, investorsCuts, fellowshipSize)

    giftGold = len(adventuringFriends) * 10
    endGold = round(startGold + adventurerCut + giftGold, 2)

    return [{'name': mainCharacter['name'], 'start': startGold, 'end': endGold}]

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
