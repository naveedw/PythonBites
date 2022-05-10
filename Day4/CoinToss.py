#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

import random   
 	 
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
random_num = random.randint(0,1)
if random_num == 1:
    print("Heads")
else:
    print("Tails")    