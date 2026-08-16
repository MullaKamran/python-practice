def cal_discount(price, discount_percent):
    discount = price * discount_percent / 100
    return price - discount

print(cal_discount(1000, 10))
