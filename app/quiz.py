#
# This is the 5 question quiz that a user will take before being paired with a pokemon
#

# Favorite color
color = input("What is your favorite color? \n A. Red \n B. Blue \n C. Green \n D. Yellow \n \n Please enter corresponding letter: ").upper()

if color =="A":
    color_value = 1
elif color == "B":
    color_value = 2
elif color == "C":
    color_value = 3
elif color == "D":
    color_value = 4

user_score = color_value

#
# Favorite Season
#

season = input("What is your favorite season? \n A. Fall \n B. Winter \n C. Spring \n D. Summer \n \n Please enter corresponding letter: ").upper()


if season =="A":
    season_value = 1
elif season == "B":
    season_value = 2
elif season == "C":
    season_value = 3
elif season == "D":
    season_value = 4

user_score = color_value + season_value



#
# Favorite Food
#

food = input("What is your favorite food? \n A. Pizza \n B. Tacos \n C. Noodles \n D. Burgers \n \n Please enter corresponding letter: ").upper()

if food =="A":
    food_value = 1
elif food == "B":
    food_value = 2
elif food == "C":
    food_value = 3
elif food == "D":
    food_value = 4

user_score = color_value + season_value + food_value



#
# Favorite Animal
#

animal = input("What is your favorite animal? \n A. Dog \n B. Cat \n C. Monkey \n D. Tiger \n \n Please enter corresponding letter: ").upper()

if animal =="A":
    animal_value = 1
elif animal == "B":
    animal_value = 2
elif animal == "C":
    animal_value = 3
elif animal == "D":
    animal_value = 4

user_score = color_value + season_value + food_value + animal_value

#
# Elemental ID
#

element = input("What earthly element do you best identify with? \n A. Earth \n B. Wind \n C. Fire \n D. Water \n \n Please enter corresponding letter: ").upper()

if element =="A":
    element_value = 1
elif element == "B":
    element_value = 2
elif element == "C":
    element_value = 3
elif element == "D":
    element_value = 4

user_score = color_value + season_value + food_value + animal_value + element_value
print(user_score)