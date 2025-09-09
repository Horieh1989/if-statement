from numpy import around


number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
if int(number1) < int(number2):
    print(f"The smallest number is: {number1}")
elif int(number1) > int(number2):
        print(f"The smallest number is: {number2}")

elif int(number1) == int(number2):
        print("Both numbers are equal")