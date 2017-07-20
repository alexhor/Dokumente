# Rotation Encryption


alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = alphabet_lower.upper()


# encrypt a string with the given key
def encrypt(message, key):
    """
    >>> encrypt('abc', 1)
    'bcd'
    >>> encrypt('1Ab', 2)
    '1Cd'
    >>> encrypt('xYz', 5)
    'cDe'
    >>> encrypt('abc', -1)
    'zab'
    """
    encrypted = []
    for character in message:
        encrypted.append(encrypt_character(character, key))
    return "".join(encrypted)


# decrypt a string with the given key
def decrypt(message, key):
    """
    >>> decrypt('bCd', 1)
    'aBc'
    >>> decrypt('1cD', 2)
    '1aB'
    >>> decrypt('cde', 5)
    'xyz'
    >>> decrypt('zab', -1)
    'abc'
    """
    decrypted = []
    for character in message:
        decrypted.append(decrypt_character(character, key))
    return "".join(decrypted)


# encrypt a character with the given key
def encrypt_character(character, key):
    """
    >>> encrypt_character('a', 1)
    'b'
    >>> encrypt_character('z', 1)
    'a'
    >>> encrypt_character('1', 10)
    '1'
    >>> encrypt_character('b', 5)
    'g'
    """
    if character in alphabet_lower:
        return alphabet_lower[(alphabet_lower.index(character) + key) % 26]
    elif character in alphabet_upper:
        return alphabet_upper[(alphabet_upper.index(character) + key) % 26]
    else:
        return character


# decrypt a character with the given key
def decrypt_character(character, key):
    """
    >>> decrypt_character('b', 1)
    'a'
    >>> decrypt_character('A', 1)
    'Z'
    >>> decrypt_character('1', 10)
    '1'
    >>> decrypt_character('g', 5)
    'b'
    """
    if character in alphabet_lower:
        return alphabet_lower[(alphabet_lower.index(character) - key) % 26]
    elif character in alphabet_upper:
        return alphabet_upper[(alphabet_upper.index(character) - key) % 26]
    else:
        return character



#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
