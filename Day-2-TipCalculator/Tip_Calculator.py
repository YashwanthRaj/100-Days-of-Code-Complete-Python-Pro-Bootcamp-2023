print("Welcome to Tip Calculator!!!")
price = float(input("Enter the total amount: "))
person = int(input("Enter the number of people: "))
tip = int(input("Enter then tip percentage {10%, 12%, 15%}: "))

tip_percentage = tip/100
total_tip = price * tip_percentage
total_price = price + total_tip

per_person = total_price / person
per_person = round(per_person, 2)

print(f"Each person should pay {per_person}: ")