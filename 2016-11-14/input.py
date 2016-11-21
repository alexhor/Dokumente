# introduction
print("Bitte füllen Sie das folgende Formular aus")
# get name
name = input("Vorname: ")
lastname = input("Nachname: ")
fullname = name + ' ' + lastname
# get birth info
birth_year = int(input("Geburtsjahr: "))
birth_place = input("Geburtsort: ")
# calculate age
age = 2016 - birth_year

print("\n")

# print generated info
print("Hallo", fullname + ",")
print("Sie sind", age, "Jahre alt und wurden in", birth_place, "geboren.")
print("Vielen Dank für Ihre Teilnahme an der Umfrage.")
