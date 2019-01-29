# ==== Code club
# ==== Exercise 3
# 
##==== Written by Max Ng 
##==== 20/01/2019
#

#
import random

# Intro message
def askgamechoice(*answer):
  print('\n\n')        
  print ("Which game would you like to play? Enter \'L\' or \'l\' for Lotto, \'E\' or \'e\' for Euromillions.")
  game_choice = input('Choice >')
  if game_choice == 'L' or game_choice =='l':
    generate_lotto_numbers()
  elif game_choice == 'E' or game_choice =='e':
    generate_euro_numbers()

# function that returns 6 random numbers
def generate_lotto_numbers():
    lotto_numbers = []
#    for i in range(6):
#        print('in generate_lotto_numbers')
#        lotto_numbers = new_random_list(lotto_numbers)
    for i in range(6):
        lotto_number = random.randint(1,59)  
        lotto_numbers.append(lotto_number)
# sort lotto numbers in ascending order        
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
    for i in range(2):
        star_number = random.randint(1,13)  
        star_numbers.append(star_number)
        
# sort euromillions numbers in ascending order        
    euro_numbers.sort() 
    star_numbers.sort()

    print('These are your five main numbers and two star numbers:')                
    print(euro_numbers)
    print(star_numbers)

def new_random_list(number_list_arg):
    temp_list = number_list_arg
#    print('in new_random_list')

    current_list_size = len(temp_list)
    flag = len(temp_list)
#    print('flag = ', flag)
    while flag == current_list_size:
        new_number = random.randint(1,60)
#            print('new random number')
#            print(new_number)
#        print(temp_list)
        if new_number not in temp_list:
            temp_list.append(new_number)
            flag = flag+1
#            print('append')
#            print(temp_list)
            return temp_list
        
#main()
if __name__ == "__main__":
  askgamechoice()