n=int(input("Enter the number:"))
if n%3==0 and n%5==0:
    print("It is divisible by both 3 and 5")
elif n%3==0:
    print("It is divisible by only 3")
elif n%5==0:
    print("It is divisible by only 5")
else:
    print("It is not divisible by both 3 and 5")
