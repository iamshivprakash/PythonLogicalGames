alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
# def encrypt(plain_text, shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         # Use List Index in Python
#         position=alphabet.index(letter)
#         new_position=position+shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"The encoded text is {cipher_text}")
# def decrypt(cipher_text, shift_amount):
#     plain_text=""
#     for letter in cipher_text:
#         position=alphabet.index(letter)
#         new_position=position-shift_amount
#         new_letter=alphabet[new_position]
#         plain_text+=new_letter
#     print(f"The decoded text is {plain_text}")
# if direction=='encode':
#     encrypt(text,shift)
# else:
#     decrypt(text,shift)

# Combine encrypt() and decrypt() functions into
# a single function called caesar()
def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position = position+shift_amount
            end_text += alphabet[new_position]
        else:
            end_text+=char
    print(f"The {direction}d text is {end_text}")
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("Type your message:\n").lower()
    shift =int(input("Type the shift number:\n"))
    shift = shift%26
    caesar(text, shift, direction)
    result=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n'")
    if result=='no':
        should_continue=False
        print("Goodbye.")



