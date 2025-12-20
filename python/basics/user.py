# scanf("%d", &var) equivalent in C

# no = input("Enter a number: ")

# print("You entered:", no)

no = int(input("Enter a number: "))  # type casting.....

print("value is:", no+1)
print("type of no:", type(no))

pers = float(input("Enter percentage: "))
print("Percentage is:", pers + 0.1)
print("Type of pers is:", type(pers))