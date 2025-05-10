import tkinter as tk # Import tkinter for GUI
from tkinter import messagebox # Import messagebox for error messages
from cryptography import encrypt, decrypt # Import encrypt and decrypt functions from cryptography module
from mood import save_mood, load_moods # Import save_mood and load_moods functions from moods module

stored_encrypted_password = None # Variable to store the encrypted password
KEY = 3 # Key for encryption and decryption

def set_password(): # Function to set a new password
    global stored_encrypted_password # Declare the variable as global to modify it
    password = password_entry.get() # Get the password from the entry field
    if not password: # Check if the password is empty
        messagebox.showerror("Error", "Please enter a password to set.") # Show error message
        return
    stored_encrypted_password = encrypt(password, key=3) # Encrypt the password
    with open("password.txt", "w") as f: # Open the file to store the encrypted password
        f.write(stored_encrypted_password) # Write the encrypted password to the file
    messagebox.showinfo("Password Set", "Password has been set successfully!") # Show success message
    password_entry.delete(0, tk.END) # Clear the entry field

def check_password(): # Function to check the entered password
    global stored_encrypted_password # Declare the variable as global to modify it
    entered_password = password_entry.get() # Get the entered password from the entry field
    if stored_encrypted_password is None:
        # Tenta ler do ficheiro se não estiver em memória
        try:
            with open("password.txt", "r") as f: # Open the file to read the encrypted password
                stored_encrypted_password = f.read() # Read the encrypted password from the file
        except FileNotFoundError: # Handle the case where the file does not exist
            messagebox.showerror("Error", "No password set. Please set a password first.") # Show error message
            return # Show error message
    decrypted_password = decrypt(stored_encrypted_password, key=3) # Decrypt the stored password
    if entered_password == decrypted_password: # Check if the entered password matches the decrypted password
        messagebox.showinfo("Success", "Password is correct!") # Show success message
        open_mood_window()
    else: # If the passwords do not match
        messagebox.showerror("Error", "Incorrect password. Please try again.") # Show error message
    password_entry.delete(0, tk.END) # Clear the entry field

def open_mood_window(): # Function to open the mood window
    mood_window = tk.Toplevel(root) # Create a new window
    mood_window.title("Mood Tracker") # Set the title of the new window
    tk.Label(mood_window, text="How do you feel today? (1 - terrible to 10 - fantastic):").pack(pady=20) # Create a label for the mood entry
    mood_entry = tk.Entry(mood_window) # Create an entry field for the mood
    mood_entry.pack(pady=20) # Add padding around the entry field
    def save_and_close(): # Function to save the mood
        mood = mood_entry.get() # Get the mood from the entry field
        if mood.isdigit() and 1 <= int(mood) <= 10: # Check if the mood is a valid number between 1 and 10
            save_mood(mood)
            messagebox.showinfo("Mood Saved", "Your mood has been saved successfully!")
            mood_window.destroy() # Close the mood window
        else: # If the mood is not valid
            messagebox.showerror("Error", "Please enter a valid mood between 1 and 10.")

    tk.Button(mood_window, text="Save Mood", command=lambda: save_mood(mood_entry.get())).pack(pady=5) # Create a button to save the mood

root = tk.Tk() # Create the main window
root.title("Mood Tracker Login") # Set the title of the window

tk.Label(root, text="Enter Password:").pack(pady=20) # Create a label for the password entry
password_entry = tk.Entry(root, show="*") # Create an entry field for the password
password_entry.pack(pady=20) # Add padding around the entry field
tk.Button(root, text="Set Password", command=set_password).pack(pady=5) # Create a button to set the password
tk.Button(root, text="Login", command=check_password).pack(pady=5) # Create a button to check the password

root.mainloop() # Start the main loop of the GUI
# This code creates a simple GUI application using tkinter that allows the user to set and check a password.