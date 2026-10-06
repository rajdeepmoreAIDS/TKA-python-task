age = int(input("enter your age: "))

if age < 1 or age > 100:
    print("invalid age")

elif age >= 18:
    print("you are eligible to vote")

else:
    print("you are not eligible to vote")