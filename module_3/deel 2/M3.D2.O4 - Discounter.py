month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    brands = month_discount_brands.split(",")

    if brand in brands:
        discount = price * MONTH_DISCOUNT_PERC / 100
    else:
        discount = 0 

    return round(discount, 2)

print(calc_discount(2000, 'Vespa', month_discount_brands))
print(calc_discount(2000, 'Honda', month_discount_brands))