
'''
9. Minimal qiymatni topish
Shart: Foydalanuvchi tomonidan kiritilgan 7 ta sondan minimal qiymatni toping.

Input                   Output
1, 2, 3, 5, 9, 4, 2     1
'''

numbers = input("Son kiriting (masalan: 1, 2, 3, 5, 9, 4, 2): ")

num = []
for i in numbers:
    if i.isdigit():
        num.append(i)

print(min(num))