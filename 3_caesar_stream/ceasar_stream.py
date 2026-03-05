import string
ciphertext = "LljujlbhxoqjlawnsyjnpkkmzqhjtgxvmsepBrrpeYenoq"
alpha = string.ascii_lowercase
a_len = len(alpha)

output = ""
for initial in range(a_len):
    for key in range(a_len):
        prev = initial
        plaintext = ""
        for i, cipher_letter in enumerate(ciphertext):
            upper = False
            if cipher_letter in string.ascii_letters:
                if cipher_letter in string.ascii_uppercase:
                    cipher_letter = cipher_letter.lower()
                    upper = True
                # do conversion and mod here

                cipher_letter = alpha[(alpha.index(cipher_letter) - key - prev)
                                      % (a_len)]

                # sets previous cipher letter to current ciphered letter
                prev = alpha.index(ciphertext[i].lower())
                if upper:
                    cipher_letter = cipher_letter.upper()
                    # REMOVE BELOW
                    # plaintext += " "
            plaintext += cipher_letter
        # print("aa")
        output += "\n" + str(key) + "," + str(initial) + ": " + plaintext

o = open("3_caesar_stream/ceasar_output.txt", "w")
o.write(output)
o.close()
# 24,5: IcanresisteverythingexcepttemptationOscarWilde
# PUT SPACES IN????
