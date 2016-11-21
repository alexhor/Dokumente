# Wahrheitswerte

a = True

b = False

print(a, b)

# Vergleiche geben IMMER Wahrheitswerte zurück
c = 7 > 5
d = 7 < 5
e = 7 == 5
print(c, d, e)

# auch Wahrheitswerte kann man umwandeln
print(str(True))

f = bool("True")
print(f)


# Verrechnen von Wahrheitswerten
g = True == True
print(g)

# Verknüpfen von Wahrheitswerten
h = True or False
print(h)

i = True and False
print(i)

j = not False
print(j)

# das ganze mit Vergleichen
k = (7 == 7) or (5 > 6)
print(k)

# beliebige Kombinationen
l = (True == False) and (not(7 >= 5))
print(l)





