prijs1 = 6.50
prijs2 = 9.30
prijs3 = 11.10

try: 
    pizza1 = int(input("Hoeveel small pizza's wilt u?:"))
except ValueError:
    print("Dit is geen heel nummer!")
    pizza1 = 0

try:
    pizza2 = int(input("Hoeveel medium pizza's wilt u?: "))
except ValueError:
    print("Dit is geen heel nummer!")
    pizza2 = 0

try:
    pizza3 = int(input("Hoeveel large pizza's wilt u?: "))
except ValueError:
    print("Dit is geen heel nummer! ")
    pizza3 = 0 

print ('**************Kassa bon**************')
if pizza1 > 0:
    print (f"Pizza's small:\t  {pizza1} x 6.50 =   {prijs1 * pizza1:.2f}")
if pizza2 > 0:
    print (f"Pizza's medium:\t  {pizza2} x 9.30 =  {prijs2 * pizza2:.2} ")
if pizza3 > 0:  
    print (f"Pizza's large:\t  {pizza3} x 11.10 = {prijs3 * pizza3:.2f} ")
print ('--------------------------------------')
print (f'Te betalen:                   {prijs1 * pizza1 + prijs2 * pizza2 + prijs3 * pizza3:.2f} ')

