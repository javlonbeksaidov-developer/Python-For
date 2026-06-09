
'''
14. Sinfdagi talabalarning o‘rtacha yoshini hisoblash
Shart: Sinfdagi 5 ta talabalarning yoshini kiriting. Ularning o‘rtacha yoshini toping.
Input                   Output
20, 21, 22, 20, 23      21.2
'''

total = 0

for i in range(5):
    yosh = int(input("Talabaning yoshini kiriting: "))
    total += yosh

result = total / 5
print(result)