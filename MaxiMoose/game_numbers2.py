# ==== Code club
# ==== Exercise 3
# 
##==== Written by Max Ng 
##==== 20/01/2019
#

#
import random
from os import path
from datetime import datetime

# Intro message
def askgamechoice():
    game_choice = 'i' #set initial alue
    while game_choice.lower() != 'q':
        print('\n')        
        print ("Which game would you like to play? Enter \'l\' for Lotto,\'e\' for Euromillions or \'q\' to quit the game.")
        game_choice = input('Choice >')
        if game_choice.lower() == 'l':
            generate_lotto_numbers()
        elif game_choice.lower() == 'e':
            generate_euro_numbers()
        elif game_choice.lower() == 'q':
            break
        else:
            print('Illegal character, try again')
    
    print('\n')
    print('Goodybye, thank you for playing')
    
# function that returns 6 random numbers
def generate_lotto_numbers():
    lotto_numbers = []
    for i in range(6):
#        print('in generate_lotto_numbers')
        lotto_numbers = new_random_list(lotto_numbers, 59)
        
    print('These are your six numbers:')
    lotto_numbers.sort()    
    print(lotto_numbers)
    save_file = input('Would you like to save these numbers? Please answer \"y\" to save. ')
    if save_file.lower() == 'y':
        save_to_file('lotto_numbers.txt', main_game = lotto_numbers)
    
    
# function that returns 5 random main numbers and 2 'star' numbers
def generate_euro_numbers():
    euro_numbers = []
    star_numbers = []
    for i in range(5):
        euro_numbers = new_random_list(euro_numbers,50)  
    for i in range(2):
        star_numbers = new_random_list(star_numbers,12)  

    print('These are your five main numbers and two star numbers:')
    euro_numbers.sort()
    star_numbers.sort()                
    print(euro_numbers)
    print(star_numbers)
    save_file = input('Would you like to save these numbers? Please answer \"y\" to save. ')
    if save_file.lower() == 'y':
        save_to_file('euro_numbers.txt', main_game = euro_numbers, stars = star_numbers, euromillion = True )
        

def new_random_list(number_list_arg, number_range):
    temp_list = number_list_arg
#    print('in new_random_list')

    current_list_size = len(temp_list)
    flag = len(temp_list)
#    print('flag = ', flag)
    while flag == current_list_size:
        new_number = random.randint(1, number_range)
#            print('new random number')
#            print(new_number)
#        print(temp_list)
        if new_number not in temp_list:
            temp_list.append(new_number)
            flag = flag+1
#            print('append')
#            print(temp_list)
            return temp_list
        
def save_to_file(filename, main_game = [], stars = [], euromillion = False):
    if path.exists(filename):
        f = open(filename, 'a')
#        f.write('\n' + datetime.now().strftime("%d %B %Y") + ' ' + str(main_game))
        f.write('\n' + datetime.now().strftime("%d/%m/%Y") + ' ' + str(main_game))
        if euromillion == True: 
            f.write(' ' + str(stars))
    else:
        f = open(filename, 'w')
        f.write(str(main_game))
        if euromillion == True: 
            f.write(' ' + str(stars))
    f.close()
        
#main()
if __name__ == "__main__":
  askgamechoice()