# Programm zur Prüfung des Geburtstages

def create_date(day, month, year):
    return {"day": day, "month": month, "year": year}


def get_today():
    import time
    today = time.localtime()
    return create_date(today[2], today[1], today[0])


def get_month_from_name(month_name):
    """ gets a month's number in the year from its name
    """
    months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    return months.index(month_name) + 1     # Januar soll 1 sein und nicht 0


def input_date():
    day = int(input("Tag: "))
    month = input("Monat: ")
    try:
        month = int(month)
    except ValueError:
        month = get_month_from_name(month)
    year = int(input("Jahr: "))
    return create_date(day, month, year)
    

def input_birthday():
    # Eingaben vom Nutzer erhalten
    print("Geben Sie Ihren Geburtstag ein:")
    return input_date()


def is_today(date, ignoreYear):
    """ indicates whether some date is today

    
    """
    today = get_today()
    if ignoreYear:
        return (date["day"] == today["day"]) and (date["month"] == today["month"])
    else:
        return (date["day"] == today["day"]) and (date["month"] == today["month"]) and (date["year"] == today["year"])


def is_past(date, ignoreYear):
    """ indicates whether some date is already past

    
    """
    today = get_today()
    if ignoreYear:
        return (date["month"] < today["month"]) or ((date["month"] == today["month"]) and (date["day"] < today["day"]))
    else:
        return (date["year"] < today["year"]) or ((date["year"] == today["year"]) and ((date["month"] < today["month"]) or ((date["month"] == today["month"]) and (date["day"] < today["day"]))))


date = input_birthday()

if is_past(date, True):
    print("Sie hatten dieses Jahr bereits Geburtstag.")
elif is_today(date, True):
    print("HERZLICHEN GLÜCKWUNSCH!")
    print("Sie haben heute Geburtstag!")
else:
    print("Sie hatten dieses Jahr noch nicht Geburtstag.")

if is_past(date, True) or is_today(date, True):
    print("Sie sind", 2016 - date["year"], "Jahre alt.")
else:
    print("Sie sind", 2015 - date["year"], "Jahre alt.")



# import doctest
# doctest.testmod()
