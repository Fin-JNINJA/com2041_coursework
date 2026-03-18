import hashlib
trueHash = "bd9888e5116de71e8fdb2c87365fbaa0612364debd20c61b72ae4c4e1a9ea6a4"
salt = "h21Qi6SZsxp30vQJ6PVJZ95p"
f = open("src/dog_names.txt", "r")
names = f.read()
f.close()
names = names.split("\n")


def find_substitutions(name: str) -> dict:
    change_letters = {}
    for i in range(len(name)):
        match list(name)[i].lower():
            case "o":
                symbols = ["0", "*"]
            case "i":
                symbols = ["1", "!"]
            case "l":
                symbols = ["1"]
            case "a":
                symbols = ["4", "@", "&"]
            case "e":
                symbols = ["3"]
            case "s":
                symbols = ["$", "5"]
            case _:
                symbols = []
        if len(symbols) > 0:
            symbols.append(name[i])
            change_letters.update({i: symbols})
    return change_letters


def make_name(sequence, name, keys):
    name_list = list(name)
    for i, key in enumerate(keys):
        name_list[key] = sequence[i]
    return "".join(name_list)


extraNames = []
for name in names:
    # print("")
    dict_places = find_substitutions(name)
    sequences = []
    # print(dict_places)

    lens = []

    list_of_list_symbols = []
    for key in dict_places:
        list_of_list_symbols.append(dict_places[key])
        lens.append(len(dict_places[key]))

    possibilities = 1
    for length in lens:
        possibilities *= length
    # print(len(lens))
    # print(possibilities)

    current_sequence = []
    max_sequence = []
    keys = []
    for key in dict_places:
        current_sequence.append(dict_places[key][0])
        max_sequence.append(dict_places[key][len(dict_places[key])-1])
        keys.append(key)

    # for a in range(list_places[0]):
    #     if len(lens) == 2:
    #         for b in range(list_places[1]):
    #             if len(lens) == 3:
    #                 for c in range(list_places[2]):
    #                     if len(lens) == 4:
    #                         for d in range(list_places[3]):
    #                             if len(lens) == 5:
    #                                 for e in range(list_places[4]):
    #                                     current_sequence list_places[a][sublist_index+1]

    # print(current_sequence)

    iter = 0
    sequence_length = len(current_sequence)
    while current_sequence != max_sequence:
        iter += 1
        if iter >= possibilities:
            print("AA")
            break

        for i in range(sequence_length):
            if i == 1:
                pass
            sublist_index = list_of_list_symbols[i].index(current_sequence[i])
            if sublist_index + 1 < len(list_of_list_symbols[i]):
                if i == 1:
                    pass
                current_sequence[i] = list_of_list_symbols[i][sublist_index+1]
                break  # dont iterate next char as the sequence has changed
            else:
                if i == 1:
                    pass
                current_sequence[i] = list_of_list_symbols[i][0]
                # iterate to next char to waterfall the change
        extraNames.append(make_name(current_sequence, name, keys))
    print(possibilities - iter)

digitExtraNames = []
o = open("5_password_cracking_harder/passwordsnewnodigit.txt", "w")
for name in extraNames:
    o.write(name + "\n")
    for i in range(100):
        if i < 10:
            num = "0" + str(i)
        else:
            num = i
        digitExtraNames.append(name+str(num))
o.close()

print("iterating:")
i = 0
o = open("5_password_cracking_harder/passwordsnew.txt", "w")
for name in digitExtraNames:
    o.write(name + "\n")
    i += 1
    hash = hashlib.sha256((name + salt).encode())

    hash_current = str(hash.hexdigest())
    if str(hash_current) == trueHash:
        print("AAAAAAAAA")
        print(name)
        print(i)
        break

    if i % 50000 == 0:
        print(str(i))
o.close()
