import base64
import codecs  # This is required for ROT13 encoding

def encode_base64(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def encode_hex(text):
    return text.encode('utf-8').hex()

def encode_rot13(text):
    # Apply ROT13 directly on the string, not the bytes
    return codecs.encode(text, 'rot_13')

def main():
    print("Welcome to the Encoder Program!")
    print("Choose an encoder:")
    print("1. Base64")
    print("2. Hexadecimal")
    print("3. ROT13")

    choice = input("Enter the number of the encoder you want to use: ")

    if choice not in ['1', '2', '3']:
        print("Invalid choice. Exiting.")
        return

    text = input("What would you like to encode? ")

    if choice == '1':
        encoded_text = encode_base64(text)
    elif choice == '2':
        encoded_text = encode_hex(text)
    elif choice == '3':
        encoded_text = encode_rot13(text)
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"\nHere is the encoded version: {encoded_text}")

if __name__ == "__main__":
    main()
