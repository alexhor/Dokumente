# Programm zur Prüfung des Geburtstages

# Eingaben vom Nutzer erhalten
print("Geben Sie Ihren Geburtstag ein:")
day = int(input("Tag: "))
month = int(input("Monat: "))
year = int(input("Jahr: "))

if month < 11 or (month == 11 and day < 21):    # vor November oder vor dem 21. November
    print("Sie hatten dieses Jahr bereits Geburtstag.")
elif month == 11 and day == 21:                 # genau am 21. November
    print("HERZLICHEN GLÜCKWUNSCH!")
    print("Sie haben heute Geburtstag!")
else:                                           # nach dem 21. November bleibt übrig
    print("Sie hatten dieses Jahr noch nicht Geburtstag.")

if month < 11 or (month == 11 and day <= 21):   # vor November oder vor oder am 21. November
    print("Sie sind", 2016 - year, "alt.")
else:                                           # nach dem 21. November
    print("Sie sind", 2015 - year, "alt.")
