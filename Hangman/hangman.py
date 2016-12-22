# import the clear function
from lib.clear import clear

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
