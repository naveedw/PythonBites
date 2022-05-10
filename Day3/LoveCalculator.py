# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

true_score = 0
love_score = 0

#TRUE score
true_score += name1_lower.count("t")
true_score += name1_lower.count("r")
true_score += name1_lower.count("u")
true_score += name1_lower.count("e")
true_score += name2_lower.count("t")
true_score += name2_lower.count("r")
true_score += name2_lower.count("u")
true_score += name2_lower.count("e")

# love score
love_score += name1_lower.count("l")
love_score += name1_lower.count("o")
love_score += name1_lower.count("v")
love_score += name1_lower.count("e")
love_score += name2_lower.count("l")
love_score += name2_lower.count("o")
love_score += name2_lower.count("v")
love_score += name2_lower.count("e")

loveScore = str(true_score) + str(love_score)
loveScore = int(loveScore)


if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore < 50 and loveScore > 40:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")



