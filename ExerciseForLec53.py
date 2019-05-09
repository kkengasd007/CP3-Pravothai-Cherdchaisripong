def vatCalculate(totalprice):
    result = totalprice * 107/100
    return  result
price = int(input("TotalPrice : "))
print(vatCalculate(price))