import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #Returns a random element froma  list
    while '-' in word or ' 'in word: #This allow us to to make sure we only chose words that dont have a - or space. could be used for kanji add on.
        word = random.choice(words)

    return word.upper()#makes word uppercase.

def hangman():
    word = get_valid_word(words)#run function on massive words list to find a suitable word.
    #store the letters of the word as a set. making it unordered and unchangeable. 
    #e.g. if word was football, then set(word) could return {'t', 'l', 'o', 'f', 'b', 'a'} or any other random arrangement of the word.
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase) #a set of all uppercase alphabet letters. e.g. {A,B,C,D,E...}
    used_letters = set()#what letters the user has used will go in here. currently it's = {}

    lives = 6

    #keep asking user for letter until theres no more words in the set of word letters.
    while len(word_letters) > 0 and lives > 0:
        # letter used
        # ' '.join(['a','b','cd']) --> 'a b cd' - join() adds the contents of a tuple/list/set to a string seprated by by whatever you put in the ' '.
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        

        #what current word is with dashes.
        #List comprehensions. this is a shorter way of creating a list from another list using a for loop.
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))


        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:# if the letter the user just guessed is a letter in the alphbet that they havn't guessed before...
            used_letters.add(user_letter) #add that letter to the list of used letters. Then...
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 #takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again')    

        else:#user typed something not in the alphabet
            print('Invalid character. Please try again.') 

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('you died, sorry. The wird was', word)
    else:
        print('You guessed the word', word, '!!')


hangman() 