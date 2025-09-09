while True:
    try:
        height = int(input("Enter the height of your luggage in cm: "))
        length= int(input("Enter the length of your luggage in cm: "))
        width = int(input("Enter the width of your luggage in cm: "))
        weight = int(input("Enter the weight of your luggage in kg: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
dimensions = height * length * width
if length<=55 and width<=40 and height<=23 and weight<=80:
    print("Your luggage is allowed")
elif length<=55 and width<=40 and height<=23 and weight>=80:
    print("Your luggage is too heavy")
elif length>=55 and width>=40 and height>=23 and weight<=80:
    print("Your luggage is too big")
