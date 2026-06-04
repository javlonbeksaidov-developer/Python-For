
'''
5. Sonlar ketma ketligi
Shart: for loop dan foydalanib foydalanuvchi kiritgan i butun sondan boshlab
foydalanuvchi kiritgan n butun songacha barcha butun sonlarni chiqaring.

Input       Output
6, 11        6 7 8 9 10 11

'''

start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

for i in range(start, stop + 1, step):
    print(i)