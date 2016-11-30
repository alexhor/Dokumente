# Schleifen mit while
zahl = 0

while zahl < 10:
    print(zahl)
    zahl += 1

print("\n######################\n")

bedingung = True

while bedingung:            # würde theoretische ewig weiterlaufen
    print("Hallo")
    break                   # Schleife abbrechen

print("\n######################\n")

while False:
    kill_all()

print("\n######################\n")

# nur gerade Zahlen ausgeben
i = 0

while i < 10:
    if i % 2 == 0:
        print(i)
    i += 1

print("\n######################\n")

# das gleiche nur anders
i = 0

while i < 10:
    print(i)
    i += 2
