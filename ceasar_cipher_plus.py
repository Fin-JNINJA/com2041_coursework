import string
ciphertext = "La olc ogrr hcd akchcmgza ogrr luta dc uqchgza. - Kchvykgyi"
max = 26


def ceaser_plus(a, b, c, ciphertext) -> str:
    a_len = len(string.ascii_lowercase)
    output = ""
    for i in range(a_len):
        plaintext = ""
        for cipher_letter in ciphertext:
            upper = False
            if cipher_letter in string.ascii_letters:
                if cipher_letter in string.ascii_uppercase:
                    cipher_letter = cipher_letter.lower()
                    upper = True
                cipher_letter_index = string.ascii_lowercase.index(
                    cipher_letter)
                cipher_letter = string.ascii_lowercase[(
                    a*(cipher_letter_index**3)
                    + b * (cipher_letter_index**2)
                    + c*cipher_letter_index
                    + i
                ) % (a_len)]
                if upper:
                    cipher_letter = cipher_letter.upper()
            plaintext += cipher_letter
        # print(str(i) + ": " + plaintext)
        output += "\n" + str(plaintext)
    return output


output = ""
for a in range(max):
    for b in range(max):
        for c in range(max):
            output += f"\n;{a},{b},{c};{ceaser_plus(a, b, c, ciphertext)}"

o = open("ceasar_output.txt", "w")
o.write(output)
o.close()

# f = open("ukenglish.txt", "r")
# english = f.read()
# f.close()

# if any(word in english for word in plaintext.split(" ")):
#     print(a, b, c, i)
# gives:
# key:
