'Exercise 4'
print("Europe Quiz! Please Answer The Questions Below!")
score=0
q1=input("What is the Capital Of Sweden? ").capitalize()
if q1 == "Stockholm":
    print("That is the Correct Answer!")
    score+=1
    print("Your Current Score=", score)
else:
    print("Sorry Wrong Answer.")
    print("Your Current Score=", score)
print("-----")
q2=input("What is the Capital Of France? ").capitalize()
if q2 == "Paris":
    print("That is the Correct Answer!")
    score+=1
    print("Your Current Score=", score)
else:
    print("Sorry Wrong Answer.")
    print("Your Current Score=", score)
print("-----")
q3=input("What is the Capital Of Italy? ").capitalize()
if q3 == "Rome":
    print("That is the Correct Answer!")
    score+=1
    print("Your Current Score=", score)
else:
    print("Sorry Wrong Answer.")
    print("Your Current Score=", score)
print("-----")
q4=input("What is the Capital Of Germany? ").capitalize()
if q4 == "Berlin":
    print("That is the Correct Answer!")
    score+=1
    print("Your Current Score=", score)
else:
    print("Sorry Wrong Answer.")
    print("Your Current Score=", score)
print("-----")
q5=input("What is the Capital Of Spain? ").capitalize()
if q5 == "Madrid":
    print("That is the Correct Answer!")
    score+=1
    print("Your Current Score=", score)
else:
    print("Sorry Wrong Answer.")
    print("Your Current Score=", score)
print("-----")
q6=input("What is the Capital Of Ukraine? ").capitalize()
if q6 == "Kyiv":
    print("That is the Correct Answer!")
    score+=1
    print("Your Current Score=", score)
else:
    print("Sorry Wrong Answer.")
    print("Your Current Score=", score)
print("-----")
q7=input("What is the Capital Of Greece? ").capitalize()
if q7 == "Athens":
    print("That is the Correct Answer!")
    score+=1
    print("Your Current Score=", score)
else:
    print("Sorry Wrong Answer.")
    print("Your Current Score=", score)
print("-----")
q8=input("What is the Capital Of Poland? ").capitalize()
if q8 == "Warsaw":
    print("That is the Correct Answer!")
    score+=1
    print("Your Current Score=", score)
else:
    print("Sorry Wrong Answer.")
    print("Your Current Score=", score)
print("-----")
q9=input("What is the Capital Of Russia? ").capitalize()
if q9 == "Moscow":
    print("That is the Correct Answer!")
    score+=1
    print("Your Current Score=", score)
else:
    print("Sorry Wrong Answer.")
    print("Your Current Score=", score)
print("-----")
q10=input("What is the Capital Of United Kingdom? ").capitalize()
if q10 == "London":
    print("That is the Correct Answer!")
    score+=1
    print("Congrats on Completing the Quiz! Your Final Score Is=", score)
else:
    print("Sorry Wrong Answer.")
    print("Congrats on Completeing the Quiz! Your Final Score Is=", score)
    print("-----")
#This program uses if else statement, first it grabs the user input
#and stores it in the variable, the .capitalize() code is used to make the
#inputs first letter capital so it is not case sensitive and will display correct
#even if not capitalizd properly, the if and else statement then check
#to see if answer is right and displays if it is on or not
#A score variable is made at the start of the program which then adds up if
#the users answer is correct and dosent add 1 if the answer is incorrect which
#is then finalized on the 10th question
