
'''
11. Eng katta va eng kichik son o‘rtachasi
Shart: Foydalanuvchi tomonidan kiritilgan n sonidan eng katta va eng kichik
sonlarning o‘rtachasini toping.

Input               Output
3, 5, 1, 8, 7       4.5
'''

first_num = int(input("Son kiriting: "))
min_number = first_num
max_number = first_num

for i in range(4):
    son = int(input("Son kiriting: "))
    if son < min_number:
        min_number = son
    if son > max_number:
        max_number = son
        
result = (min_number + max_number) / 2
print(result)