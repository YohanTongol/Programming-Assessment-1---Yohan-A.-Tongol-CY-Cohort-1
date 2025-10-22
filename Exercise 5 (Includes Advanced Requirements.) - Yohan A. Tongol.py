'Exercise 5'
months={'1':31,
        "2":28,
        "3":31,
        "4":30,
        "5":31,
        "6":30,
        "7":31,
        "8":31,
        "9":30,
        "10":31,
        "11":30,
        "12":30}

month=(input("Please type the month in number, 1-12 "))
if month == '1':
    print("Your answer", month, ", Is January and it has", months[month],  "days.")
elif month == '2':
    yn=input("Is this month a leap year? Please type y or n for your answer.").lower()
    if yn == "y":     
        print("Your answer", month, "Is Febuary, It has", months[month], "days on a leap year.")
    else:
        months["2"]="29"    
        print("Your answer", month, "Is Febuary, It has", months[month], "days.")
elif month == '3':
    print("Your answer", month, ", Is March, It has",months[month], "days.")
elif month == '4':
    print("Your answer", month, ", Is April, It has,", months[month] ,"days.")
elif month == '5':
    print("Your answer", month, ", Is May, It has",months[month] ,"days.")
elif month == '6':
    print("Your answer", month, ", Is June, It has", months[month]," days.")
elif month == '7':
    print("Your answer", month, ", Is July, It has",months[month] ," days.")
elif month == '8':
    print("Your answer", month, ", Is August, It has",months[month],"days.")
elif month == '9':
    print("Your answer", month, ", Is September, It has",months[month],"days.")
elif month == '10':
    print("Your answer", month, ", Is October, It has",months[month], "days.")
elif month == '11':
    print("Your answer", month, ", Is November, It has",months[month], "days.")
elif month == '12':
    print("Your answer", month, ", Is December, It has",months[month],"days.")
else:
    print("Sorry this is an invalid number for a month.")
#This program uses if else statement to check if the number of the 
#user input is valid, it saves the user input which is an integer and
#it is then checked if it ranges from 1 to 12 which then gives the answer
#and displays the user input. This is because of the dictionary that is created earlier
#The left side of the dictionary is all the months in numbers and the right
#is the amount of days within that month, it is used to store and make it easier
#to get the data to display
# Another if else statement is used for the month
#Febuary to ask if it is a leap year, if Y has been typed then it will display
#the days of the leap year, else it will display the normal febuary days.
