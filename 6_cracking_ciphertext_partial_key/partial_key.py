import string
ciphertext = "bqxcacrkfta"
partial = "h?el??rt?gw"

sequences = []
for a in string.ascii_lowercase:
    for b in string.ascii_lowercase:
        for c in string.ascii_lowercase:
            for d in string.ascii_lowercase:
                sequences.append(a+b+c+d)


# CORRECT AFTER DECRYPT
letter_filtered = []
with open("src/11-letter-words.txt") as file:
    for word in file:
        if list(word)[0] == "u" and list(word
                                         )[2] == "t" and list(word)[3] == "r":
            print(word)
            word_san = word.replace("\n", "")
            letter_filtered.append(word_san)

print(letter_filtered)
print("1")
output_p = []
output_s = []
for sequence in sequences:
    current = f"h{sequence[0]}el{sequence[1]}{sequence[2]}rt{sequence[3]}gw"
    plaintext = ""
    for i, cipher_letter in enumerate(ciphertext):
        upper = False
        if cipher_letter in string.ascii_letters:
            if cipher_letter in string.ascii_uppercase:
                cipher_letter = cipher_letter.lower()
                upper = True
            # MAKE DECRYPT SHOULD BE NOW
            cipher_letter = string.ascii_lowercase[(26 +
                                                    string.ascii_lowercase.index(
                                                        cipher_letter) - string.ascii_lowercase.index(current[i])
                                                    ) % (len(string.ascii_lowercase))]
            if upper:
                cipher_letter = cipher_letter.upper()
        plaintext += cipher_letter
    # print(sequence + ": " + plaintext)
    output_p.append(plaintext)
    output_s.append(sequence)
print("2")
o = open("6_cracking_ciphertext_partial_key/output_p.txt", "w")
o.write("\n".join(output_p))
o.close()

o = open("6_cracking_ciphertext_partial_key/output_s.txt", "w")
o.write("\n".join(output_s))
o.close()

i = 0
for line in output_p:
    i += 1
    for word in letter_filtered:
        if word == line:
            print(str(i)+": "+word)
    if i % 10000 == 1:
        print(i)

# Gives: 88320: ultramarine
# Sequence: faqx
