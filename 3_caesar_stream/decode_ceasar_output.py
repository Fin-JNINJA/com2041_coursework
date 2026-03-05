f = open("src/ukenglish.txt", "r")
english = f.read()
f.close()
english = english.split("\n")

i = 0
with open("3_caesar_stream/ceasar_output.txt", "r") as file:
    for line in file:
        i += 1
        for word in english:
            if word in line and len(word) > 4:
                print(word)
                print(i)
                print(line)
                break
        # if i % 100 == 1:
        #     print(str(i) + ":"+line)
