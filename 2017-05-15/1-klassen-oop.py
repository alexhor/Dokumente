# Klassen - Objektorientierte Programmierung


# Kurze Erläuterung:
#
# Bisher haben wir unsere Programme stets mittels Unterteilung
# in verschiedene Funktionen strukturiert und wiederverwendbar
# gemacht. Wir haben also FUNKTIONSORIENTIERT gearbeitet.
#
# Nun lernen wir die höchste und abstrakteste Form der Programmierung
# kennen: das OBJEKTORIENTIERTE Programmieren. Wie der Name schon
# sagt stehen hierbei Objekte im Vordergrund.


# ----- Einführung in Klassen ---------------------------------------

# Wir betrachten zunächst ein einfaches Beispiel. Eine Bank möchte
# eine Datenbank über ihre Konten anlegen. Die Daten eines einzelnen
# Kontos sollen hierbei innerhalb eines Objektes hinterlegt sein.
#
# Mit unserem bisherigen Wissen, stehen uns mehrere Lösungswege für
# dieses Problem zur Verfügung. Bsp.: Dictionary oder Liste
#
# Für jedes Konto erstellen wir also bspw. ein eigenes Dictionary

konto_a = {
        "kontoinhaber": "Robin Grether",
        "kontonummer": 123472,
        "kontostand": 1007.59
        }

konto_b = {
        "kontoinhaber": "Max Mustermann",
        "kontonummer": 123473,
        "kontostand": 1295.65
        }

# Ein solches Dictionary stellt nun stets ein Konto dar.
#
# Mit einheitlichen Methoden könnten wir auf den Objekten operieren.
#
# In diesem Beispiel könnten dies die Methoden einzahlen() und
# auszahlen() sein:

def einzahlen(konto, geldmenge):
    if geldmenge <= 0:              # keine negativen Beträge einzahlen
        return False
    else:
        konto["kontostand"] = konto["kontostand"] + geldmenge
        return True

def auszahlen(konto, geldmenge):
    if geldmenge <= 0:                      # keine negativen Beträge auszahlen
        return False
    elif konto["kontostand"] < geldmenge:   # nicht mehr auszahlen, als auf dem Konto ist
        return False
    else:
        konto["kontostand"] = konto["kontostand"] - geldmenge
        return True

# Beim Operieren auf unseren Daten gibt es nun ein Problem und einen
# Schönheitsfehler:
#
# Da der Parameter konto der beiden Methoden jeweils ein Dictionary
# sein soll und Dictionarys prinzipiell das Speichern allerlei
# unterschiedlicher Objekte erlauben (nicht nur Zahlen/Zeichenketten),
# kann es vorkommen, dass aus Versehen ein nicht Zahlwert unter dem
# Schlüssel "kontostand" eingespeichert wird. Dies ist vor allem dann
# nicht unwahrscheinlich, wenn andere Personen mit unserem Code arbeiten.
#
# Tritt dieser Fall nun ein, so werden unsere Funktionen, wie sie oben
# definiert sind, unbrauchbar, da diese dann nur noch Fehler produzieren.
#
# Selbstverständlich könnten wir dutzende if-else und try-except Blöcke
# einfügen, um jegliche Fälle abzufangen, sodass unsere Methode
# zumindest keine Fehler produziert. Jedoch können wir trotzdem nicht
# verhindern, dass eine Zeichenkette oder sonst etwas anderes als ein
# reiner Zahlenwert unter "kontostand" eingespeichert wird.
#
# Desweiteren ist aus unserem Code zunächst nur schwer ersichtlich,
# dass die Datenstruktur unserer Dictionarys direkt mit den beiden
# definierten Funktionen zusammenhängt. Denn für Python selbst sind
# die beiden Funktionen genauso unabhängig davon, wie die Funktionen
# print() oder input().
#
# Es muss hierfür doch aber eine Lösung geben?!
#
# Die Lösung sind KLASSEN!!!

# Was sind Klassen?
#
# Klassen sind Baupläne aus denen Python nach unseren Vorstellungen
# spezielle Objekte erzeugt. Diese Objekte können wir exakt an unsere
# Anforderungen und Wünsche anpassen, sodass wir bspw. obiges Problem
# sehr einfach und übersichtlich lösen können :D

# Wie sieht die Klasse nun aus?

