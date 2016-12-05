# Datenstrukturen - Listen

# sortierte Liste
a = [0, 1, 2, 3, 4]

# eine Liste kann verschiedene Datentypen enthalten
b = ["Robin", "Grether", 18, 9, 1998]

# auf einen Eintrag der Liste zugreifen
print(b[1])         # gibt "Grether" aus

#      #0     #1      #2     #3    #4
c = ["some", 0.5, "objects", 16, "..."]

# Objekt wieder erhalten
print(c[0])

# Länge einer Liste
length = len(c)

# Objekte hinzufügen
a.append(5)
a[len(a):] = [6]

# Listen erweitern
a.extend([8, 9, 10])
a[len(a):] = [11, 12, 13]

print(a)

# Objekte ändern
b[1] = "Was auch immer"

# Objekte einfügen
a.insert(7, 7)  # an der 7. Stelle die Zahl 7 einfügen

print(a)


# Objekte entfernen

# - entweder das Objekt angeben
c.remove("some")

# - oder die Stelle angeben
del c[1]

print(c)



# Stelle eines Objekts erhalten
index = c.index("...")

# Liste löschen
c.clear()

del a[:]




