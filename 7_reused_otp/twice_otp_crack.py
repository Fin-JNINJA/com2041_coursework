import string
ciphertexts = ["wxgzgvxpub", "vhwgfblmhq"]

letter_10_filtered = []
with open("src/10-letter-words.txt") as file:
    for word in file:
        word_san = word.replace("\n", "")
        letter_10_filtered.append(word_san)

print(letter_10_filtered)

c0_minus_c1 = ""

for i in range(len(ciphertexts[0])):
    cipher_letter = "?"
    if ciphertexts[0][i] in string.ascii_letters and ciphertexts[1][i] in string.ascii_letters:
        cipher_letter = string.ascii_lowercase[(26 +
                                                string.ascii_lowercase.index(
                                                    ciphertexts[0][i]) - string.ascii_lowercase.index(ciphertexts[1][i])
                                                ) % (len(string.ascii_lowercase))]
    c0_minus_c1 += cipher_letter
print(c0_minus_c1)


for word in letter_10_filtered:
    # c0_minus_c1
    # print(word)
    maybe_plain_word = ""
    for i, letter in enumerate(word):
        maybe_plain_letter = "?"
        if letter in string.ascii_letters and c0_minus_c1[i] in string.ascii_letters:
            maybe_plain_letter = string.ascii_lowercase[(
                string.ascii_lowercase.index(
                    letter) + string.ascii_lowercase.index(c0_minus_c1[i])
            ) % (len(string.ascii_lowercase))]
        maybe_plain_word += maybe_plain_letter
    if maybe_plain_word in letter_10_filtered:
        print(maybe_plain_word, word)
        plaintexts = [maybe_plain_word, word]
        break

# ciphertexts[0]-maybe_plain_word
# ciphertexts[0]-word

for i, word in enumerate(ciphertexts):
    key = ""
    for j, letter in enumerate(word):
        maybe_key_letter = "?"
        if letter in string.ascii_letters and plaintexts[i][j] in string.ascii_letters:
            maybe_key_letter = string.ascii_lowercase[(26 +
                                                       string.ascii_lowercase.index(
                                                           letter) - string.ascii_lowercase.index(plaintexts[i][j])
                                                       ) % (len(string.ascii_lowercase))]
        key += maybe_key_letter
    print(key)

# deciphered
# cosponsors
# key: tterrotyqy
