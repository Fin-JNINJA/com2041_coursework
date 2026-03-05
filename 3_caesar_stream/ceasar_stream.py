import string
# "LljujlbhxoqjlawnsyjnpkkmzqhjtgxvmsepBrrpeYenoq" #my one
ciphertext = "FvsjdhazptxrvuuzwqxrqiuyyxnvptmcgllicjztyswimicbttyrhkottqkrhtxxwmuoslbfkkhbiyYcqcfNhetj"
a_len = len(string.ascii_lowercase)

output = ""
for initial in range(a_len):
    prev = initial
    for k in range(a_len):
        plaintext = ""
        for cipher_letter in ciphertext:
            upper = False
            if cipher_letter in string.ascii_letters:
                if cipher_letter in string.ascii_uppercase:
                    cipher_letter = cipher_letter.lower()
                    upper = True
                # do conversion and mod here

                cipher_letter = string.ascii_lowercase[(
                    string.ascii_lowercase.index(
                        cipher_letter) + k + prev
                ) % (a_len)]

                # sets previous cipher letter to current ciphered letter
                prev = string.ascii_lowercase.index(cipher_letter)
                if upper:
                    cipher_letter = cipher_letter.upper()
                    # REMOVE BELOW
                    # plaintext += " "
            plaintext += cipher_letter
        # print("aa")
        output += "\n" + str(k) + "," + str(initial) + ": " + plaintext

o = open("3_caesar_stream/ceasar_output.txt", "w")
o.write(output)
o.close()
