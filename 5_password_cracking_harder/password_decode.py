import hashlib
trueHash = "bd9888e5116de71e8fdb2c87365fbaa0612364debd20c61b72ae4c4e1a9ea6a4"
salt = "h21Qi6SZsxp30vQJ6PVJZ95p"
f = open("src/dog_names.txt", "r")
names = f.read()
f.close()
names = names.split("\n")


i = 0

for name in names:
    #add extra words to check with the formatting extras specified in pdf
    
    pass

for name in names:
    name = name.removeprefix(" ")
    name = name.removesuffix(" ")
    name = name.removeprefix("\n")
    name = name.removesuffix("\n")
    i += 1
    hash =hashlib.sha256()
    hash.update((name + salt).encode())
    if str(hash.hexdigest()) == trueHash:
        print(name)
        print(i)
        break
    if i % 1000 == 0:
        print(str(i))
