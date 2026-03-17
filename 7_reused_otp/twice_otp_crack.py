import string
import itertools
ciphertexts = ["wxgzgvxpub", "vhwgfblmhq"]

letter_10_filtered =[]
with open("src/11-letter-words.txt") as file:
    for word in file:
        word_san = word.replace("\n","")
        letter_10_filtered.append(word_san)

print(letter_10_filtered)
alphabets = list(itertools.repeat(string.ascii_lowercase,10))
print(len(alphabets))
output_p0 = []
output_p1 = []
output_s = []

count = 0
for a,b,c,d,e,f,g,h,i,j in itertools.product(*alphabets):
    count+=1
    if count % 10000 == 1:
        print(count)
    current = a+b+c+d+e+f+g+h+i+j
    #print(current)
    for ci,ciphertext in enumerate(ciphertexts):
        plaintext = ""
        for iter,cipher_letter in enumerate(ciphertext):
            upper = False
            if cipher_letter in string.ascii_letters:
                if cipher_letter in string.ascii_uppercase:
                    cipher_letter = cipher_letter.lower()
                    upper = True
                #MAKE DECRYPT SHOULD BE NOW
                cipher_letter = string.ascii_lowercase[(26+
                    string.ascii_lowercase.index(cipher_letter) - string.ascii_lowercase.index(current[iter])
                ) % (len(string.ascii_lowercase))]
                if upper:
                    cipher_letter = cipher_letter.upper()
            plaintext += cipher_letter
        #print(sequence + ": " + plaintext)
        if ci:
            output_p1.append(plaintext)
        else:
            output_p0.append(plaintext)
    output_s.append(current)

o = open("7_reused_otp/output_p0.txt", "w")
o.write("\n".join(output_p0))
o.close()

o = open("7_reused_otp/output_p1.txt", "w")
o.write("\n".join(output_p1))
o.close()

o = open("7_reused_otp/output_s.txt", "w")
o.write("\n".join(output_s))
o.close()