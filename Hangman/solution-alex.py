# import the clear function
from lib.clear import clear
# import the hangman render module
from lib.render_hangman import render_hangman
# import other required modules and functions
from time import sleep

# global variables
orig_word = ()
word = letters = wrong_letters = hangman_progress = []

def input_correct(value):
    """ checks if the value the user gave as an input is valid

    >>> input_correct("a")
    True
    >>> input_correct("g")
    True
    >>> input_correct("3")
    False
    >>> input_correct(3)
    False
    >>> input_correct(523)
    False
    >>> input_correct("523")
    False
    >>> input_correct("dsse")
    False
    >>> input_correct("sd")
    False
    >>> input_correct("S")
    False
    >>> input_correct("SD")
    False
    >>> input_correct("3a")
    False
    """
    # check the value is a string
    if type(value) != str:
        return False
    # check the value is just one character long
    if len(value) > 1:
        return False
    # check the value is a letter
    if not value.isalpha():
        return False
    # check the value is lower case
    if not value.islower():
        return False
    # value is valid
    return True

def get_letter():
    """requests the next letter from the user"""
    return input("Your next guess: ")
    
def get_word():
    """request a word from the user"""
    return input("Enter a word for guessing: ")

def check_word(word):
    """checks if a given word is actually a word with just letters

    >>> check_word("a")
    True
    >>> check_word("g")
    True
    >>> check_word("3")
    False
    >>> check_word(3)
    False
    >>> check_word(523)
    False
    >>> check_word("523")
    False
    >>> check_word("dsse")
    True
    >>> check_word("sd")
    True
    >>> check_word("S")
    True
    >>> check_word("SD")
    True
    >>> check_word("3a")
    False
    """
    # check the word is a string
    if type(word) != str:
        return False
    # check the word just contains of letters
    if not word.isalpha():
        return False
    # word is valid
    return True

def print_hangman(letters, max_wrong_letters):
    """print the hangman figure according to the number wrong letters

    no tests here, because this is just printing stuff"""
    # print the actual hangman
    render_hangman(len(letters), max_wrong_letters)
    
    # if there are no wrong letters, just print another blank line
    if len(letters) < 1:
        print()
        return
    
    print(len(letters), " wrong letters: ", end='')
    # print all wrong letters
    for letter in letters:
        print(letter, end=' ')
    # add a line end
    print("\n", end='')

def print_letters_correct(letters):
    """prints all correct letters

    no tests here, because this is just printing stuff"""
     # show the already right guessed letters
    print(len(letters), " right letters: ", end='')
    for letter in letters:
        print(letter, end=' ')
    # end with line break
    print()

def print_word_underscores(orig_word, word):
    """prints the original word an replaces all not yet guessed letters with
    underscores

    no tests here, because this is just printing stuff"""
    # go through every letter in the original word
    for index in range(len(orig_word)):
        # show the letter if it has been guessed already
        if word[index] == -1:
            print('', orig_word[index], '', end='')
        # show an underscore if the letter is still unknown to the player
        else:
            print(' _ ', end='')
    # end with a new line
    print()

def render(orig_word, word, letters_right, letters_wrong, action, max_wrong_letters):
    """renders the game area

    no tests here, because this is just printing stuff"""
    # show the hangman and already guessed wrong letters
    print_hangman(letters_wrong, max_wrong_letters)
    # show already guessed right letter
    print_letters_correct(letters_right)
    # show the current state of the word to be guessed
    print_word_underscores(orig_word, word)

