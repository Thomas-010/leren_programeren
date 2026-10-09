from recipe_lib import *
from frittata_ingredients import *

def print_pieces(amount: int, txt: str):
    print(f'* {amount} {str_single_plural(amount, txt)}')

def print_measured(amount: float, unit: str, txt: str):
    print(f'* {str_amount_fraction(amount)} {str_units(amount, unit)} {str_single_plural(amount, txt)}')

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons('Ingredienten voor hoeveel personen?\n')

# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons / RECIPE_PERSONS
# calculate amount_eggs
amount_eggs = round_piece(AMOUNT_EGGS * factor)
# calculate amount_milk
amount_milk = round_quarter(AMOUNT_MILK * factor)
# calculate amount_salt
amount_salt = round_quarter(AMOUNT_SALT * factor)
# calculate amount_pepper
amount_pepper = round_quarter(AMOUNT_PEPPER * factor)
# calculate amount_oil
amount_oil = round_quarter(AMOUNT_OIL * factor)
# calculate amount_onions
amount_onions = round_piece(AMOUNT_ONIONS * factor)
# calculate amount_garlics
amount_garlics = round_piece(AMOUNT_GARLICS * factor)
# calculate amount_spinach
amount_spinach = round_quarter(AMOUNT_SPINACH * factor)
# calculate amount_paprikas
amount_paprikas = round_piece(AMOUNT_PAPRIKAS * factor)
# calculate amount_cheese
amount_cheese = round_quarter(AMOUNT_CHEESE * factor)
# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} {str_single_plural(nr_persons, TXT_PERSONS)}')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print_pieces(amount_eggs, TXT_EGGS)
print_measured(amount_milk, UNIT_MILK, TXT_MILK)
print_measured(amount_salt, UNIT_SALT, TXT_SALT)
print_measured(amount_pepper, UNIT_PEPPER, TXT_PEPPER)
print_measured(amount_oil, UNIT_OIL, TXT_OIL)
print_pieces(amount_onions, TXT_ONIONS)
print_pieces(amount_garlics, TXT_GARLICS)
print_pieces(amount_paprikas, TXT_PAPRIKAS)
print_measured(amount_spinach, UNIT_SPINACH, TXT_SPINACH)
print_measured(amount_cheese, UNIT_CHEESE, TXT_CHEESE)
print('-----------------------------------------------')