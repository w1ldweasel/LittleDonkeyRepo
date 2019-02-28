# ==== Code club
# ==== Exercise 3 Nicks Version
# ==== Added Sorting to Lotto and Euro and Star Numbers

import random

# Intro message
def askgamechoice(*answer):
  print('\n\n')        
  print ("Which game would you like to play? Enter \'L\' for Lotto, \'E\' for Euromillions.")
  game_choice = input('Choice >')
  if game_choice.lower() == 'l':
    generate_lotto_numbers()
  elif game_choice.lower() == 'e':
    generate_euro_numbers()
  else: print('You did not enter L or E, so quitting')

# function that returns 6 random numbers
def generate_lotto_numbers():
    lotto_numbers = []
    for i in range(6):
        lotto_number = random.randint(1,59)
        lotto_numbers.append(lotto_number)
        lotto_numbers.sort()
    print('These are your six numbers:')
    print(lotto_numbers)

# function that returns 5 random main numbers and 2 'star' numbers
def generate_euro_numbers():
    euro_numbers = []
    star_numbers = []
    for i in range(5):
        euro_number = random.randint(1,51)  
        euro_numbers.append(euro_number)
        euro_numbers.sort()
    for i in range(2):
        star_number = random.randint(1,13)  
        star_numbers.append(star_number)
        star_numbers.sort()

    print('These are your five main numbers and two star numbers:')                
    print(euro_numbers)
    print(star_numbers)

def new_random_list(number_list_arg):
    temp_list = number_list_arg
    current_list_size = len(temp_list)
    flag = len(temp_list)
    while flag == current_list_size:
        new_number = random.randint(1,60)
        if new_number not in temp_list:
            temp_list.append(new_number)
            flag = flag+1
            return temp_list
        
#main()
if __name__ == "__main__":
  askgamechoice()