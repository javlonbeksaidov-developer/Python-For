
'''
13. Telefonlarning eng katta va eng kichik narxining o‘rtachasini topish
Shart: Telefon do‘konidagi telefonlarning narxlaridan eng yuqori va eng past narxlarni
toping. Bu o‘rtacha narxni yangi telefonlar uchun belgilash mumkin. Telefonlar soni 5
ta.
Input                           Output
300, 450, 150, 720, 620         150, 720
'''

first_tel_price = int(input("Telefon narxini kiriting: "))
min_number = first_tel_price
max_number = first_tel_price

for i in range(4):
    tel = int(input("Telefon narxini kiriting: "))
    if tel < min_number:
        min_number = tel
    if tel > max_number:
        max_number = tel
        
result = (min_number + max_number) / 2
print(result)
print(min_number, max_number)