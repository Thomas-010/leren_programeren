import functions
from calculations import CALCULATIONS
from test_lib import test, report

number1 = 2.0
number2 = 2.0
expected = functions.addition(number1, number2)
calculated = CALCULATIONS['addition'](number1, number2)
test('addition', expected, calculated)



number1 = 2.0
number2 = 2.0
expected = functions.subtraction(number1, number2)
calculated = CALCULATIONS['subtraction'](number1, number2)
test('subtraction', expected, calculated)



number1 = 2.0
number2 = 2.0
expected = functions.multiplication(number1, number2)
calculated = CALCULATIONS['multiplication'](number1, number2)
test('multiplication', expected, calculated)



number1 = 2.0
number2 = 2.0
expected = functions.division(number1, number2)
calculated = CALCULATIONS['division'](number1, number2)
test('division', expected, calculated)

report()