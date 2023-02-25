file = open("test.txt")
# print(file.read()) # read all content test.txt
# print(file.read(2))  # read only 2 char of test.txt

# read single line
# print(file.readline())
# print(file.readline())

# read line by line 
line = file.readline()
# while line!= "":
#    print(line)
#    line = file.readline()

# use of readlines
for line in file.readlines():
    print(line)


file.close()




