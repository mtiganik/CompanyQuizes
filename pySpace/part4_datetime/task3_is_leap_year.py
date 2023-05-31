def is_leap_year(year):
    return True if year%400==0 or(year%100!=0 and year%4==0) else False 

assert is_leap_year(2016) == True
assert is_leap_year(2023) == False
assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(4000) == True
assert is_leap_year(4100) == False
assert is_leap_year(4001) == False
assert is_leap_year(4004) == True

print("EndofProgram")