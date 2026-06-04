
'''
12. Juft va toq sonlarning yig‘indisini alohida hisoblash
Shart: 1 dan boshlab foydalanuvchi tomonidan kiritilgan n soniga qadar bo‘lgan juft
va toq sonlarning yig‘indisini alohida hisoblang.

Input   Output
6       12, 9
'''

stop = int(input("Sonni kiriting: "))

toq = 0
for i in range(1, stop + 1, 2):
    toq += i

juft = 0  
for i in range(2, stop + 1, 2):
    juft += i

print(toq, juft)
    