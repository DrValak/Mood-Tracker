from cryptography import encrypt, decrypt

KEY = 3

def save_mood(mood): # Function to save the mood
    encrypted_mood = encrypt(mood, KEY) # Encrypt the mood
    with open("mood.txt", "a") as f: # Open the file in append mode
        f.write(encrypted_mood + "\n") # Write the encrypted mood to the file
    print("Mood saved successfully!") # Print success message

def load_moods(): # Function to load moods
    moods = [] # Initialize an empty list to store moods
    try:
        with open("mood.txt", "r") as f: # Open the file to read moods
            for line in f: # Iterate through each line in the file
                decrypted_mood = decrypt(line.strip(), KEY) # Decrypt the mood
                moods.append(decrypted_mood) # Append the decrypted mood to the list
    except FileNotFoundError: # Handle the case where the file does not exist
        print("No moods saved yet.") # Print message if no moods are saved
    return moods # Return the list of moods