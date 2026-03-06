import hashlib
trueHash = "bd9888e5116de71e8fdb2c87365fbaa0612364debd20c61b72ae4c4e1a9ea6a4"
salt = "h21Qi6SZsxp30vQJ6PVJZ95p"
f = open("src/dog_names.txt", "r")
names = f.read()
f.close()
names = names.split("\n")
#print(names)

def branch(name:str, i:int, symbols:list) ->str:
    newNames = []
    newNames.append(name)
    for symbol in symbols:
        name = list(name)
        name[i] = symbol
        print(str(name))
        if len(name) < i+1:
            newNames += substitute(str(name),i+1)
    return newNames


def substitute(name:str,i:int) -> list:
    
    newNames = []
    match list(name)[i].lower():
        case "o":
            newNames += branch(name,i,["0","*"])
        case "i":
            newNames += branch(name,i,["1","!"])
        case "a":
            newNames += branch(name,i,["4","@","&"])
        case "e":
            newNames += branch(name,i,["3"])
        case "s":
            newNames += branch(name,i,["$","5"])
        case _:
            if len(name) < i+1:
                newNames += substitute(name,i) # i think#newNames += name
    return newNames


extraNames = []
for name in names:
    #add extra words to check with the formatting extras specified in pdf
    #print(name)
    extraNames.append(name)
    extraNames += substitute(name,0)

print(extraNames)
i = 0
for name in extraNames:
    i += 1
    hash =hashlib.sha256()
    hash.update((name + salt).encode())
    if str(hash.hexdigest()) == trueHash:
        print(name)
        print(i)
        break
    if i % 50 == 0:
        print(str(i))
print(i)