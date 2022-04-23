import random
import Database

 
def print_game_status(remaining_guesses):
    mistakes ==  len(words)-1
    print("word: ",end='')

    for element in guesses:
        print(f"{element}",end='')
    print(f"\nYou have {remaining_guesses} turns remain")    

  
words = ['elephant','apple','circle','square','rabbit','mouse','keyboard','fan','frock','frog','dog','cat','watermelon','chair','table','door','bag','rat','house','radio']
guesses = []

mistakes = 0

status = ""

def startgame():
    mistakes = 0
    status = ""
    word_index = random.randint(0, len(words)-1)
    remaining_guesses = len(words[word_index])
    word = words[word_index].upper()

    

    turns_provide = len(word)
    for i in range(len(word)):
        guesses.append('_')

    game_over = False

    while not game_over:
        print_game_status(remaining_guesses)

    
        user_input = input("please enter a letter : ")

        if not user_input:
            print("That's not a valid input.please try again")
        else:
            letter = user_input[0].upper()
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        guesses[i] = letter
                        
                if '_' not in guesses:
                    game_over = True
            else:
                print("Sorry, that's not part of the word")
                remaining_guesses -= 1
                mistakes += 1
                if mistakes == len(words[word_index]):
                    game_over = True
                
    if mistakes == len(words[word_index]):
        status = "Loss"
        print_game_status(remaining_guesses)
        print(f"Sorry,You lost. The word is : {word}")
    else:
    
        status = "Win"
    
        print("Congratulations......You won!")
        print(f"The word is : {word}")
        
    Database.insert_data(name,word,turns_provide,remaining_guesses,status)
       
name = input("Enter your name : ")
print("Hello", name + "!")
print("Let's play hangman.....")

while True:
    print()
    print("Welcome to Hangman")
    print(" ")
    print("_____Menu_____")
    print("")
    print(" A. Play ")
    print(" B. View History")
    print(" C. Exit")
    I = input("Enter your Menu Letter : ")
    if I == "A":
        startgame()
    elif I == "B":
        Database.display_data()
    elif I == "C":
        print("Game End!")
        break
