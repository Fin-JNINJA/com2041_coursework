import string
ciphertext = "tgmmmrrjgeytnwpgpsgktbtavcxdjmfeggmwsqfibapeqhzfqjpmcijqpsomgqlulqmcxzjoyzbtzutqxlnbubxpefegyzznwxwwdzfdxwvzzmbqbqkggbqfofzneqkgfeggacfuywdekgaocteoozzknrrozhfkaoefztgwhfqgebeopqmewnqgpyodefqqmvtmtyuoarwjgpvogakyzrfttskaoutnpyzlcxzcptztnrrnqmeaekgpvwdqyeuomeakmeyooeffebeyajbqffgaeaumgbcubehjnlqmzfltemkgfgyxwtezjoqbnmkeaymogfgyllgpziwxurypbgqtnqmiabtnmycnbwnqmrtnswdzfdxwvnrfbwpkqyltsytpzttnloeugtrryenomajgpyltsytpzttnryenomajgplovbgmpeohccbfeiwdwwthuvkfvmyftszpfhhrnoaqeefwtyexcqqoeuujtqpgyxselceizjkljsfhomajpmjgwxwwuonbqjkaozzrwoyhyalcyzffgacqixfeeopdbkzmcwtxcwqunqdibzjgqciblpysefzbubayqaqiwtbfxqyqqbvgazfuznfghtayltnqbmnutrteaskvrrgduywluaeyltbqeohrtnswqeimakopzuvszfqygbqytyxmtnsbahvtiuaxgbttqghzewetrummwepvqkgaruwqcesehgfekztfbaybtcubhxvdarbaykzllefbvywpcmcjwxwghxntrmguontarwthkvkfvomgywtptbfukopuogfqjyfikeqioefonsqoncgnrrraonvzcfxyltzcqucwdqyfpfyybwbxpbtcuqqniqehfqhzbqbtullwzyfehiqpcfxxvjemtuvg"
# dictionary word with a random triple for each letter
f = open("src/ukenglish.txt", "r")
english = f.read()
f.close()
english = english.split("\n")

# 7 letter key maybe from kasikis test
# values of a,b,c that give a cipher scheme.  The example in the question shows that not all values do.


def ceaser_plus(a, b, c, i, ciphertext) -> str:

    a_len = len(string.ascii_lowercase)
    output = ""

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


max = 26
a = 0
b = 0
c = 1
o = open("8_vigenere_plus/plaintextsmaybe.txt", "w")

for word in english:
    output = ""
    if len(word) == 7:
        for i, ciphertext_letter in enumerate(ciphertext):
            output += ceaser_plus(a, b, c, string.ascii_lowercase.index(
                word[i & (len(word)-1)]), ciphertext_letter).replace("\n", "")

        o.write(output + "\n")

o.close()
