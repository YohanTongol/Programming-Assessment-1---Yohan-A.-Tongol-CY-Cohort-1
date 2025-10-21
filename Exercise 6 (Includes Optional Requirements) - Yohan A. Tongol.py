'Exercise 6'
pas=12345 #This is the correct Password and is a variable
n1=5 #This is the starting amount of tries that the user has
max=1 #This is the limit of tries of the user
i=int(input("Please Enter Pin: ")) #This code asks the user to enter their pin
while i != pas: # A while loop is used to 
 n1-=1
 print("Incorrect Password Please Try again, You have", n1,"Tries left")
 i=int(input("Please Re-enter your Pin: "))
 if n1 == max:
  print("Max Tries Reached")
  break;
if i == pas:
   print("Succesful Log-In")   