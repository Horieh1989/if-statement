number=int(input("enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
if number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")
if number % 5==0 and number % 2!=0:
    print("The number is divisible by both 5 and is odd.")