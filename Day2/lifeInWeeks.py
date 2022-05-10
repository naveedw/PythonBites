# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_remaining = (90 - int(age))

days_single_year = int(365)
weeks_single_year = int(52)
months_single_year = int(12)


message = (f"You have {days_single_year*age_remaining} days, {weeks_single_year*age_remaining} weeks, and {months_single_year*age_remaining} months left.")

print(message)

