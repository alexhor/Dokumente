
# KGN - Chat Protokoll


Version: 0.1  
Autor: David Lang  
Letzte Änderung: David Lang (2017-03-12_21:00)  

## Begriffe


Nachricht:  
Gesamter String, der übertragen wird.  
Nachrichtentext:  
Inhalt der Nachricht, der Übertragen werden soll  

## Festlegungen


  * Als Datenformat wird JSON verwendet. 
  * Als Zeichenkodierung wird utf-8 verwendet.

## Protokoll

Darstellung erfolgt so:

    Key: Datentyp  
    Beschreibung  

Jede Nachricht muss unter allen Umständen folgende Daten enthalten:

 
####nachrichten_id: number 
Gibt an, welcher Typ von Nachricht zu erwarten ist. Definiert auch, welche Keys die Nachricht besitzen muss.  
####sender_id: string
Gibt an, von wem die Nachricht kommt. Dieser Wert muss einmalig sein. Kann z.B. der Klarname ("Arthur Dent") oder Benutzername ("adent42") sein.
####zeitstempel: number
Gibt an, zu welcher Zeit die Nachricht abgesendet wurde. Wird in Unixzeit angegeben.
####protokoll_version: string
Gibt an, welche Version des Protokolls verwendet wird.

###Beispiel:
    {
      "nachrichten_id": 0,
      "sender_name": "ArthurDent42",
      "zeitstempel": 314159265,
      "protokoll_verion": "0.1"
    } 

### Nachrichtentyp 1 - Textnachricht

Jede Nachricht mit der nachrichten_id == 1 muss unter allen Umständen folgende Daten enthalten: 

####text: string
Enthält den Inhalt der Nachricht, der übertragen wird.
####text_länge: number
Gibt an, wie Lang der gesendete Test ist.
####verschlüsselung: object
#####algorithmus: string
Gibt an, welcher Verschlüsselungsalgorithmus verwendet wird.
#####parameter: array
Gibt an, mit welchem Parameter die Verschlüsselung eingesetzt wird. Ist ein Array. (z.B. bei Caesar wird nur ein Wert benötigt.

###Beispiel:
    {
      "nachrichten_id": 1,
      "text": "Keine Panik!",
      "text_länge": 12,
      "verschlüsselung": 
      {
        "algorithmus": "caesar",
        "parameter": [26]
      },
      "sender_name": "ArthurDent42",
      "zeit_stempel": 314159265,
      "protokoll_verion": "0.1"
    }
   
