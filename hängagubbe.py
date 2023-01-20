import random

print("Welcome to hangwoman")

# A function that chooses and returns random word from a text document
def wrd_from_list():
    with open("ordlista.txt") as text:
        words = text.readlines()
        word = random.choice(words)

    return word


def game():
    # A while-loop that makes the user choose who he/she wants to play against
    # If user chooses computer: the random word funtion is called
    # If user chooses friend: the program lets the user inpu a word
    comp_or_frnd = False
    while comp_or_frnd == False:
        versus = input("Play vs computer or vs friend?").lower()
        if versus == "computer":
            word = wrd_from_list()
            break

        elif versus == "friend":
            word = input("Let your friend choose a word ")
            break

        else:
            print("Choose between computer or friend")

    # While-loop that makes the user choose how many lives he/she will have
    # Try and except is used so there is no error when anything but a number is used
    lives = 0
    while lives != 5 and lives != 7 and lives != 10:
        try:
            lives = int(input("Choose between 5,7 or 9 lives"))
        except ValueError:
            print("You can only type numbers")

    # Exchanges letters with underscores to create a hidden word
    # A list for guessed letters
    hidden_wrd = len(word) * "_"
    letters_guessed = []

    # A while-loop that works until the user wins or loses
    # The heart of the game
    while lives > 0 and "_" in hidden_wrd:
        print(hidden_wrd)
        guess = input("Guess a letter ").lower()
        if guess in letters_guessed:
            print("You have already guessed this letter")

        # Guess has to be a single letter
        elif len(guess) == 1 and guess.isalpha():
            # Checks if the guessed letter is in the word an replaces the underscore with it
            if guess in word:
                letters_guessed.append(guess)
                for i in range(0, len(word)):
                    if word[i] == guess:
                        hidden_wrd = (
                            hidden_wrd[0:i]
                            + guess
                            + hidden_wrd[i + 1 : len(hidden_wrd)]
                        )
                print(f"This letter is correct")

            # Removes a life and adds the input into guessed letters list
            else:
                letters_guessed.append(guess)
                lives -= 1
                print("This letter is incorrect")
                print(f"You have already guessed these letters {letters_guessed}")
                print(f"You have {lives} guesses left")

        else:
            print("Your guess has to be a single letter! ")

    # Win or lose
    if lives == 0:
        print("You lose")
    else:
        print("You win")

    # Asks if the user wants to play again
    again = input("Do you want to play again?").lower()
    if again == "yes":
        game()
    elif again == "no":
        print("Ok, have a nice day")
    else:
        print("I guess not")


game()
