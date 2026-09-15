from functions import *
from test_lib import test, report

expected = False
result = is_prime(-7)
test('TEST: is_prime(-7)',expected, result)

expected = False
result = is_prime(0)
test('TEST: is_prime(0)',expected, result)

expected = False
result = is_prime(1)
test('TEST: is_prime(1)',expected, result)

expected = True
result = is_prime(2)
test('TEST: is_prime(2)',expected, result)

expected = True
result = is_prime(7)
test('TEST: is_prime(7)',expected, result)

expected = False
result = is_prime(66)
test('TEST: is_prime(66)',expected, result)

expected = True
result = is_prime(101)
test('TEST: is_prime(101)',expected, result)

expected = False
result = is_prime(19872496)
test('TEST: is_prime(19872496)',expected, result)

expected = [2, 3, 5, 7, 11]
result = get_first_primes(5)
test('TEST: get_first_primes(5)', expected, result)

expected = [2, 3, 5]
result = get_first_primes(3)
test('TEST: get_first_primes(3)', expected, result)

if __name__ == "__main__":
    report()