class Konto:                # mit dieser Anweisung erzeugen wir eine
                            # neue Klasse (also einen neuen Bauplan)

    def __init__(self, kontoinhaber, kontonummer, kontostand=0.0):      # mit dieser speziellen Funktion namens __init__()
                                                                        # initialisieren wir ein Objekt;
                                                                        # diese Funktion wird immer dann aufgerufen, wenn
                                                                        # ein neues Objekt erzeugt wird
                                                                        #
                                                                        # der Parameter self stellt dabei das erzeugte Objekt
                                                                        # dar
        
        if isinstance(kontoinhaber, str) and isinstance(kontonummer, int) and isinstance(kontostand, (int, float)):
                            # wir überprüfen zunächst die Parameter auf korrekte Objekttypen
                    
            self.kontoinhaber = kontoinhaber
            self.kontonummer = kontonummer
            self.kontostand = float(kontostand)         # Kontostand soll stets eine Kommazahl sein

        else:
            raise Exception

    # nun weiß Python wie es ein Objekt des neuen Datentyps Konto erstellt,
    # wir können allerdings noch weitermachen, die Funktionen fehlen ja noch

    def einzahlen(self, geldmenge):         # innerhalb der Klasse können wir Funktionen erstellen,
                                            # welche direkt mit den aus der Klasse erzeugten Objekten
                                            # zusammenhängen;
                                            # diese Funktionen können nur mit einem entsprechenden
                                            # Objekt der Klasse aufgerufen werden
        if not isinstance(geldmenge, (int, float)):
            return False
        elif geldmenge <= 0:                # auch hier überprüfen wir wieder die Datentypen der Parameter
            return False                    # sowie mögliche aber nicht sinnvolle Werte
        else:
            self.kontostand = self.kontostand + float(geldmenge)
            return True


    def auszahlen(self, geldmenge):         # wie man sieht, erhält jede Funktion innerhalb der Klasse
                                            # zusätzlich den Parameter self;
                                            # dieser steht jeweils für das Objekt der Klasse, auf dem
                                            # gerade operiert wird
        if not isinstance(geldmenge, (int, float)):
            return False
        elif geldmenge <= 0:
            return False
        elif self.kontostand < geldmenge:
            return False
        else:
            self.kontostand = self.kontostand - float(geldmenge)
            return True


    def daten_ausgeben(self):               # zuletzt noch eine zusätzliche Methode, damit wir gleich
                                            # eine bessere Veranschaulichung bekommen
        print("Kontoinhaber: " + self.kontoinhaber)
        print("Kontonummer:  " + str(self.kontonummer))
        print("Kontostand:   " + str(self.kontostand))



# Nun ist unsere Klasse, also unser Bauplan, fertig.
# Jetzt geht es daran Objekte zu erstellen xD

konto1 = Konto("Robin Grether", 123472, 1007.59)        # hier wird nun jeweils ein neues Objekt erzeugt und
konto2 = Konto("Max Mustermann", 123473, 1295.65)       # anschließend __init__() mit unseren Angaben aufgerufen

konto1.daten_ausgeben()                                 # und so rufen wir die Funktionen auf, die wir innerhalb
konto2.daten_ausgeben()                                 # der Klasse definiert haben;
                                                        # das Objekt das vor dem . steht ist dabei automatisch der
                                                        # Parameter self, welcher in den Klammern hier nie angegeben
                                                        # werden darf

# Angenommen, es soll nun von konto1 nach konto2 Geld
# überwiesen werden. Eine solche Funktion haben wir
# leider innerhalb der Klasse noch nicht definiert.
#
# Nun müssen wir ja doch wieder eine Funktion außerhalb
# der Klasse erzeugen!

def ueberweisen(konto_a, konto_b, geldmenge):

    if isinstance(konto_a, Konto) and isinstance(konto_b, Konto) and isinstance(geldmenge, (int, float)):
        if konto_a.auszahlen(geldmenge):
            konto_b.einzahlen(geldmenge)
            return True
    return False

# Erneut ist jedoch auf den ersten Blick nicht sofort ersichtlich,
# dass unsere Funktion konkret zu unserer Datenstruktur Konto
# gehört. Irgendwie muss es doch einen Weg geben, Klassen nach ihrer
# Definition noch zu erweitern?


# Die Lösung ist die VERERBUNG!

# Wir können Klassen nach ihrer Definition NICHT mehr verändern.
# Wir können allerdings eine weitere Klasse erstellen, welche unsere
# erste Klasse erweitert und auch vollkommen mit dieser kompatibel
# ist.


class ErweitertesKonto(Konto):          # in der Klammer steht die Klasse, die wir erweitern (=Superklasse)

    def __init__(self, kontoinhaber, kontonummer, kontostand=0.0):
        super().__init__(kontoinhaber, kontonummer, kontostand)

        # unsere neue Klasse hat keine weiteren Attribute,
        # die Initialisierung lassen wir daher unsere Superklasse erledigen

    # die Methoden der Superklasse (hier: einzahlen(), auszahlen(), daten_ausgeben())
    # sind auch automatisch für unsere neue Klasse definiert, wir brauchen diese
    # nicht erneut zu definieren

    def ueberweisen(self, empfaenger_konto, geldmenge):     # nun unsere neue Funktion
        if isinstance(empfaenger_konto, Konto) and isinstance(geldmenge, (int, float)):
            if self.auszahlen(geldmenge):                   # ein Paar Überprüfungen müssen hier auch wieder sein
                empfaenger_konto.einzahlen(geldmenge)       
                return True
        return False
    

