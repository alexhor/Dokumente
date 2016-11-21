# Wiederholung der letzten Stunde

# Ich bin ein Kommentar, das heißt ich werde nicht ausgeführt,
# sondern unterstütze nur bei der Programmierung, indem ich
# Erklärungen und andere Infos über den eigentlichen Code enthalte

# eine einfache Rechnung
7 + 7

# geht auch mit Kommazahlen
7.5 + 2.5

# jetzt geben wir die Ergebnisse mit print() aus
print( 7 + 7 )
print( 7.5 + 2.5 )

# jetzt mal ein paar Zeichenketten "Strings" (str)
print( "Hallo Welt!" )
print("abc" + "def")    # auch hier geht +

# Zeichenketten mit " oder '
print("test")
print('test')

print("Robin erklärte die 'aromatische, elektrophile Substitution'.")

print('Jonas sagt: "Sehr interessant!"')

# Zeichenketten kann man multiplizieren
print("test " + "test " + "test ")
print("test " * 3)

# mehrere Objekte ausgeben
print("test", 17.3, "abcdefg")

# Seperator ändern
print("ich", "bin", "durch", "Punkte", "getrennt", sep=".")

# Objekte mittels Variablen speichern
variable1 = 7.5
variable2 = 2.5

# Variablen verrechnen
summe = variable1 + variable2
print(summe)    # Summe ist 10

# zuerst wird ausgewertet, danach gespeichert
variable2 = 3.5
print(summe)    # Summe ist immernoch 10

# Eingabe erhalten
eingabe = input("Geben Sie etwas ein: ")
# gibt immer eine Zeichenkette zurück, auch wenn nur numerische Symbole enthalten sind

print(eingabe)
