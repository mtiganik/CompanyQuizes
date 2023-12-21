def getDeck(cards):
    deck = ['0'*13]*4
    for c in cards:
        suit = c['suit']
        if suit == 'hearts': i = 0
        elif suit == 'diamonds': i=1
        elif suit == 'clubs': i=2
        elif suit == 'spades': i=3
        deck[i] = deck[i][:c['value']-1] + '1' + deck[i][c['value'] :]
    return deck


def NoOfKind(deck,n):
    for i in range(13):
        currCnt = 0
        for j in range(4):
            if deck[j][i] == '1': currCnt += 1
        if currCnt >= n: return True
    return False

def NoOfKindExclude(deck,n,exclude):
    for i in range(13):
        if i != exclude:
            currCnt = 0
            for j in range(4):
                if deck[j][i] == '1': currCnt += 1
            if currCnt >= n: return i
    return -1

def TwoPair(deck):
    two = NoOfKindExclude(deck,2,-1)
    if two == -1: return False
    if NoOfKindExclude(deck,2,two) != -1: return True
    return False


def FullHouse(deck):
    three = NoOfKindExclude(deck,3,-1)
    if three == -1: return False
    if NoOfKindExclude(deck,2,three) != -1: return True
    return False

def Straigh(deck):
    s = '0'*13
    for i in range(0,13):
        if '1' in [deck[0][i], deck[1][i], deck[2][i], deck[3][i]]:
            s = s[:i] + '1' + s[i + 1:]
    if '11111' in s or (s[0] == '1' and s[-4:] == '1111'): return True
    return False

def Flush(deck):
    for x in deck:
        if x.count('1') >= 5: return True
    return False

def straightFlushCheck(deck):
    for x in deck:
        if "11111" in x or (x[0] == '1' and x[-4:]=='1111'):
            return True
    return False



def pokervalue(cards):
    deck = getDeck(cards)
    if straightFlushCheck(deck):
        return 'straight flush'
    if NoOfKind(deck,4):
        return 'four of a kind'
    if FullHouse(deck):
        return 'full house'
    if Flush(deck):
        return 'flush'
    if Straigh(deck):
        return 'straight'
    if NoOfKind(deck,3):
        return 'three of a kind'
    if TwoPair(deck):
        return 'two pair'
    if NoOfKind(deck,2):
        return 'one pair'
    return 'high card'



# sama kaarti võib mitu korda olla. 
cards = [
    {'suit': 'clubs', 'value': 9},
    {'suit': 'hearts', 'value': 11},
    {'suit': 'diamonds', 'value': 11},
    {'suit': 'clubs', 'value': 6},
    {'suit': 'spades', 'value': 2},
    {'suit': 'spades', 'value': 2},
    {'suit': 'spades', 'value': 2},
]

print(pokervalue(cards))

