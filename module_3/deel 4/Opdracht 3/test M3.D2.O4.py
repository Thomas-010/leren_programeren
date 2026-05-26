from test_lib import test, report
 
MONTH_DISCOUNT_PERC = 10
 
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    brands = month_discount_brands.split(",")
    if brand in brands:
        discount = price * MONTH_DISCOUNT_PERC / 100
    else:
        discount = 0
    return round(discount, 2)
 
DISCOUNT_BRANDS = 'Vespa,Kymco,Yamama'

price = 2000
brand = 'Vespa'
expect_discount = 200.00
name = f'test discount: brand={brand} price={price}'
test(name, expect_discount, calc_discount(price, brand, DISCOUNT_BRANDS))
 
price = 1500
brand = 'Kymco'
expect_discount = 150.00
name = f'test discount: brand={brand} price={price}'
test(name, expect_discount, calc_discount(price, brand, DISCOUNT_BRANDS))
 
price = 3000
brand = 'Yamama'
expect_discount = 300.00
name = f'test discount: brand={brand} price={price}'
test(name, expect_discount, calc_discount(price, brand, DISCOUNT_BRANDS))
 
price = 2000
brand = 'Honda'
expect_discount = 0
name = f'test discount: brand={brand} price={price} (geen korting)'
test(name, expect_discount, calc_discount(price, brand, DISCOUNT_BRANDS))
 
price = 5000
brand = 'BMW'
expect_discount = 0
name = f'test discount: brand={brand} price={price} (geen korting)'
test(name, expect_discount, calc_discount(price, brand, DISCOUNT_BRANDS))
 
price = 0
brand = 'Vespa'
expect_discount = 0.00
name = f'test discount: brand={brand} price={price}'
test(name, expect_discount, calc_discount(price, brand, DISCOUNT_BRANDS))
 
price = 99.99
brand = 'Kymco'
expect_discount = 10.00
name = f'test discount: brand={brand} price={price}'
test(name, expect_discount, calc_discount(price, brand, DISCOUNT_BRANDS))
 
price = 2000
brand = 'vespa'
expect_discount = 0
name = f'test discount: brand={brand} price={price} (kleine letter = geen korting)'
test(name, expect_discount, calc_discount(price, brand, DISCOUNT_BRANDS))
 
report()