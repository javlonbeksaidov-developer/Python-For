
'''
9. Minimal qiymatni topish
Shart: Foydalanuvchi tomonidan kiritilgan 7 ta sondan minimal qiymatni toping.

Input                   Output
1, 2, 3, 5, 9, 4, 2     1
'''

first_num = int(input("Son kiriting: "))
min_number = first_num

for i in range(6):
    son = int(input("Son kiriting: "))
    if son < min_number:
        min_number = son
        
print(min_number)
        