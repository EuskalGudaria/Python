textfile = open("file.txt", encoding= "ISO-8859-1")
lines = textfile.readlines()

for line in reversed(lines):
    print(line)

textfile.close()
