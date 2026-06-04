
'''
3. Sonlar ketma ketligi
Shart: for loop dan foydalanib foydalanuvchi kiritgan butun sondan boshlab 15 gacha
barcha butun sonlarni chiqaring.

Input       Output
3           3 4 5 6 7 8 9 10 11 12 13 14 15
'''

start = int(input("Start: "))
stop = 15

if start < stop:
    for i in range(start, stop + 1):
        print(i)
else:
    print("Start soni 15 sonidan kichik bo'lishi kerak.")