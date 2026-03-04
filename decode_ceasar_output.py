
f = open("../src/ukenglish.txt", "r")
english = f.read()
f.close()
english = english.split("\n")

i = 0
with open("../src/ceasar_output.txt", "r") as file:
    for line in file:
        i += 1
        if line[0] != ";":
            # any(word in english for word in line.split()):
            for word in line.split():
                if word in english and len(word) > 4:
                    print(word)
                    print(i)
                    print(line)
                    break
        if i % 1000 == 1:
            print(str(i) + ":"+str(line.split()))
