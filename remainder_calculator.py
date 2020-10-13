def remainder_calculator(numerator, denominator):

    float = numerator / denominator
    rem_decimal = float - int(float)
    remainder = rem_decimal * denominator

    return round(remainder)

x = remainder_calculator(25, 44)
print(x)
