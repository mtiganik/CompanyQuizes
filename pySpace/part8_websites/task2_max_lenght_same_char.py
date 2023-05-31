def longest_repeated_seq(word):
    w = word.lower()
    d, curr = 0,0
    for i in range(0,len(w)-1): 
        if w[i] == w[i+1]: curr += 1
        else:
            if curr > d: d = curr
            curr = 0
    return 0 if max(d,curr) == 0 else max(d,curr) +1

assert longest_repeated_seq('hopPlaaaa') == 4
assert longest_repeated_seq('hzzzZZlcccc')  == 5
assert longest_repeated_seq('hzdlc5') == 0 

