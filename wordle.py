from english_words import english_words_lower_alpha_set
from random import randint

def wordle():
    print('\nWelcome to Wordle!\n')
    count = 0
    guess = '123456'

    def get_6_letter_word():
        #Convert set into list
        word_list = []
        for i in english_words_lower_alpha_set: 
            word_list.append(i)

        #Get a random word
        num = randint(1,2)
        secret_word = word_list[num]

        #Check if the word is 6 letters long and reset if not
        while len(secret_word) != 6:
            num = randint(1,100)
            secret_word = word_list[num]
        
        #Return the new word
        return(secret_word)
    
    word = get_6_letter_word()

    while guess != word:
        #Make sure the guess is 6 characters long
        while len(guess) != 6:
            print('Your guess needs to be 6 letters long!. Try again')
            guess = input('Guess: ').lower() 
        #Counter
        count += 1
        #Print the hint out 
        print('Hint: ',end='')
        for i, letter in enumerate(guess):
            if letter == word[i]:
                print(letter.upper(),end='')
            elif guess[i] in word:
                print(letter.lower(),end='')
            else:
                print('_',end='')

        print()
        #Get the guess from the user
        guess = input('Guess: ').lower()

    #Prints is they guess it correctly    
    print(f'Congratulations! You guessed it in {count} tries.\n')
     
#Run the game
wordle()