def replace_letter(letter, word, letters_right, letters_wrong):
    """replaces every occurrence of the letter in the word

    >>> word = ['h', 'a', 'l', 'l', 'o']
    >>> letters_right = []
    >>> letters_wrong = []
    >>> replace_letter('a', word, letters_right, letters_wrong)
    True
    >>> word
    ['h', -1, 'l', 'l', 'o']
    >>> letters_right
    ['a']
    >>> letters_wrong
    []
    
    >>> replace_letter('a', word, letters_right, letters_wrong)
    True
    >>> word
    ['h', -1, 'l', 'l', 'o']
    >>> letters_right
    ['a']
    >>> letters_wrong
    []
    
    >>> replace_letter('y', word, letters_right, letters_wrong)
    False
    >>> word
    ['h', -1, 'l', 'l', 'o']
    >>> letters_right
    ['a']
    >>> letters_wrong
    ['y']
    
    >>> replace_letter('y', word, letters_right, letters_wrong)
    False
    >>> word
    ['h', -1, 'l', 'l', 'o']
    >>> letters_right
    ['a']
    >>> letters_wrong
    ['y']
    """
    # check if the letter was detected as right before
    if letter in letters_right:
        return True
    # check if the letter was detected as wrong before
    elif letter in letters_wrong:
        return False
    # init variables
    replaced = False
    # go through the whole word
    for key in range(len(word)):
        # check if the current letter has to be replaced
        if word[key] == letter:
            # replace the letter
            word[key] = -1
            # we replaced something
            replaced = True
    # if the letter was in the word put the letter in the letter right array
    if replaced:
        letters_right.append(letter)
        return True
    # if the letter was not in the word put the letter in the letter wrong array
    else:
        letters_wrong.append(letter)
        return False

def word_solved(word):
    """checks if the given word is completly solved

    >>> word_solved([-1,-1,-1])
    True
    >>> word_solved([-1,"s",-1])
    False
    >>> word_solved("acs")
    False
    >>> word_solved(["a","s","d","s"])
    False
    >>> word_solved([])
    True
    >>> word_solved(2)
    False
    """
    try:
        # go through every letter
        for letter in word:
            # if one letter is not erased yet, the word is not solved yet
            if letter is not -1:
                return False
        # no letter was left over
        return True
    except:
        # a wrong letter was found
        return False

def start(max_wrong_letters):
    """starts a hangman game"""
    max_wrong_letters -= 1
    # initial screen clearing
    clear()
    # run the game until the user cancels it
    while True:
        # ask for a word from the user until he types a correct one
        while True:
            # get a word
            orig_word = get_word()
            # if the word is valid convert it into a list and leave the loop
            if check_word(orig_word):
                word = list(orig_word)
                break;
            else:
                # tell the user that his input was wrong
                clear()
                print("Invalid word, please try again")
        
        # empty the correct and wrong letters from last game
        correct_letters = []
        wrong_letters = []
        # initial screen render
        clear()
        render(orig_word, word, correct_letters, wrong_letters, -1, max_wrong_letters)
        
        # we got a valid word now, so start a guessing round
        while True:
            # get a letter
            letter = get_letter()
            # clear the screen
            clear()
            action = -1
            
            # only continue with the main code if the input is valid
            if input_correct(letter):
                # check if the letter is in the word
                if replace_letter(letter, word, correct_letters, wrong_letters):
                    action = 1
                # the letter wasn't in the word
                else:
                    action = 0
            # check if the user wants to quit the game
            elif letter == 'quit':
                # clean up
                clear()
                # and quit
                return
            # refresh the screen
            render(orig_word, word, correct_letters, wrong_letters, action, max_wrong_letters)

            # if the word is correct, then we are done
            if word_solved(word):
                print("Congratulations! You won!")
                # give the player time to enjoy his victory
                sleep(5)
                # clean up and start a new game
                clear()
                break;
            # if too many wrong letters have been guessed the game ends
            elif len(wrong_letters) > max_wrong_letters:
                print("Game over! Too many wrong letters!")
                # print the correct word
                print("The word was:", orig_word)
                # give the player time to look at the word
                sleep(5)
                # clean up and start a new game
                clear()
                break;
                
# start a game
start(10)

# running tests
if __name__ == "__main__":
    import doctest
    doctest.testmod()
