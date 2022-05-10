# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
add_pepperoni_S = 2
add_pepperoni_ML = 3
add_extra_cheese = 1

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += add_pepperoni_S
    if extra_cheese == "Y":
        bill += add_extra_cheese 
if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += add_pepperoni_ML
    if extra_cheese == "Y":
        bill += add_extra_cheese 
if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += add_pepperoni_ML
    if extra_cheese == "Y":
        bill += add_extra_cheese 
print(f"Your final bill is: ${bill}.")