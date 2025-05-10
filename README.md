# Daily Mood Encryptor (CLI)

## Overview

**Daily Mood Encryptor** is a simple tool for tracking your daily mood securely. Each entry is encrypted using Ceaser cipher and protected by a password you choose. You can add new mood entries.

---

## Features

- **Add Entry:**  
  - Prompts for a mood rating (1–10) and an optional note.
  - Asks for your password at launch.
  - Encrypts and appends the entry (with timestamp) to a local file.
- **View Entries:**  
  - Prompts for your password, decrypts, and displays all entries in plain text.
- **Simple Encryption:**  
  - Uses a Caesar cipher for basic encryption.
  - Each entry is encrypted with a fixed key.

---

## How It Works

- **File Format:**  
  Each line in the data file contains:  
  - Numeric mood number.

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

- Enter your password (used to encrypt/decrypt your data).
- Enter your mood rating (1–10).

### 2. View Mood History

- Enter your password.
- All past entries are decrypted and shown in plain text.

---


---

## Author

Fabio Machado
