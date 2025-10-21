'Exercise 9'
def hello(): #this code defines hello() as an intruction
    print("Hello") #this code is within the function and prints "Hello" if function is called
    
def main(): #this code is to link the function main() to the hello() function. this makes it so that if main() function is called it runs the hello() function also
    hello()

if __name__ == "__main__":
    main() #this finally prints the word "Hello" into the function