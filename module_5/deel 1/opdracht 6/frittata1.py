from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons('Ingredienten voor hoeveel personen?\n')

# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons / RECIPE_PERSONS
# calculate amount_eggs
AMOUNT_EGGS = round_piece(AMOUNT_EGGS * factor)
# calculate amount_milk
AMOUNT_MILK = round_quarter(AMOUNT_MILK * factor)
# calculate amount_salt
AMOUNT_SALT = round_quarter(AMOUNT_SALT * factor)
# calculate amount_pepper
AMOUNT_PEPPER = round_quarter(AMOUNT_PEPPER * factor)
# calculate amount_oil
AMOUNT_OIL = round_quarter(AMOUNT_OIL * factor)
# calculate amount_onions
AMOUNT_ONIONS = round_piece(AMOUNT_ONIONS * factor)
# calculate amount_garlics
AMOUNT_GARLICS = round_piece(AMOUNT_GARLICS * factor)
# calculate amount_spinach
AMOUNT_SPINACH = round_quarter(AMOUNT_SPINACH * factor)
# calculate amount_paprikas
AMOUNT_PAPRIKAS = round_piece(AMOUNT_PAPRIKAS * factor)
# calculate amount_cheese
AMOUNT_CHEESE = round_quarter(AMOUNT_CHEESE * factor)
# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print(f'* {AMOUNT_EGGS} {TXT_EGGS}')
print(f'* {AMOUNT_MILK} {UNIT_MILK} {TXT_MILK}')
print(f'* {AMOUNT_SALT} {UNIT_SALT} {TXT_SALT}')
print(f'* {AMOUNT_PEPPER} {UNIT_PEPPER} {TXT_PEPPER}')
print(f'* {AMOUNT_OIL} {UNIT_OIL} {TXT_OIL}')
print(f'* {AMOUNT_ONIONS} {TXT_ONIONS}')
print(f'* {AMOUNT_GARLICS} {TXT_GARLICS}')
print(f'* {AMOUNT_SPINACH} {UNIT_SPINACH} {TXT_SPINACH}')
print(f'* {AMOUNT_PAPRIKAS} {TXT_PAPRIKAS}')
print(f'* {AMOUNT_CHEESE} {UNIT_CHEESE} {TXT_CHEESE}')
print('-----------------------------------------------')