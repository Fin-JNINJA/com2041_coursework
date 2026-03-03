import string
ciphertext = ""
plaintext = ""

string.ascii_lowercase
for cipher_letter in ciphertext:
    upper = False
    if cipher_letter in string.ascii_letters:
        if cipher_letter in string.ascii_uppercase:
            cipher_letter = cipher_letter.lower
            upper = True
        # do conversion and mod here
        if upper:
            # see if i can remove str once conversion is done
            cipher_letter = str(cipher_letter).lower
    plaintext += str(cipher_letter)
