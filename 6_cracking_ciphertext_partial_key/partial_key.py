import string
ciphertext = "bqxcacrkfta"
partial = "h?el??rt?gw"

sequences = []
for a in string.ascii_lowercase:
    for b in string.ascii_lowercase:
        for c in string.ascii_lowercase:
            for d in string.ascii_lowercase:
                sequences.append(a+b+c+d)

f = open("src/11-letter-words.txt", "r")
letter11 = f.read()
f.close()

letter_i = []
for word in letter11:
    if word[0] == "i":
        letter_i.append(word)

print("1")
output_p = []
output_s = []
for sequence in sequences:
    current = f"h{sequence[0]}el{sequence[1]}{sequence[2]}rt{sequence[3]}gw"
    plaintext = ""
    for i,cipher_letter in enumerate(ciphertext):
        upper = False
        if cipher_letter in string.ascii_letters:
            if cipher_letter in string.ascii_uppercase:
                cipher_letter = cipher_letter.lower()
                upper = True
            cipher_letter = string.ascii_lowercase[(
                string.ascii_lowercase.index(cipher_letter) + string.ascii_lowercase.index(current[i])
            ) % (len(string.ascii_lowercase))]
            if upper:
                cipher_letter = cipher_letter.upper()
        plaintext += cipher_letter
    #print(sequence + ": " + plaintext)
    output_p.append(plaintext)
    output_s.append(sequence)
print("2")
o = open("6_cracking_ciphertext_partial_key/output_p.txt", "w")
o.write("\n".join(output_p))
o.close()

o = open("6_cracking_ciphertext_partial_key/output_s.txt", "w")
o.write("\n".join(output_s))
o.close()

i=0
for line in output_p:
    i += 1
    for word in letter_i:
        if word == line:
            print(str(i)+": "+word)
    if i % 100 == 1:
        print(i)