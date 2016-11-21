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






# ================ bis hier sind wir gekommen ==================

# Schleifen mit while
zahl = 0

while zahl < 10:
    print(zahl)
    zahl += 1


bedingung = True

while bedingung:            # würde theoretische ewig weiterlaufen
    print("Hallo")
    break                   # Schleife abbrechen




# nur gerade Zahlen ausgeben
i = 0

while i < 10:
    if i % 2 == 0:
        print(i)
    i += 1


# das gleiche nur anders
i = 0

while i < 10:
    print(i)
    i += 2








