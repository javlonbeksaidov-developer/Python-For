
'''
11. Eng katta va eng kichik son o‘rtachasi
Shart: Foydalanuvchi tomonidan kiritilgan n sonidan eng katta va eng kichik
sonlarning o‘rtachasini toping.

Input               Output
3, 5, 1, 8, 7       4.5
'''

numbers = input("Son kiriting (masalan: 1, 2, 3, 5, 9, 4, 2): ")

num = []
for i in numbers:
    if i.isdigit():
        num.append(i)
        
katta = max(num)
kichik = min(num)

urtacha = (int(katta) + int(kichik)) / 2
print(urtacha)