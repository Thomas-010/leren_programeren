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
print(f'Ingrediënten voor {nr_persons} {str_single_plural(nr_persons, TXT_PERSONS)}: ')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print_pieces(amount_eggs, TXT_EGGS)
print_volume(amount_milk, UNIT_MILK, TXT_MILK)
print_weight(amount_salt, UNIT_SALT, TXT_SALT, GRAM_PER_ML_SALT)
print_weight(amount_pepper, UNIT_PEPPER, TXT_PEPPER, GRAM_PER_ML_PEPPER)
print_volume(amount_oil, UNIT_OIL, TXT_OIL)
print_pieces(amount_onions, TXT_ONIONS)
print_pieces(amount_garlics, TXT_GARLICS)
print_pieces(amount_paprikas, TXT_PAPRIKAS)
print_weight(amount_spinach, UNIT_SPINACH, TXT_SPINACH, GRAM_PER_ML_SPINACH)
print_weight(amount_cheese, UNIT_CHEESE, TXT_CHEESE, GRAM_PER_ML_CHEESE)
print('-----------------------------------------------')