prijs1 = 6.50
prijs2 = 9.30
prijs3 = 11.10


pizza1 = float(input("Hoeveel small pizza's wilt u?: "))
pizza2 = float(input("Hoeveel medium pizza's wilt u?: "))
pizza3 = float(input("Hoeveel large pizza's wilt u?: "))

print ('**************Kassa bon**************')
print (f"Pizza's small:\t  {pizza1} x 6.50 =   {prijs1 * pizza1:.2f}")
print (f"Pizza's medium:\t  {pizza2} x 9.30 =  {prijs2 * pizza2} ")
print (f"Pizza's large:\t  {pizza3} x 11.10 = {prijs3 * pizza3} ")
print ('--------------------------------------')
print (f'Te betalen:                     {prijs1 * pizza1 + prijs2 * pizza2 + prijs3 * pizza3} ')


