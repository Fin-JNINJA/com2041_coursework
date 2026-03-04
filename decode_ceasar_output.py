
f = open("ukenglish.txt", "r")
english = f.read()
f.close()

i = 0
with open("ceasar_output.txt", "r") as file:
    i += 1
    for line in file:
        if line[0] != ";":
            if any(word in english for word in line.split(" ")):
                print(i)
                print(line)
