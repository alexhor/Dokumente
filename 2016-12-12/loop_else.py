import random

# guessing a number
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("Neue Zahl: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Zahl zu groß")
        elif guess < to_be_guessed:
            print("Zahl zu klein")
    else:
        print("Schade, Sie geben also auf!")
        break
else:
    print("Glückwunsch! Das war's!")

#
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print( n, ' = ', x, ' * ', int(n/x))
            break
    else:
        # loop fell through without finding a factor
        print(n, 'ist eine Primzahl')
