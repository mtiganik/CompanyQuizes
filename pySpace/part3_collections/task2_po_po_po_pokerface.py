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


def threeOfKind(cards): return False
def twoPair(cards): return False
def onePair(cards): return False

cards = [
    {'suit': 'hearts', 'value': 2},
    {'suit': 'hearts', 'value': 1},
    {'suit': 'hearts', 'value': 12},
    {'suit': 'hearts', 'value': 9},
    {'suit': 'hearts', 'value': 6},
    {'suit': 'diamonds', 'value': 1},
    {'suit': 'diamonds', 'value': 2},
    {'suit': 'diamonds', 'value': 3},
    {'suit': 'clubs', 'value': 13},
    {'suit': 'spades', 'value': 6},
    {'suit': 'spades', 'value': 2},
    {'suit': 'spades', 'value': 3},
    {'suit': 'spades', 'value': 4},
    {'suit': 'spades', 'value': 5},
]
sorting = [
    {'suit':'hearts', 'toMove':0},
    {'suit':'diamonds', 'toMove': 16},
    {'suit':'clubs', 'toMove': 32},
    {'suit':'spades', 'toMove':48}
    ]

def getDeck(cards):
    currVal = 0
    for sort in sorting:
        for card in cards:
            if card['suit']==sort['suit']:
                currVal += 1 << (sort['toMove'] + card['value'])
    return currVal

#suit: hearts, 1-Diamonds, 2-Clubs, 3-Spades
def getOneTypeCards(deck, suit):
    return (deck >> suit*16) & 65535

def getOneTypeAsList(deck):
    list = []
    for i in range(0,4):
        list.append((deck >> i*16) & 65535)
    return list

def flushCheck(deck):
    list = getOneTypeAsList(deck)
    for i in list:
        if bin(i).count('1') == 5:
            return True
    return False
deck = getDeck(cards)

def straightFlushCheck(deck):
    list = getOneTypeAsList(deck)
    for i in list:
        str = bin(i)
        if "11111" in str or (str[-2:] == '10' and len(str) == 16 and 'b1111' in str):
            return True
    return False

straightFlushCheck(deck)

id = getDeck(cards)
width = 17
bin_num = format(id, '0{}_b'.format(width+3))
print(bin_num)
