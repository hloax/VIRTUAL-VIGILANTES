letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
length = len(letters)

def encryption(text, key):
    result = ""
    for char in text:
        if char in letters:
            encrypted_index = (letters.index(char) + key) % length
            result += letters[encrypted_index]
        else:
            result += char
    return result

def decryption(text, key):
    result = ""
    for char in text:
        if char in letters:
            decrypted_index = (letters.index(char) - key) % length
            result += letters[decrypted_index]
        else:
            result += char
    return result

while True:
    # Prompt user:
    print("Hi, please press 'e' to encrypt or 'd' to decrypt")
    user_mode = input("e/d: ").lower()

    if user_mode == "e":
        print("ENCRYPTION \n")
        while True:
            key = int(input("Please enter key (1 to 25): "))
            if 1 <= key <= 25:
                break
            else:
                print("Key must be between 1 and 25. Please try again.")
        text = input("Please enter text to encrypt: ")
        encrypted = encryption(text, key)
        print("Encrypted text: ", encrypted)
        break

    elif user_mode == "d":
        print("DECRYPTION \n")
        while True:
            key = int(input("Please enter key (1 to 25): "))
            if 1 <= key <= 25:
                break
            else:
                print("Key must be between 1 and 25. Please try again.")
        text = input("Please enter text to decrypt: ")
        decrypted = decryption(text, key)
        print("Decrypted text: ", decrypted)
        break

    else:
        print("Only enter 'd' or 'e'. Please try again")
