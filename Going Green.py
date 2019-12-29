#Sabrina Turney
#October 8, 2018
#Going Green
#This program takes multiple inputs from the user to calculate their overall
#savings from "going green" using multiple arrays.

def main():
    #Declare local variables
    endProgram = "no"
    while endProgram == "no":
        notGreenCost = [0] * 12
        goneGreenCost = [0] * 12
        savings = [0] * 12
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        #Function calls
        getNotGreen(notGreenCost, months)
        getGoneGreen(goneGreenCost, months)
        energySaved(notGreenCost, goneGreenCost, savings)
        displayInfo(notGreenCost, goneGreenCost, savings, months)

        #Repetition structure here will end or repeat the program:
        endProgram = input("Do you want to end the program? Yes or no: ")

#Here's where we get our not green cost array filled up by the user:
def getNotGreen(notGreenCost, months):
    #I just called the "counter" variable index here to keep in line
    #with the list nomenclature!
    index = 0
    while index < len(notGreenCost):
        #To avoid too many args in the input line, I made the months into
        #headers that appear before the user inputs so they know which
        #month they are inputting to.
        print ("\t\t" + (months[index]))
        notGreenCost[index] = int(input("Enter NOT GREEN energy costs for this month: "))
        index += 1
    print("-----------------------------------------------")
    return notGreenCost, months

def getGoneGreen(goneGreenCost, months):
    index = 0
    while index < len(goneGreenCost):
        #Again, I display the months as headers here to avoid having
        #too many arguments in the code input.
        print("\t\t" + months[index])
        goneGreenCost[index] = int(input("Enter GONE GREEN energy costs for this month: "))
        index += 1
    print("-----------------------------------------------")
    return goneGreenCost, months

#Calculation using a bunch of arrays! Cool!
def energySaved(notGreenCost, goneGreenCost, savings):
    index = 0
    while index < len(savings):
        #I picked savings here because all our arrays are 12 elements long anyway.
        savings[index] = notGreenCost[index] - goneGreenCost[index]
        index += 1
    return notGreenCost, goneGreenCost, savings

#Just printing out all the good info for the end user.
def displayInfo(notGreenCost, goneGreenCost, savings, months):
    index = 0
    while index <len(savings):
        #I tried to make it look a little nicer here at the display,
        #but kept in line with the pseudocode.
        #unlike the "your code might look like this!" example.
        print("-----------------------------------------------")
        print("\t\t SAVINGS")
        print("-----------------------------------------------")
        print("Information for: ", months[index])
        print("Savings: $", savings[index])
        print("Not Green Costs: $", notGreenCost[index])
        print("Gone Green Costs: $", goneGreenCost[index])
        #this prevents our savings from running forever
        index += 1

#Call the main function for the user.        
main()
