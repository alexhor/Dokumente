# define a function
def print_prim(a, b):
    """prints all prim numbers between the two given numbers
    b
    >>> print_prim(10, 20)
    11 ist eine Primzahl
    13 ist eine Primzahl
    17 ist eine Primzahl
    19 ist eine Primzahl
    >>> print_prim(1, 5)
    1 ist eine Primzahl
    2 ist eine Primzahl
    3 ist eine Primzahl
    """
    for n in range(a, b):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            # loop fell through without finding a factor
            print(n, 'ist eine Primzahl')

# function with return
def get_prim(a, b):
    """returns a list of all prim numbers between the two given numbers
    
    >>> get_prim(10, 20)
    [11, 13, 17, 19]
    """
    output = []
    for n in range(a, b):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            # loop fell through without finding a factor
            output.append(n)
    return output

# function calling another function
def print_prim_fct(a, b):
    """prints all prim numbers between the two given numbers,
    by calling another function

    >>> print_prim(10, 20)
    11 ist eine Primzahl
    13 ist eine Primzahl
    17 ist eine Primzahl
    19 ist eine Primzahl"""
    prims = get_prim(a, b)
    for prim in prims:
        print(prim, 'ist eine Primzahl')

# calling function
print_prim(10, 20)
a = get_prim(10, 20)
print(a)
print_prim_fct(10, 20)

# running tests
if __name__ == "__main__":
    import doctest
    doctest.testmod()
