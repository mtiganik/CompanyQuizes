def roman(number):
    if number > 3999: raise Exception("Index out of range") 
    letters,i,res = "IVXLCDMMM",0,""
    while number != 0:
        res = makeDigit(number % 10,letters[i:i+3]) + res
        number = number // 10
        i = i+2
    return res

def makeDigit(num, path):
    d1,d2,d3 = path[0],path[1],path[2]
    if num == 0: return ""
    if num < 4: return d1*num
    if num == 4: return d1 + d2
    if num < 9: return d2 + d1*(num%5)
    else: return d1 + d3

assert roman(39) == "XXXIX"
assert roman(246) == "CCXLVI"
assert roman(789) == "DCCLXXXIX"
assert roman(2421) == "MMCDXXI"
assert roman(160) == "CLX"
assert roman(207) == "CCVII"
assert roman(1009) == "MIX"
assert roman(3999) == "MMMCMXCIX"
assert roman(1776) == "MDCCLXXVI"
assert roman(1918) == "MCMXVIII"
assert roman(1944) == "MCMXLIV"
assert roman(2023) == "MMXXIII"
print(roman(3999))
# assert roman(2023) == "MMXXIII"

print("End of program")