while True:
    try:
        age = int(input("Enter your age: "))
        weight = int(input("Enter your weight in kg: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

 
if 3 <= age <= 7 and 15 <= weight <= 25:
    print("You should take medicine 1/5 pill")
elif 7 <= age <= 12 and 26 <= weight <= 40:
    print("You should take medicine 1/2-1 pill")
elif age >= 12:
    print("You should take medicine 1-2 pills")
else:
    print("You are not in this category")

    