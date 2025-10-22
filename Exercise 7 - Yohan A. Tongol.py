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
    print("Increments of 1= ", c)#This line of code adds an increment of 1 starting from 30 and until the limit 50
print("----------------------")
for d in range(50, 8, -2):
    print("Decrements of 2= ", d)#This line of code deducts a decrement of -2 starting from 50 and until the limit 10
print("----------------------")
for e in range(100, 205, 5):#This line of code adds increments of +5 and adds them to the starting number 100 until the limit 200
    print("Increments of 5= ", e)