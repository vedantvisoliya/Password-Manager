# 🔐 Password Manager (Python CLI)

A secure, beginner-friendly command-line **Password Manager** built with Python and the `cryptography` module. It uses AES encryption (via Fernet) to store credentials securely, and access is protected by a **master key**, which is created the first time you run the program.

---

## 🛡️ Features

- 🔑 **Master key authentication** to access all features.
- 🔒 AES-based encryption with `cryptography.fernet`.
- ➕ Add account passwords.
- 🔍 View saved passwords.
- ❌ Delete saved passwords.
- 🧠 Master key and passwords are stored separately and securely in `key.key`.
- 💾 Passwords are saved in an encrypted format in `passwords.txt`.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
    git clone https://github.com/vedantvisoliya/Password-Manager.git

    cd Password-Manager
```

### 2. Install Dependencies

```bash
    pip install cryptography
```

### 3. Run the Program

First run the key_function.py to generate the master key and Fernet key.
Then run the main.py

```bash
    python key_function.py
    python main.py
```

🛡️ Security Considerations

    1. The encryption key (key.key) is essential for decrypting saved data. Do not delete or share it.

    2. The master key is encrypted and stored in master.txt. Make sure it is strong and not easily guessable.

    3. All saved passwords are encrypted line-by-line in passwords.txt.

    ❗ This project is intended for educational purposes only. For real-world use, you'd want to:

        1. Store the key securely (e.g., in environment variables or a vault)

        2. Add rate-limiting to prevent brute-force attacks

        3. Hide or obfuscate storage files

---
