def vatCalculate(total):
    result = total+(total*7/100)
    return result
print("Price + Vat = ",vatCalculate(int(input("Input Price: ")))," THB")