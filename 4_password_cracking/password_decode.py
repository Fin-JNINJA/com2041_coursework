import hashlib
trueHash = "8b2adc074cac58db0d894fbdb620dacc6dcdd70b86c390f70d9e42a4b9aa6a16"
#trueHash = "7a8a1ef53704c6ba6bee1c0ac8a99c74b17d59228297d6d877a36b9cb836221e"
salt = "kvFMlhH8Za5i"
f = open("src/ukenglish.txt", "r")
english = f.read()
f.close()
english = english.split("\n")

f = open("src/10-letter-words.txt", "r")
letter10 = f.read()
f.close()
english += letter10.split("\n")

f = open("src/11-letter-words.txt", "r")
letter11 = f.read()
f.close()
english += letter11.split("\n")

i = 0

#print(english[6]+str(len(english[6])))
o = open("4_password_cracking/hashes.txt", "w")
for word in english:
    word = word.removeprefix(" ")
    word = word.removesuffix(" ")
    word = word.removeprefix("\n")
    word = word.removesuffix("\n")
    i += 1
    hash =hashlib.sha256()
    hash.update((word + salt).encode())
    #hash.update(("contemplates"+"FZ23sDK0NcUi").encode()) #remove
    
    #print(hash.hexdigest())
    o.write(str(hash.hexdigest()) +"\n")
    if str(hash.hexdigest()) == trueHash:
        print(word)
        print(i)
        break
    if i % 1000 == 0:
        print(str(i))
o.close()
#gives: forcemeat