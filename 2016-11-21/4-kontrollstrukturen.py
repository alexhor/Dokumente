# Kontrollstrukturen

# Bedingungen mit if

zahl1 = 7
zahl2 = 5

if zahl1 > zahl2:
    print(zahl1, "ist größer als", zahl2)


wahrheitswert = False

if wahrheitswert:           # kann auch direkt ein Wahrheitswert sein
    print("Wahrheitswert ist True")


# ansonsten
if zahl1 > zahl2:
    print(zahl1, "ist größer als", zahl2)
else:
    print(zahl1, "ist nicht größer als", zahl2)     # 'kleiner als' wäre hier NICHT richtig


# mehrere Bedingungen
if zahl1 > zahl2:
    print(zahl1, "ist größer als", zahl2)
elif zahl1 == zahl2:
    print(zahl1, "ist gleich", zahl2)
else:
    print(zahl1, "ist kleiner als", zahl2)          # jetzt ist 'kleiner als' korrekt
