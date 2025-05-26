import random
from words_hang import word_list
import string


# def get_valid_word(word_list):
# what is the difference with the one below
def get_valid_word():
    word = random.choice(word_list)
    return word

def hangman():
    word = get_valid_word().upper()
    # why use set for hang man
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) 
    used_letters = set()
    lives = 6 

    
 
    while lives!=0 and len(word_letters) != 0:

        used_display = "  ".join(used_letters)
        print(f"LIVES - {lives} \n Your used letters are  {used_display} ")

        word_list = [letter  # this list should house all letters
        if letter in used_letters 
        else "-" for letter # else house - if the letter isn't in used letter
        in word] # for all letters in word
        
        print("current word is ", "".join(word_list))
        user_letter = input("guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            # what is the difference between the add and append
            used_letters.add(user_letter)
            # different approach
            if user_letter in word_letters:
                #so when user is doe
                word_letters.remove(user_letter)
            else :
                lives -= 1
                print("WRONG WORD")
                

        elif user_letter in used_letters: 
            print("You have already used this letter. please try again.")

           
        else:
            lives -= 1
            print("Invalid character. Please")
            
    if len(word_letters) == 0:
        print("hurray")
    else:
        print('you died')
    

 

hangman()