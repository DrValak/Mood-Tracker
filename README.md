# Daily Mood Encryptor (CLI)

## Overview

**Daily Mood Encryptor** is a simple command-line tool for tracking your daily mood securely. Each entry is encrypted using AES-GCM and protected by a password you choose. You can add new mood entries or view your entire mood history—always encrypted at rest.

---

## Features

- **Add Entry:**  
  - Prompts for a mood rating (1–10) and an optional note.
  - Asks for your password at launch.
  - Encrypts and appends the entry (with timestamp) to a local file.
- **View Entries:**  
  - Use the `view` command to see your mood history.
  - Prompts for your password, decrypts, and displays all entries in plain text.
- **Strong Encryption:**  
  - Uses AES-GCM for authenticated encryption.
  - Each entry uses a unique IV for security.

---

## How It Works

- **File Format:**  
  Each line in the data file contains:  
  `IV | ciphertext | tag` (all base64-encoded and separated by `|`).

- **Encryption:**  
  - When adding an entry, the program generates a random IV.
  - The entry (timestamp, rating, note) is encrypted with AES-GCM using your password-derived key.
  - The IV, ciphertext, and authentication tag are stored.

- **Decryption:**  
  - On `view`, you enter your password.
  - The program derives the key, reads each line, and decrypts the entries for display.

---

## Usage

### 1. Add a Mood Entry

```sh
python3 mood_encryptor.py
```
- Enter your password (used to encrypt/decrypt your data).
- Enter your mood rating (1–10).
- Optionally, add a note.

### 2. View Mood History

```sh
python3 mood_encryptor.py view
```
- Enter your password.
- All past entries are decrypted and shown in plain text.

---

## Requirements

- Python 3.6+
- [cryptography](https://cryptography.io/en/latest/) library  
  Install with:  
  ```sh
  pip install cryptography
  ```

---

## Example

**Adding an entry:**
```
$ python3 mood_encryptor.py
Enter password: ******
Mood rating (1-10): 7
Optional note: Feeling productive!
Entry saved securely.
```

**Viewing entries:**
```
$ python3 mood_encryptor.py view
Enter password: ******
2024-05-10 09:00 | Mood: 7 | Note: Feeling productive!
2024-05-09 21:00 | Mood: 5 | Note: Tired but okay.
...
```

---

## Security Notes

- Your data is only as secure as your password—choose a strong one!
- The program never stores your password, only a key derived from it.
- Each entry is encrypted with a unique IV for maximum security.

---

## Author

Fabio Machado