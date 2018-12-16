import random
import re


def get_usable_random_movie_name(movie_list):
    movie_name = random.choice(movie_list).strip()
    blank_form = convert_to_blank_form(movie_name)
    if has_atleast_one_blank(blank_form):
        return movie_name.upper(),blank_form
    get_usable_random_movie_name(movie_list)


def convert_to_blank_form(str):
    return re.sub(r'[a-zA-Z]','_',str)

def has_atleast_one_blank(str):
    regex = re.compile('[_]')   
    if(regex.search(str) == None): 
        return False       
    return True 

def find_allindexes_of_letter_in_str(str,letter):
    return [m.start() for m in re.finditer(letter, str)]
    
def replace_blanks_with_letters(string,letter, index_list):
    strlist = list(string)
    for i in index_list:
        strlist[i] = letter
    return ''.join(str(e) for e in strlist) 
    
def read_movienames_from_file():
    file = open('new_movie_list.txt','r')
    mlist = file.readlines()
    file.close()
    return mlist

def get_character_guess_from_user():
    while True:
            userInput = input('Enter Guess:')
            if len(userInput) == 1 and userInput.isalpha():
                return userInput.upper()
            print('Please enter only one Alphabetical Guess')

def run():
    lives_remaining = 9
    miss_list = []
    already_guessed_list = []

    mlist = read_movienames_from_file()
    movie, blank= get_usable_random_movie_name(mlist)

    while(has_atleast_one_blank(blank) and lives_remaining>0):
        print("***********************************")
        print("\n",blank,"\n")
        print("Lives Remaining = ",lives_remaining)
        print("Failed Guess List : ",','.join(miss_list))
        userInput = get_character_guess_from_user()

        if userInput in already_guessed_list:
            print('You have already tried guessing ',userInput)
            continue
        already_guessed_list.append(userInput)    

        index = find_allindexes_of_letter_in_str(movie,userInput)
        if not index:
            print('OOPS! YOU LOST A LIFE!')
            lives_remaining -=1
            miss_list.append(userInput)
        else:
            print('GOOD GUESS')
            blank = replace_blanks_with_letters(blank,userInput,index)

    print("***********************************")
    print("***********************************")
    
    if(lives_remaining==0):
        print("GAME OVER! \nYou clearly need to watch some films. \nThe Movie was :",movie)
    else:
        print("You are a cine-lover! That's Great!\n You correctly guessed the movie :", movie)        
def main():
    print("Welcome to GuessTheMovie.\nYou have nine lives.\nTry to guess the correct movie name by entering characters one by one.\nLet's see if you are a real movie buff.\n ")
    option = "y"
    while(option.lower()=="y"):
        run()
        option= input("Do you want to play again [y/n]") 
main()
