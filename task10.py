
'''
10. Maximum qiymatni topish
Shart: Foydalanuvchi tomonidan kiritilgan 7 ta sondan maximal qiymatni toping.

Input                   Output
1, 2, 3, 5, 9, 4, 2     9
'''

numbers = input("Son kiriting (masalan: 1, 2, 3, 5, 9, 4, 2): ")

num = []
for i in numbers:
    if i.isdigit():
        num.append(i)

print(max(num))