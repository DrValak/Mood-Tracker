# Mood Tracker GUI

A simple password-protected mood tracker built with Python and Tkinter.  
Your moods are encrypted and stored locally, and you can view your mood history at any time.

---

## Features

- **Password Protection:**  
  Set and check a password to access your mood tracker.

- **Encrypted Mood Storage:**  
  Each mood entry (1-10) is encrypted before being saved to disk.

- **Mood History:**  
  View your full (decrypted) mood history in the app.

- **Simple GUI:**  
  User-friendly interface built with Tkinter.

---

## How It Works

1. **Set Password:**  
   - Enter a password and click "Set Password".  
   - The password is encrypted and saved locally.

2. **Login:**  
   - Enter your password and click "Login".  
   - If correct, you can add your mood for today.

3. **Add Mood:**  
   - Enter a number from 1 (terrible) to 10 (fantastic) and save it.  
   - The mood is encrypted and appended to `mood.txt`.

4. **View Mood History:**  
   - Click "View Mood History" to see all your past moods (decrypted).

---

## File Structure

- `test.py` — Main GUI application.
- `cryptography.py` — Functions for encrypting and decrypting data.
- `mood.py` — Functions for saving and loading moods.

---

## Requirements

- Python 3.x
- Tkinter (included with most Python installations)

---

## How to Run

1. Clone or download this repository.
2. Make sure all `.py` files are in the same folder.
3. Run the app:
    ```sh
    python3 test.py
    ```

---

## Security Note

This project uses a simple Caesar cipher for demonstration purposes.  
For real-world applications, use strong encryption like AES-GCM.

---

## Author

Valak