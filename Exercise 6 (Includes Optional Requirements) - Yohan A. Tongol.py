'Exercise 6'
pas=12345 #This is the correct Password and is a variable
n1=5 #This is the starting amount of tries that the user has
max=1 #This is the limit of tries of the user
i=int(input("Please Enter Pin: ")) #This code asks the user to enter their pin
while i != pas: # A while loop is used to keep to keep track if of the amount of times the password has been entered
 n1-=1#It will then deduct 1 point from the users "tries"
 print("Incorrect Password Please Try again, You have", n1,"Tries left")
 i=int(input("Please Re-enter your Pin: ")) #This will allow the user to keep inputting their password
 if n1 == max: #If the user has reached the max limit it will print the series of strings below
  print("Max Tries Reached. Authorities Contacted.")
  break;
if i == pas: #If the user has inputted the correct password a successful log in screen will present on the program
   print("Succesful Log-In")   