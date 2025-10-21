'Exercise 10'
number1=int(input("Please Enter Your Number= ")) #this code asks for the user input

def ooe(number1): #a function called "ooe" is defined with number1 being inside
    if number1 % 2 ==0: #the if statement takes the user input and does modolus by 2 to check if there is a remainder. This code checks to see if the user input is an even number
        print("Your Number", number1, "Is an Even Number")
    else:#else, if the user input modolus answer is equal to 1, it then prints that the number is odd
        print("Your Number", number1, "Is an Odd Number")
ooe(number1) #this calls the function to run it and show the answer
