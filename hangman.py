# Hangman Game

# modules: time module to pause gameplay at intervals
import time 

# PROGRAM FUNCTIONS

# spaces: prints many new lines to hide previous input 
def spaces():
    for space in range(0,60,1):
        print(" ")

# characters: validates individual character input in game
def character():
                
    while True:
        char = input("Enter a character ").lower()
        if char.isalpha() == False:
            print("Character must be a letter!")
        elif char == "":
            print("Character field cannot be blank!")
        elif len(char) > 1:
            print("Character should only be one letter!")
        else:
            break
        print()
    return char

# guessed_word: prints blanks/entered characters for hangman word
def get_guessed_word(word, correct_letters):
    new_blanks = ""
    for char in word:
        if char in correct_letters: 
            new_blanks = new_blanks + char + " "
        elif char == " ":
            new_blanks = new_blanks + "  "
        else:
            new_blanks= new_blanks + "_ "
    return new_blanks

# display_hangman: prints hangman based on incorrect entries 
def display_hangman(tries, fails):

    result = tries - fails

    if result == 8:
        print("    _____ \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              " __|__\n")
        
    if result == 7:
        print("    _____ \n"
              "   |     |\n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              " __|__\n")
        
    if result == 6:
        print("    _____ \n"
              "   |     |\n"
              "   |     |\n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              " __|__\n")
        
    if result == 5:
        print("    _____ \n"
              "   |     |\n"
              "   |     |\n"
              "   |     0\n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              " __|__\n")
    
    if result == 4:
        print("    _____ \n"
              "   |     |\n"
              "   |     |\n"
              "   |     0\n"
              "   |     |\n"
              "   |      \n"
              "   |      \n"
              " __|__\n")
        
    if result == 3:
        print("    _____ \n"
              "   |     |\n"
              "   |     |\n"
              "   |     0\n"
              "   |    /|\n"
              "   |      \n"
              "   |      \n"
              " __|__\n")
        
    if result == 2:
        print("    _____ \n"
              "   |     |\n"
              "   |     |\n"
              "   |     0\n"
              "   |    /|\ \n"
              "   |      \n"
              "   |      \n"
              " __|__\n")
        
    if result == 1:
        print("    _____ \n"
              "   |     |\n"
              "   |     |\n"
              "   |     0\n"
              "   |    /|\ \n"
              "   |    / \n"
              "   |      \n"
              " __|__\n")
        
    if result == 0:
        print("    _____ \n"
              "   |     |\n"
              "   |     |\n"
              "   |     0\n"
              "   |    /|\ \n"
              "   |    / \ \n"
              "   |      \n"
              " __|__\n")
            
# introduces game   
print("Hangman Game")
print("------------")
print()

# SETUP

# defines turn 
gamerun = 1

# player scores 
player1_score = 0
player2_score = 0

# list of all words preventing reuse of words 
entered_words = []

# get usernames 
while True:
    player1 = input("Player 1, enter your name: ").title()
    if player1 == "":
        print("Player name cannot be blank!")
    else:
        break

while True:
    player2 = input("Player 2, enter your name: ").title()
    if player2 == player1:
        print("Player names cannot be the same!")
    elif player2 == "":
        print("Player name cannot be blank!")
    else:
        break

print()

print("Hello", player1, "and", player2 + "!")

print()

time.sleep(0.5)

# main running of game 

while True:

    # prints instructions based on whose turn it is 
    if gamerun % 2 != 0:    
        print(player1, "it's your turn! Don't let", player2, "look!")
        print()
        time.sleep(0.75)
        print("Think of a secret word or phrase. ", player2, "will try to guess this")
        print()
        time.sleep(0.75)
        print(player2, "will have a number of tries to guess the word or phrase")
        print()

    if gamerun % 2 == 0: 
        print(player2, "it's your turn! Don't let", player1, "look!")
        print()
        time.sleep(0.75)
        print("Think of a secret word or phrase. ", player1, "will try to guess this")
        print()
        time.sleep(0.75)
        print(player1, "will have a number of tries to guess the word or phrase")
        print()

    time.sleep(3)

    # enter tries for other player to guess word 
    while True:
        try:
            tries = int(input("Enter number of tries: "))
            print()
            if tries > 9:
                print("Too many tries! Enter a number from 1 to 9")
            elif tries < 1:
                print("Too few tries! Enter a number from 1 to 9")
            else:
                print("Good choice!")
                break
        except ValueError:
            print("Invalid input! Enter a number from 1 to 9")

    time.sleep(1)

    print()
    
    # enter validated word or phrase for other player to guess 
    while True:
        word = input("Enter a word or short phrase ").lower()
        if len(word) == 0:
            print("Field cannot be blank!")
        elif len(word) == 1:
            print("Too short! Try using a longer word or phrase")
        else:
            wordreplace = word.replace(" ", "")
            if wordreplace.isalpha():
                if word in entered_words:
                    print("Word or phrase already used in this game!")
                    print()
                else:
                    entered_words.append(word)
                    print("This will now be the hangman word or phrase!")
                    break
            else:
                print("Word or phrase should only include letters and spaces!")

    # splits phrase into individual words 
    words = word.split()

    time.sleep(1)

    # hide previous user input 
    spaces()
    
    # hands over to playing user 
    if gamerun % 2 != 0:    
        print(player2, "it is your turn!")
    else:
        print(player1, "it is your turn!")

    print()

    time.sleep (1)

    # prints instructions to playing user 
    print("The hangman word or phrase will be presented as blank spaces")
    time.sleep(0.75)
    
    print("Your goal is to enter the correct characters to discover the hangman word or phrase")

    print()
    time.sleep(1)

    print("If you guess", tries, "letters incorrectly the game will be over")

    print()

    time.sleep(2.5)
    
    # SETUP

    # list representing characters of word or phrase as underscores 
    blankslst = []

    # creating blankslst
    for item in words:
            blankslst.append("_ " * len(item) + " ")

    blanks = ""
    
    for item in blankslst:
        blanks = blanks + item

    print(blanks)

    time.sleep(1)

    print()

    # records incorrect entries to be used in hangman display
    fails = 0

    # set storing entered letters that are correct
    correct_letters = set()

    # loop for character entry gameplay 

    while True:
        
        setword = set(wordreplace)
    
        if len(setword) == len(correct_letters):
            print("You win!")
            if gamerun % 2 != 0:
                player2_score = player2_score + 1
            else:
                player1_score = player1_score + 1
            break

        if fails == tries:
            print("Game over!")
            print("The hangman word/phrase was: ", word)
            time.sleep(0.75)
            break

        # character entry
        char = character()

        print()
              
        # checks for correct character entry 
        count = 0

        if char in word:
            if char in correct_letters:
                print("Letter already entered!")
            else:
                count = count + 1
                print("TEST: ", str(count))
                if len(char) == 1:
                    correct_letters.add(char)
        if count > 0:
            print(get_guessed_word(word, correct_letters))
        if char not in word:
            print(char, "is not in the word/phrase!")
            fails = fails + 1
            print()
            display_hangman(tries, fails)
            time.sleep(1)

        print()

    print()

    # user decides to continue playing or quit 
    while True:
        again = input("Play again? (Y) or (N) ").upper()
        if again == "Y":
            gamerun = gamerun + 1
            time.sleep(1)
            spaces()
            break
        if again == "N":
            break
        else:
            print("Enter Y to play again and N to quit")

    if again == "N":
        break

print()

time.sleep(0.5)

# prints results of game to users 
while True:
    if player1_score == player2_score:
        if player1_score > 0 or player2_score > 0:
            print("You both tied!")
        else:
            break
    elif player1_score > player2_score:
        print(player1 + " won! The score was ", str(player1_score) + ":" + str(player2_score))
    else:
        print(player2 + " won! The score was ", str(player2_score) + ":" + str(player1_score))
    print()
    time.sleep(1)
    break

# exit message
print("Thank you for playing!")
