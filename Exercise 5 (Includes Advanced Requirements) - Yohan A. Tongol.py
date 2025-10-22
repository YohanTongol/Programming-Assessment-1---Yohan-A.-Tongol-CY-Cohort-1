'Exercise 5'
month=int(input("Please type the month in number, 1-12 "))
if month== 1:
    print("Your answer", month, (", Is January and it has 31 days."))
elif month == 2:
    yn=input("Is this month a leap year? Please type y or n for your answer.").lower()
    if yn == "y":     
        print("Your answer", month, ("Is Febuary, It has 29 days on a leap year."))
    else:
            print("Your answer", month, ("Is Febuary, It has 28 days."))
elif month == 3:
    print("Your answer", month, (", Is March, It has 31 days."))
elif month == 4:
    print("Your answer", month, (", Is April, It has 30 days."))
elif month == 5:
    print("Your answer", month, (", Is May, It has 31 days."))
elif month == 6:
    print("Your answer", month, (", Is June, It has 30 days."))
elif month == 7:
    print("Your answer", month, (", Is July, It has 31 days."))
elif month == 8:
    print("Your answer", month, (", Is August, It has 31 days."))
elif month == 9:
    print("Your answer", month, (", Is September, It has 30 days."))
elif month == 10:
    print("Your answer", month, (", Is October, It has 31 days."))
elif month == 11:
    print("Your answer", month, (", Is November, It has 30 days."))
elif month == 12:
    print("Your answer", month, (", Is December, It has 30 days."))
else:
    print("Sorry this is an invalid number for a month.")
#This program uses if else statement to check if the number of the 
#user input is valid, it saves the user input which is an integer and
#it is then checked if it ranges from 1 to 12 which then gives the answer
#and displays the user input. Another if else statement is used for the month
#Febuary to ask if it is a leap year, if Y has been typed then it will display
#the days of the leap year, else it will display the normal febuary days.
