# ==== Code club
# ==== Exercise 3
# 
##==== Written by Max Ng
##==== Updated by Maxine McFarlane
##==== 20/01/2019
#

#
import random
from datetime import date


# Intro message
def askgamechoice(*answer):
    game_choice = 'x'
     
    while game_choice != 'Q' or game_choice != 'q':
        print('\n\n')        
        print ("Which game would you like to play? Enter \'l\' for Lotto or \'e\' for Euromillions.")
        print ("Enter \'q\' to quit the game")
        game_choice = input('Choice > ')
        
        if game_choice == 'L' or game_choice =='l':
            generate_lotto_numbers()
        elif game_choice == 'E' or game_choice =='e':
            generate_euro_numbers()
        elif game_choice == 'Q' or game_choice == 'q':
            break
            quit_game()
        elif game_choice != 'L' or game_choice !='l' or game_choice != 'E' or game_choice !='e':
            print ("That is not an option.  Please select one of the options listed.")



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
    
    print('Would you like to save these numbers to a file, \'y\' or \'n\'?')
    print_choice = input('Choice > ')
    
    if print_choice == 'Y' or print_choice =='y':
        f = open("lotto_numbers.txt", "a+")
        f.write("Lotto Numbers - %s, played on %s\n" %(lotto_numbers, date.today()))
        f.close()
        print('Your numbers have been saved')
    elif print_choice != 'Y' or print_choice !='y':
        print('Your numbers have not been saved')



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
    
    print('Would you like to save these numbers to a file, \'y\' or \'n\'?')
    print_choice = input('Choice > ')
    
    if print_choice == 'Y' or print_choice =='y':
        f = open("euro_numbers.txt", "a+")
        f.write("Euro Numbers - %s, Star Numbers - %s, played on %s\n" %(euro_numbers, star_numbers, date.today()))
        f.close()
        print('Your numbers have been saved')
    elif print_choice != 'Y' or print_choice !='y':
        print('Your numbers have not been saved')



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
        
        
        
def quit_game():
    exit()
    
    
    
#main()
if __name__ == "__main__":
  askgamechoice()