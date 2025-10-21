'Exercise 7'
a=0# This code creates and stores a value of 0 into A
for a in range(51):#This code caluclates the range and will make a limit to how much this code can print
    print("Increments of 1 = ", a) #this code prints the increments of +1 to a until it reaches 50
    a+=1
print("----------------------")

for b in range(50, -1,-1): #this code takes another approach because I wanted to experiment with the codes
    print("Decrements of 1 = ", b) # This code makes decrements of 1 which starts from 50 as shown on the first code
    #The second argument in the range() code is how many times it will minus 50 by, and the last argument is the limit
print("----------------------")

for c in range(30,51,1):
    print("Increments of 1= ", c)
print("----------------------")
for d in range(50, 8, -2):
    print("Decrements of 2= ", d)
print("----------------------")
for e in range(100, 205, 5):
    print("Increments of 5= ", e)