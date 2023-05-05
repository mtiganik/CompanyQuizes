from operator import itemgetter
def pokervalue(cards):
    if straightFlush(cards):
        return 'straight flush'
    if fourKind(cards):
        return 'four of a kind'
    if fullHouse(cards):
        return 'full house'
    if flush(cards):
        return 'flush'
    if straight(cards):
        return 'straight'
    if threeOfKind(cards):
        return 'three of a kind'
    if twoPair(cards):
        return 'two pair'
    if onePair(cards):
        return 'one pair'
    return 'high card'

def straightFlush(cards):
    return False
def fourKind(cards): return False
def fullHouse(cards): return False
def flush(cards): return False

# 10 9 8 7 6
def straight(cards): 
    # Sort the cards by value
    sorted_cards = sorted(cards, key=lambda x: x['value'])
    # Check if the values are consecutive
    for i in range(3):
        straightCnt = 0
        for i in range(5):
            if sorted_cards[i]['value'] != sorted_cards[i+1]['value']-1:
                # If two consecutive values are not consecutive, return False
                return False
        if straightCnt == 5: return True
        
    # If all values are consecutive, return True
    return True

def threeOfKind(cards): return False
def twoPair(cards): return False
def onePair(cards): return False

cards = [
    {'suit': 'diamonds', 'value': 9},
    {'suit': 'clubs', 'value': 2},
    {'suit': 'hearts', 'value': 9},
    {'suit': 'hearts', 'value': 12},
    {'suit': 'spades', 'value': 9},
    {'suit': 'spades', 'value': 6},
    {'suit': 'spades', 'value': 3},
]

print(pokervalue(cards))