def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            # Shift uppercase letters (A=65 to Z=90)
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Shift lowercase letters (a=97 to z=122)
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Keep spaces, numbers, symbols unchanged
            result += char
    return result

def caesar_decrypt(text, shift):
    # Decrypt is just encrypt with negative shift
    return caesar_encrypt(text, -shift)

def brute_force_decrypt(ciphertext):
    print("\nBrute-forcing all 26 possible shifts:")
    for i in range(26):
        decrypted = caesar_decrypt(ciphertext, i)
        print(f"Shift {i:2}: {decrypted}")

# === Main Program ===
print("=== Caesar Cipher Tool (Encrypt/Decrypt/Brute-Force) ===\n")

while True:
    print("Options:")
    print("1. Encrypt a message")
    print("2. Decrypt with known shift")
    print("3. Brute-force decrypt")
    print("4. Quit")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == '4':
        print("Goodbye! 🔒")
        break
    
    if choice in ['1', '2', '3']:
        message = input("Enter your message: ")
        
        if choice == '1':
            try:
                shift = int(input("Enter shift number (1-25): "))
                encrypted = caesar_encrypt(message, shift)
                print("\nEncrypted message:", encrypted)
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == '2':
            try:
                shift = int(input("Enter shift number used for encryption: "))
                decrypted = caesar_decrypt(message, shift)
                print("\nDecrypted message:", decrypted)
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == '3':
            brute_force_decrypt(message)
    
    else:
        print("Invalid choice! Try again.")