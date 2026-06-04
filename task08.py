
'''
8. Sonning kvadratini yig‘ish
Shart: 1 dan N gacha bo‘lgan sonlarning kvadratlarini yig‘ing.

Input   Output
4       30
'''

stop = int(input("Stop: "))

sum = 0
for i in range(1, stop + 1):
    sum += i ** 2
print(sum)