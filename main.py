# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1lw = name1.lower()
name2lw = name2.lower()
t = name1lw.count("t") + name2lw.count("t")
r = name1lw.count("r") + name2lw.count("r")
u = name1lw.count("u") + name2lw.count("u")
e = name1lw.count("e") + name2lw.count("e")
true = t + r + u + e

l = name1lw.count("l") + name2lw.count("l")
o = name1lw.count("o") + name2lw.count("o")
v = name1lw.count("v") + name2lw.count("v")
e = name1lw.count("e") + name2lw.count("e")
love = l + o + v + e


#print(f"Value is {love}{true}")
#score = love + true
score = int(str(love) + str(true))

if score >= 40 and score <= 50 :
  print(f"Your score is {score}, you are alright togethe.")

elif score < 10 or score > 90:
  print(f"Your score is {score},you go together like coke and mentos.")

else :
  print(f"Your score is {score}")
