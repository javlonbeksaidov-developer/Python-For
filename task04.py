
'''
4. Sonlar ketma ketligi
Shart: for loop dan foydalanib foydalanuvchi kiritgan i butun sondan boshlab 15
gacha barcha butun sonlarni foydalanuvchi kiritgan step butun son qadam bilan
chiqaring.
Input       Output
4, 3        4 7 10 13
'''

start = int(input("Start: "))
stop = 15
step = int(input("Step: "))

if start < stop:
    for i in range(start, stop + 1, step):
        print(i)
else:
    print("Start soni 15 sonidan kichik bo'lishi kerak.")