# Ausnahmen und ihre Behandlung

# wir kennen schon
input_string = input("Bitte geben Sie eine Zeichenkette ein: ")

#zahl = int(input_string)    # hier könnte ein ValueError auftreten


# wir kennen ebenfalls
summe = 2 + 5           # funktioniert mit Zahlen
gesamt = "ab" + "cd"    # funktioniert ebenfalls mit Zeichenketten

#gesamt2 = "abcd" + 7    # funktioniert nicht mit gemischten Typen
                        # es tritt ein sog. TypeError auf


# Error -> engl. für 'Fehler'

# Error ist eine Art von Ausnahme (engl. 'Exception')

# Ausnahmen behandeln
try:
    zahl = int(input_string)    # dieser Codeblock wird ausgeführt, bis eine Ausnahme auftritt (er wird 'versucht')
    print("Sehr gut! Sie haben eine gültige Ganzzahl eingegeben!")
except:                         # tritt eine beliebige Ausnahme ein, so machen wir hier weiter, anstatt die Ausführung zu beenden
    print("Sie haben keine gültige Ganzzahl eingegeben!")


# Ausnahmen filtern
try:
    # euer Code oder was auch immer
    pass
except TypeError:
    pass
except ValueError:
    pass
# ....



