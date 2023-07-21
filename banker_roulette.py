# pogram to choose a random name in a group who will foot the bill for everyone else

import random

names_string = input("Give me everybody's names, seperated by a comma. ")

# convert input into a string
names = names_string.split(", ")

# shuffle the names
random.shuffle(names)

# Since in a list, we can pull items from that list using an index, i have chosen to use the index of 0 to be where i pull the name from. 
# So any user's names that falls at the 0 zero index after every shuffle will be the name picked

print(f"{names[0]} is going to buy the meal toady!")

# another way to look at it is:
# get the total number of items in the list
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
payee = names[random_choice]
print(payee + "ïs going to buy the meal today")