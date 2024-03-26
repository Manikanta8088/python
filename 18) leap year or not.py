year=int(input("Enter the year:"))
if year%400==0 and year%100==0:
    print("It is an leap year")
elif year%4==0 and year%100!=0:
    print("It is an leap year")
else:
    print("It is not an leap year")
`
