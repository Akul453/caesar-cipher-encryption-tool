# Caesar Cipher Encryption & Decryption Tool 🔐

A simple, educational Python project implementing the classic *Caesar Cipher* — one of the oldest known encryption techniques.  
This tool demonstrates basic symmetric cryptography, the importance of key strength, and how easily classical ciphers can be broken with brute-force attacks.

Built as a beginner cybersecurity project while preparing for *Erasmus Mundus Joint Master's in Cybersecurity* (e.g., CYBERUS, CyberMACS, CYBERSURE), where cryptography is a core focus.

## Features
- *Encrypt* any text message with a custom shift key (1–25)
- *Decrypt* with a known shift
- *Brute-force decryption* — automatically tries all 26 possible shifts to reveal the original message
- Handles uppercase, lowercase letters, spaces, numbers, and special characters
- Interactive menu with loop (keep checking without restarting)
- Basic error handling for invalid inputs

## Why This Project Matters
The Caesar Cipher illustrates key cybersecurity concepts:
- Substitution ciphers and their vulnerabilities
- The role of key space in encryption strength
- Why modern algorithms (like AES or RSA) use much larger keys and complex math
- Practical understanding of brute-force attacks

Perfect hands-on introduction to cryptography fundamentals!

## How to Run
1. Make sure you have *Python 3* installed
2. Clone or download this repository
3. Open a terminal/command prompt in the project folder
4. Run:
   ```bash
   python caesar_cipher.py
