# Programm zur Prüfung des Geburtstages

# Eingaben vom Nutzer erhalten
print("Geben Sie Ihren Geburtstag ein:")
day = int(input("Tag: "))
month = input("Monat: ")
year = int(input("Jahr: "))

months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
month = months.index(month) + 1                 # Januar soll 1 sein und nicht 0

if month < 12 or (month == 12 and day < 5):     # vor Dezember oder vor dem 5. Dezember
    print("Sie hatten dieses Jahr bereits Geburtstag.")
elif month == 12 and day == 5:                  # genau am 5. Dezember
    print("HERZLICHEN GLÜCKWUNSCH!")
    print("Sie haben heute Geburtstag!")
else:                                           # nach dem 5. Dezember bleibt übrig
    print("Sie hatten dieses Jahr noch nicht Geburtstag.")

if month < 12 or (month == 12 and day <= 5):    # vor Dezember oder vor oder am 5. Dezember
    print("Sie sind", 2016 - year, "Jahre alt.")
else:                                           # nach dem 5. Dezember
    print("Sie sind", 2015 - year, "Jahre alt.")

