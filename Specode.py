mport base64
import codecs

# Updated Morse Code Dictionary with Punctuation
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': '/',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--'
}

REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


# Encoding Functions
def encode_base64(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')


def encode_hex(text):
    return text.encode('utf-8').hex()


def encode_rot13(text):
    return codecs.encode(text, 'rot_13')


def encode_xor(text, key):
    return ''.join(chr(ord(char) ^ key) for char in text)


def encode_caesar(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)
    return ''.join(result)


def encode_morse(text):
    text = text.upper()
    encoded_text = ' '.join(MORSE_CODE_DICT.get(char, '?') for char in text)
    return encoded_text


# Decoding Functions
def decode_base64(encoded_text):
    try:
        return base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
    except Exception:
        return "Invalid Base64 string!"


def decode_hex(encoded_text):
    try:
        return bytes.fromhex(encoded_text).decode('utf-8')
    except Exception:
        return "Invalid hexadecimal string!"


def decode_rot13(text):
    return codecs.encode(text, 'rot_13')


def decode_xor(text, key):
    return ''.join(chr(ord(char) ^ key) for char in text)


def decode_caesar(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift_base - shift) % 26 + shift_base))
        else:
            result.append(char)
    return ''.join(result)


def decode_morse(morse_code):
    decoded_text = ''.join(REVERSE_MORSE_DICT.get(code, '?') for code in morse_code.split(' '))
    return decoded_text.replace('/', ' ')


# Main Loop
def main():
    while True:
        print("\nWelcome to the Encoder/Decoder Program!")
        print("What would you like to do?")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '3':  # Exit condition
            exit_choice = input("Are you sure you want to exit? (y/n): ").lower()
            if exit_choice == 'y':
                print("Goodbye! 👋")
                break
            else:
                continue

        if choice not in ['1', '2']:
            print("Invalid choice. Please choose again.")
            continue

        if choice == '1':  # Encode
            print("\nChoose an encoder:")
            print("1. Base64")
            print("2. Hexadecimal")
            print("3. ROT13")
            print("4. XOR")
            print("5. Caesar Cipher")
            print("6. Morse Code")

            encoder_choice = input("Enter the number of the encoder: ")
            text = input("What would you like to encode? ")

            if encoder_choice == '1':
                encoded_text = encode_base64(text)
            elif encoder_choice == '2':
                encoded_text = encode_hex(text)
            elif encoder_choice == '3':
                encoded_text = encode_rot13(text)
            elif encoder_choice == '4':
                key = int(input("Enter a number key for XOR: "))
                encoded_text = encode_xor(text, key)
            elif encoder_choice == '5':
                shift = int(input("Enter a shift value for Caesar Cipher: "))
                encoded_text = encode_caesar(text, shift)
            elif encoder_choice == '6':
                encoded_text = encode_morse(text)
            else:
                print("Invalid encoder choice.")
                continue

            print(f"\nHere is the encoded version: {encoded_text}")

        elif choice == '2':  # Decode
            print("\nChoose a decoder:")
            print("1. Base64")
            print("2. Hexadecimal")
            print("3. ROT13")
            print("4. XOR")
            print("5. Caesar Cipher")
            print("6. Morse Code")

            decoder_choice = input("Enter the number of the decoder: ")
            text = input("What would you like to decode? ")

            if decoder_choice == '1':
                decoded_text = decode_base64(text)
            elif decoder_choice == '2':
                decoded_text = decode_hex(text)
            elif decoder_choice == '3':
                decoded_text = decode_rot13(text)
            elif decoder_choice == '4':
                key = int(input("Enter the number key used for XOR: "))
                decoded_text = decode_xor(text, key)
            elif decoder_choice == '5':
                shift = int(input("Enter the shift value for Caesar Cipher: "))
                decoded_text = decode_caesar(text, shift)
            elif decoder_choice == '6':
                decoded_text = decode_morse(text)
            else:
                print("Invalid decoder choice.")
                continue

            print(f"\nHere is the decoded version: {decoded_text}")


if __name__ == "__main__":
    main()