# Nun ist unsere erweiterte Klasse fertig :D
# Ran gehts ans Objekte erstellen.
        
        
konto3 = ErweitertesKonto("Dagobert Duck", 123474, 1750076.10)

konto3.ueberweisen(konto1, 500.00)              # wir können auch an das ursprüngliche Konto überweisen

konto1.daten_ausgeben()
konto3.daten_ausgeben()

#konto1.ueberweisen(konto3, 500.00)              # das funktioniert nicht, da konto1 nur ein Konto und kein
                                                # erweitertes Konto ist


# Wofür verwendet man Vererbung im Allgemeinen?
#
# 1. Teilen von Code
# Zwei Subklassen einer gemeinsamen Superklasse können sich so
# bestimmte Funktionen teilen.
#
# 2. Sinngemäße Vererbung
# Eine Subklasse kann auch sinngemäß von einer Superklasse geerbt
# sein. Beispiel:

class Tier:
    pass

class Hund(Tier):
    pass

class Dackel(Hund):
    pass

class Katze(Tier):
    pass

# D.h. jeder Dackel ist ein Hund, jeder Hund ist ein Tier, jeder Dackel ist ein Tier, jede Katze ist ein Tier
# ABER nicht jeder Hund ist ein Dackel, nicht jedes Tier ist ein Hund, ...


# Leider haben wir nun immernoch ein kleines Problem:

konto1.kontostand = 1000000.00

# Wir können die Daten einfach ändern, auch ohne einzahlen() oder auszahlen()
# aufrufen zu müssen.


# Die Lösung ist EINGESCHRÄNKTE SICHTBARKEIT!

class SicheresKonto:

    def __init__(self, kontoinhaber, kontonummer, kontostand=0.0):        
        if isinstance(kontoinhaber, str) and isinstance(kontonummer, int) and isinstance(kontostand, (int, float)):
            self.__kontoinhaber = kontoinhaber
            self.__kontonummer = kontonummer            # beginnt der Variablenname mit __
            self.__kontostand = float(kontostand)       # so ist die Variable privat
        else:
            raise Exception

    def einzahlen(self, geldmenge):
        if not isinstance(geldmenge, (int, float)):
            return False
        elif geldmenge <= 0:                
            return False                    
        else:
            self.__kontostand = self.__kontostand + float(geldmenge)
            return True


    def auszahlen(self, geldmenge):         
        if not isinstance(geldmenge, (int, float)):
            return False
        elif geldmenge <= 0:
            return False
        elif self.__kontostand < geldmenge:
            return False
        else:
            self.__kontostand = self.__kontostand - float(geldmenge)
            return True


    def daten_ausgeben(self):               
        print("Kontoinhaber: " + self.__kontoinhaber)
        print("Kontonummer:  " + str(self.__kontonummer))
        print("Kontostand:   " + str(self.__kontostand))


konto4 = SicheresKonto("Lukas Baier", 123476, 1.00)

konto4.daten_ausgeben()
konto4.einzahlen(0.50)
konto4.daten_ausgeben()

konto4.__kontostand = 500      # verändert nichts an der eigentlichen Variable

konto4.daten_ausgeben()

# Wenn wir die Variablen des Objektes mit __ beginnen,
# so sind diese privat und können nur von Funktionen
# innerhalb der Klasse, zu der das Objekt gehört,
# aufgerufen oder verändert werden.


# Abschluss
#
# Mit Klassen können wir Baupläne für eigene Objekte bzw. Datenstrukturen erzeugen.
# Die erzeugbaren Objekte werden dabei genau nach unseren Vorstellungen geformt und
# direkt mit den für die bestimmten Funktionen verknüpft.
#
# Mit Vererbung können wir Code zwischen Klassen teilen und Verwandtschaften von
# Klassen bzw. den erzeugbaren Objekten sinngemäß darstellen.
#
# Klassen sind somit ein einfaches, praktisches, flexibles und mächtiges Werkzeug,
# mit dem wir Gegenstände und Datenstrukturen innerhalb unseres Programmes
# verwalten und strukturieren können.



# Übungen
#
# Schreibe mithilfe der Vorlage selbst eine Klasse für ein solches Konto.
