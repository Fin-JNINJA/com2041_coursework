import string
ciphertext = "Sokad bgaz vxkbktox wak makxox."

a_len = len(string.ascii_lowercase)
for i in range(a_len):
    plaintext = ""
    for cipher_letter in ciphertext:
        upper = False
        if cipher_letter in string.ascii_letters:
            if cipher_letter in string.ascii_uppercase:
                cipher_letter = cipher_letter.lower()
                upper = True
            # do conversion and mod here
            cipher_letter = string.ascii_lowercase[(
                string.ascii_lowercase.index(cipher_letter) + i
            ) % (a_len)]
            if upper:
                # see if i can remove str once conversion is done
                cipher_letter = cipher_letter.upper()
        plaintext += cipher_letter
    print(str(i) + ": " + plaintext)
# gives: Mieux vaut prevenir que guerir.
# key: 20
