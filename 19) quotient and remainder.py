dividend=int(input("Enter the dividend value:"))
divisor=int(input("Enter the divisor value:"))
if divisor!=0:
    quotient=dividend/divisor
    remainder=dividend%divisor
    print("Quotient =",quotient)
    print("Remainder =",remainder)
else:
    print("Error!")
