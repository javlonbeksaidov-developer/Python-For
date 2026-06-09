
'''
10. Maximum qiymatni topish
Shart: Foydalanuvchi tomonidan kiritilgan 7 ta sondan maximal qiymatni toping.

Input                   Output
1, 2, 3, 5, 9, 4, 2     9
'''

first_num = int(input("Son kiriting: "))
max_number = first_num

for i in range(6):
    son = int(input("Son kiriting: "))
    if son > max_number:
        max_number = son
        
print(max_number)
