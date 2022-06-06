import random
from hangman_art import stages
from hangman_cities import word_list
from hangman_art import logo

print(logo)

chosen_word= random.choice(word_list)


display= []


word_length=len(chosen_word)
for letter in chosen_word:
    display.append("_") 


end_of_game = False

lives= 6



while not end_of_game:
    guess= input("Pick a letter?").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}. ")


    for position in range (word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position]= letter
            print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You lose a life. Try again")
        if lives == 0:
            end_of_game=True
            print(f"You lose! The city is {chosen_word}!") 
    


    if "_" not in display:
        end_of_game= True
        print(f"You Win! You correctly guessed the city of {chosen_word}.")
    
    print(stages[lives])
    


    

