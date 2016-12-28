import os, sys

def clear():
    if 'idlelib.run' in sys.modules:
        # clears the IDLE screen
        print("\n" * 100)
    else:
        # clears the console screen
        clear = lambda: os.system('cls')
        clear()
