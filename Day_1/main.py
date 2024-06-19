# Today i am going to create hangman game

import random
import variable

# word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'iceberg lettuce', 'kale', 'lemon', 'mango']
chosen_word = random.choice(variable.word_list)
empty_list=[]
lives = 6
result = False


# print(f'The chosen word is: {chosen_word}')

# Creating list having underscore
for _ in range(len(chosen_word)):
    empty_list.append("_")
print(empty_list)


while(result is False):
    guess = input("Guess the word: ").lower()
    if guess[0] in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess[0]:
                empty_list[i] = guess[0]

        
    else:
        print("Wrong guess")
        lives-=1
    print(empty_list)
    print(variable.stages[lives])
    if "_" not in empty_list:
        result = True
        print("You win")

    if lives == 0:
        result = True
        print("You lose")


