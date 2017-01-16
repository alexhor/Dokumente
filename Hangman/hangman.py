# import the clear function
from lib.clear import clear

def main():
    """main function that runs the whole game

    no tests here, because there is nothing to test here"""
    word = input("Wort zum Erraten eingeben: ")
    word = word.upper(word)
    print_underscores(word)
    # create variables
    wrong_letters = []
    guessed = []
    # main game loop
    while True:
        letter = get_letter()
        if test_letter(letter, word):
            guessed = replace_letter(letter, word, guessed)
        else:
            wrong_letters.append(letter)
            print_hangman(wrong_letters)
        if word_complete(guessed):
            break;
    # the game has been won
    print("You won!")

def print_underscores(word):
    """TODO: fill with your code"""
    pass

def get_letter():
    """TODO: fill with your code"""
    pass

def test_letter(letter, word):
    """TODO: fill with your code"""
    pass

def replace_letter(letter, word, guessed):
    """TODO: fill with your code"""
    pass

def print_hangman(wrong_words):
    """TODO: fill with your code"""
    pass

def word_complete(guessed):
    """TODO: fill with your code"""
    pass

def loading_screen():
    """example for using the function to refresh the screen

    no tests, because this just prints to the screen
    """
    # function for pausing the code
    from time import sleep
    # init loading string
    loading = "Loading "
    # initial screan clearing to avoid conflicts later
    clear()

    # add a dot every second
    for i in range(10):
        loading += ". "
        print(loading)
        sleep(1)
        clear()

    # loading finished
    print("Finished")

# running the example
loading_screen()
