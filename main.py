print("Welcome to the bill calculator")
bill = float(input("How much was the total bill $"))
tip = float(input("What percentage of tip would you like to give? "))
people = int(input("How many people to split the bill "))

tip = tip / 100 * bill
bill = round((bill + tip) / people,2)
print(f"The amount of money each person should pay ${bill}")
