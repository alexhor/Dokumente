# Programm zur Ausgabe von Multiplikationstafeln

# Eingabe erhalten
number = int(input("Dieses Programm gibt eine Multiplikationstafel aus!\nGeben Sie die gewünschte Zahl ein: "))

# leere Zeile ausgeben
print()

for factor in range(1, 11):     # 1 als Startwert, 11 als Stoppwert der NICHT mehr dabei ist
    print(factor, "*", number, "=", factor * number)    # Berechnung und Ausgabe in einem
