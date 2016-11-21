# Umwandlungen

eingabeStr = input("Geben Sie Ihr Geburtsjahr ein: ")

# in Ganzzahlumwandeln
eingabeInt = int(eingabeStr)

# rechnen...
alter = 2016 - eingabeInt

print("Alter:", alter)


# geht auch anders rum
text = str(1976)
print(text)

# auch mit Kommazahlen
kommazahl = float("7.5")

print(str(kommazahl + 2.5))     # gibt 10.0 aus

# Kommazahl zu Ganzzahl
ganzzahl = int(kommazahl)
print(ganzzahl)
print(float(ganzzahl))

# kein mathematisch korrektes runden, sondern floor
print(int(0.8))

