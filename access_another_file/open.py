f = open('read.txt' , 'r')

print(f.read())

#print(f.readline())  read lines

f1 = open('new.txt' , 'w') #a append

f1.write("something")


# copy all data from f and paste in f1
for data in f:
    f1.write(data)

# copy img from f and paste in f1

f = open('ASCII CODE.png' , 'rb')

f1 = open('new.jpg' , 'wb')

for data in f:
    f1.write(data)
