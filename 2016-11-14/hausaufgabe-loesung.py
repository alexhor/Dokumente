# Programm zur Eingabe einiger persönlicher Daten und Ausrechnung des Alters

# Eingaben
vorname = input("Geben Sie Ihren Vornamen ein: ")
nachname = input("Geben Sie Ihren Nachnamen ein: ")
gebOrt = input("Wo sind Sie geboren? ")
gebJahr = input("In welchem Jahr wurden Sie geboren? ")

# Ausgabe der Daten
print("Name:", vorname, nachname)
print("Geburtsort:", gebOrt)
print("Geburtsjahr:", gebJahr)

# ab hier: neuer Teil
gebJahr = int(gebJahr)      # Zeichenkette (str) in Ganzzahl (int) umwandeln      
alter = 2016 - gebJahr      # Alter berechnen
print("Alter:", alter)      # Alter ausgeben
