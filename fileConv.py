import string

file = open("example.html",'r')
file2 = open("newFile.txt",'a')

while 1:
    char = file.read(1)

    if(char is '<'):

        char = file.read(1)

        if(char is 'a'):
            char = file.read(1)
            char = file.read(1)
            char = file.read(1)
            char = file.read(1)
            char = file.read(1)
            char = file.read(1)
            char = file.read(1)
            char = file.read(1)

            while(char is not '"'):
                file2.write(char)
                char = file.read(1)

            file2.write(' ')

        while(char is not '>'):
            char = file.read(1)


    if not char:
        break
    if (char is not '>'):
        file2.write(char)

print('The \"TXT\" File is:')

file3 = open("newFile.txt",'r')
while 1:
    char2 = file3.read()
    if not char2:
        break
    print(char2)

file.close()
file2.close()
file3.close()