class Konto:

    def __init__(self, kontoinhaber, kontonummer, kontostand=0.0):
        if isinstance(kontoinhaber, str) and isinstance(kontonummer, int) and isinstance(kontostand, (int, float)):
            self.__kontoinhaber = kontoinhaber
            self.__kontonummer = kontonummer
            self.__kontostand = float(kontostand)
        else:
            raise Exception

    def einzahlen(self, geldmenge):
        pass

    def auszahlen(self, geldmenge):
        pass
    
    def ueberweisen(self, empfaenger_konto, geldmenge):
        pass

    def daten_ausgeben(self):
        pass

    def zinsen_bekommen(self, zinssatz):
        pass

