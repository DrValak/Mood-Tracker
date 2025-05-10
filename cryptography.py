def encrypt(text, key):
    """
    Encrypts the given text using a simple Caesar cipher with the provided key.
    
    :param text: The text to encrypt.
    :param key: The number of positions to shift each letter.
    :return: The encrypted text.

    """
    encrypted_text = [] # Initialize an empty list to store the encrypted characters
    
    for char in text: # Iterate through each character in the input text
        if char.isalpha(): # Check if the character is a letter
            shift = key % 26 # Normalize the key to be within 0-25 (the range of the alphabet)
            if char.islower(): # Check if the character is lowercase
                base = ord('a') # ASCII value of 'a'
            else:
                base = ord('A') # ASCII value of 'A'
            encrypted_char = chr((ord(char) - base + shift) % 26 + base) # Encrypt the character
            encrypted_text.append(encrypted_char) # Append the encrypted character to the list
        else:
            encrypted_text.append(char) # Non-alphabetic characters remain unchanged
    
    return ''.join(encrypted_text) # Join the list of characters into a single string

def decrypt(text, key):
    """
    Decrypts the given text using a simple Caesar cipher with the provided key.
    
    :param text: The text to decrypt.
    :param key: The number of positions to shift each letter.
    :return: The decrypted text.

    """
    return encrypt(text, -key) # Decrypting is just encrypting with the negative key

def create_password(password, key=3):
    """
    Creates a password using the encrypt function.
    
    :return: The encrypted password.

    """

    key = 3 # Shift value for the Caesar cipher
    encrypted_password = encrypt(password, key) # Encrypt the password
    return encrypted_password # Return the encrypted password