# Addierer mit += 1

# Eingaben erhalten
a = input("Dies ist ein Addierer!\nGeben Sie a ein: ")
b = input("Geben Sie b ein: ")

# Zeichenketten in Zahlen umwandeln
a = int(a)
b = int(b)

# neue Variable verwenden, Eingaben nicht verändern
result = a

i = 0
if b > 0:               # wenn b größer Null
    while i < b:        # dann Schleife positiv durchlaufen
        result += 1
        i += 1
elif b < 0:             # wenn b kleiner Null
    while i > b:        # dann Schleife negativ durchlaufen
        result -= 1
        i -= 1

print("\nDas Ergebnis ist: " + str(result))

