# Veränderlichkeit von Objekten (engl. 'mutability')


# Vorwort

# Wertzuweisung genau betrachtet
something = "Hallo, ich bin eine Zeichenkette!"

#  ^                            ^
#  |                            |
#  |                            |
#
#  Referenz               tatsächliches Objekt
#
#  Name unter dem           Platz im Arbeitsspeicher
#  wir das Objekt           in dem etwas gespeichert
#  wiederfinden             ist


# weitere Wertzuweisung
other_thing = something

# other_thing und something sind weiterhin unabhängige Referenzen,
# wird eine der beiden erneut verändert (durch Wertzuweisung) bleibt
# die jeweils andere Referenz hiervon unberührt.
#
# other_thing und something referieren allerdings auf das gleiche
# tatsächliche Objekt, also auf die selben Bytes im RAM.


# Hier beginnt nun der Unfug....


# 1) Referenzen sind stets unabhängig voneinander
other_thing = "Fischers Fritz..."

print(something)    # gibt immernoch 'Hallo, ich bin eine Zeichenkette!' aus



# 2) Objekte verhalten sich unterschiedlich

# 2.1) Unveränderliche Objekte (engl. 'immutable')

string1 = "Ich bin ein Satz!"
string2 = string1           # string1 und string2 zeigen nun auf das gleiche Objekt

string2 = string2.upper()   # das Objekt wird scheinbar 'verändert' und erneut zugewiesen

print(string2)              # gibt 'ICH BIN EIN SATZ!' aus

print(string1)              # gibt 'Ich bin ein Satz!' aus

string1.upper()             # nun 'verändern' wir auch string1

print(string1)              # gibt immernoch 'Ich bin ein Satz!' aus

# Zeichenketten (engl. 'strings') sind IMMER UNveränderliche Objekte.
#
# D.h. bei Veränderungen der Zeichenkette selbst (mittels Funktionen, nicht Zuweisungen)
# wird keine wirkliche Änderung vorgenommen, sondern stets eine völlig neue Zeichenkette
# erstellt. Daher zeigen zwei Referenzen nach einer solchen 'Veränderung' auch nicht mehr
# auf das selbe Objekt. Desweiteren muss stets eine Wertzuweisung erfolgen, wenn man die
# Ergenisse einer Funktion der Zeichenkette behalten möchte. Da diese Ergebnisse lediglich
# als Rückgabewert der Funktion vorhanden sind. Die ursprüngliche Zeichenkette bleibt von
# Funktionen wie .upper() unberührt.

# andere unveränderliche Objekte sind:
# int, float, complex, long, bool


# 2.2) Veränderliche Objekte (engl. 'mutable')

list1 = [0, 1, 2, 3, 4, 5]
list2 = list1               # list1 und list2 zeigen nun auf das gleiche Objekt

list2.append(6)             # das Objekt wird tatsächlich verändert

print(list1)                # da list1 auf das gleiche Objekt zeigt,
                            # sind die Änderungen auch hier sichtbar

list1[0] = -1               # gleiches Verhalten bei Wertzuweisungen der Attribute

print(list2)                # auch hier ist die letzte Änderung vorhanden,
                            # da list1 und list2 auf das gleiche Objekt zeigen

# Listen sind IMMER veränderliche Objekte.
#
# D.h. bei Veränderungen der Liste (mittels Funktionen oder Wertzuweisungen der
# Attribute) wird tatsächlich die Liste selbst verändert, also ein neuer Wert
# eingespeichert. Zwei Referenzen zeigen nach solchen Veränderungen also noch
# immer auf das gleiche und veränderte Objekt. Funktionen solcher Objekte verändern
# in der Regel das Objekt selbst. Es ist folglich keine Wertzuweisung mehr nötig
# um die Veränderungen einzuspeichern.

# andere veränderliche Objekte sind:
# array, dictionary



# 3) Folgen für den Programmierer

lower_case = "abc"
lower_case.upper()
print(lower_case)       # gibt 'abc' aus

# --> Bei unveränderlichen Objekten aufpassen, Veränderungen durch Funktionen wirken
#     sich NICHT auf das ursprüngliche Objekt aus.


def some_function(parameter):
    pass                        # tut irgendwas mit parameter

# --> Bei unveränderlichen Objekten kann die Funktion keine sichtbaren Änderungen am
#     übergebenen Parameter durchführen. Sämtliche Änderungen innerhalb der Funktion
#     sind nur für die Funktion sichtbar.

# --> Bei veränderlichen Objekten kann die Funktion sehr wohl sichtbare Änderungen
#     am übergebenen Parameter durchführen. Änderungen innerhalb der Funktion sind
#     auch außerhalb der Funktion sichtbar. Daher sollte man darauf aufpassen, ob
#     eine Funktion einen Parameter wirklich global verändern können sollte.


                            






