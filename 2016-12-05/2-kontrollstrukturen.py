# Schleifen mit for

# wir kennen bereits
i = 0
while i < 10:
    print(i)
    i += 1


# neuer Weg mit for
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i)


# einfacher mit range()
for i in range(0, 10, 1):       # Startwert, Stoppwert, Schrittweite
    print(i)                    # ACHTUNG: Stoppwert ist NICHT teil der Liste

for i in range(0, 10):          # Schrittweite standardmäßig 1
    print(i)

for i in range(10):             # Startwert standardmäßig 0
    print(i)


# auch abwärts möglich
for i in range(10, 0, -2):      # 10 ist jetzt teil der Liste
    print(i)                    # 0 hingegen nicht mehr


# auch mit Listen möglich
a = ["a", "b", "c"]

for element in a:
    print(element)


