#File Handling

#Stores the data into the file, access it whenever.

#Two types of files
#1. Text file - .txt, .csv... ASCII
#2. Binary file - .dat, .obj, .bin...

# File Methods (Operations)
#1. open() - It is used to open the file and also create the file if not exists.
#2. write(str, int) - write a single lube into the fie at once.
#3. writelines(seq) - writes multiple lins into the file.
#4. read()- read the whole content of file at once.
#5. readline()- read the single line at once.
#6. readlines()- read the multiple lines from the files.
#7. close() - It is used to close the file.

#File Modes
#r - read only
#w - write only
#a - append only (End of the file)
#x - write, error if file already exists
#a+ - append and read
#w+ - write and read
#r+ - read and write

#binary files - add 'b' in all modes
#rb, wb, ab, a+b, ab+, r+b/rb+, w+b/wb+, a+b/ab+

#writing data into the files
#file = input("Enter File name to write:: ")
#f1= open("file", "w")
#lines = int(input("Enter number of lines ::"))
#for i in range(lines):
#    data=input("Enter content to write::")
#    f1.write(data+"\n")
#f1.write("CR7")
#f1.writelines(["This is file\n ", "file handling\n", ])

#print("Write successfully")
#f1.close()

list1=[]

file = input("Enter File name to write:: ")
f1= open("file", "w")
lines = int(input("Enter number of lines ::"))
for i in range(lines):
    data=input("Enter content to write::")
    f1.append(data+"\n")
    
f1.writelines(list1)    
print("Write successfully")
f1.close()
#Reading data into the file
#f2= open("demo.txt", "r")
#data=f2.read()
#print(data)
#print(f2.read())

#readline() -reads the single line at a time.
#print(f2.readline())
#print(f2.readline())
#print(f2.readline())

#readlines() - reads multiple lines at a time.
#print(f2.readlines())

#f2.close()

#append - write if file not exits and append if file exits
list1=[]
fnm = input("Enter file name :")
with open(fnm, 'a') as f1:
    lines = int(input("How many lines to append : "))
    for l in range(lines):
        data = input("Enter content to append : ")
        list1.append(data+"\n")
    f1.writelines(list1)
    print("Append sucessfully")

'''
'''
#w+ = write and read

file=input("Enter file name: ")

with open(file, "w+") as fobj:
    lines=int(input("How many lines to write: "))

    for l in range(lines):
        info=input("Enter content to write: ")
        fobj.write(info+"\n")
    print("Written successfully")
    print("======================================")

    #tell() - provides current cursor position.
    print(fobj.tell())

    #seek() - moves the cusor pointer to specific position
    #0 - beginning
    fobj.seek(0)
    print("Current position: ", fobj.tell())
    print("File content :: ")
    print(fobj.read())
'''
'''
#a+ = append and read

file=input("Enter file name: ")

with open(file,"a+") as fobj:
    lines = int(input("How many lines to append: "))

    for l in range(lines):
        info= input("Enter content to write: ")
        fobj.write(info+"\n")

    print("Append successfully")
    print("========================================")
    fobj.seek(0)
    print("Current position: ", fobj.tell())
    print("File content :: ")
    print(fobj.read())
    
'''

#r+ = read and write both the content

file = input("Enter file name: ")
try:

    with open(file, "r+") as fobj:
        print("File content:: ")
        print(fobj.read())
        print("======================================")
        lines=int(input("How many lines to write : "))

        for l in range(lines):
            info=input("Enter content to write: ")
            fobj.write(info+"\n")
