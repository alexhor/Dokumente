# Module importieren

# ein gesamtes Modul importieren
import time

print(time.localtime())     # Modul angeben


# eine einzelne Funktion aus einem Modul importieren
from time import localtime

print(localtime())          # Modul nicht angeben




# Beispielmodule

# aktuelle Zeit erhalten
import time

current_time = time.localtime()

year = current_time[0]      # Greg. Kalender
month = current_time[1]     # 1 - 12
day = current_time[2]       # 1 - 31
hour = current_time[3]      # 24 Stunden basiert
minute = current_time[4]


# Zufallszahlen erzeugen
import random

# zufällige Kommazahl zwischen 0.0 und 1.0
random.random()

# zufällige Ganzzahl (int) zwischen 0 und 10
zufallszahl = random.randint(0, 10)



