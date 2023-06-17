#todo, add bias coin system
import time
from logo import logo #load logo file into data
from api import api

#display logo file
print(logo)

#def all variables
flips = 0
loop = 1

#mainloop
while loop == 1:
    userinput = input("How many times would you like to flip the coin, or if you want to exit, type exit: ") #gathers user input and stores to the userinput variable
    if userinput == "exit": #if user types exit, program exits
        loop = 0 #exits the program
    elif userinput.isnumeric(): #for if the user inputs a number, below code executes
        userinput = int(userinput)  #convert the input to an integer value for mathematic calculations
        if userinput > 0: #if the user puts a compatable number (<0), the program begins2
            head, tail = api(userinput) #sends the user flip value to the api, returns heads count and tails count, read apidoc.md for documentation
            print("") #newline
            print("the coin landed on heads", head, "times, and it landed on tails", tail, "times") #print the results from the api
            print("")  # newline
            time.sleep(2) #cleanupcmd
            exit = input("if you want to go again, type yes, if you want to exit, type no: ") #ask user if they want to go again
            if exit == "no":  #catch no arg
                loop = 0 #exit the loop, stopping the program
        elif userinput <= 0: #catch the user being silly and putting in an impossible value
            print("You cant flip a coin zero or less times, put in a positive integer more than zero!") #tell 'em off
            time.sleep(1) #you have to wait now lmao
    else: #if the user does not put exit, or a number
        print("please put a number, or the word exit to exit!") #ask the user to re-input their response
        time.sleep(1)