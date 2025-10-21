'Exercise 8'
nlist=["Jake","Zac","Ian","Ron","Sam","Dave"] #this code makes nlist into a list of strings or names
pick=input("Please Enter a Name: ").capitalize()#this code asks for a user input and the .capitalize code makes the answer properly capitalized
if pick == nlist[4]: #this if statement checks to see if the user has chosen a specific string by using indexing since instructions say Sam is the correct answer
    print("You have chosen the correct name,", pick,"!")
elif pick in nlist: #this elif statement checks to see if the user has chosen a name within the list and prints if it is true
    print("The name", pick, "is within the system")
else: #the else code checks if the user input is not within the list and prints the last statement
    print("The name is not within the system")