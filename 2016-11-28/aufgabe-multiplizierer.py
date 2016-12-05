# Multiplizierer mit += 1

# Eingaben erhalten
a = input("Dies ist ein Multiplizierer!\nGeben Sie a ein: ")
b = input("Geben Sie b ein: ")

# Zeichenketten in Zahlen umwandeln
a = int(a)
b = int(b)

# Ergebnisvariable erstellen
result = 0

if a == 0 or b == 0:
    pass                    # Satz vom Nullprodukt, also keine Rechnung notwendig
elif (a > 0 and b > 0) or (a < 0 and b < 0):
    i = 0                   # beide positiv oder beide negativ -> Ergebnis positiv
    while i < abs(a):
        j = 0
        while j < abs(b):
            result += 1     # Schleife mit +1 durchlaufen
            j += 1
        i += 1
else:
    i = 0                   # übrig bleibt:
    while i < abs(a):       # eins positiv und eins negativ -> Ergebnis negativ
        j = 0
        while j < abs(b):
            result -= 1
            j += 1
        i += 1

# Ergebnis ausgeben
print("\nDas Ergebnis ist: " + str(result))
