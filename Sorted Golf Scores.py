#Sabrina Turney
#October 8, 2018
#Sorted Golf Scores
#The purpose of this program is to get user input for 10 golf scores, store them
#in an array, and then sort the array in ascending order and display it for user


#Here's our nice introduction module as always, keeping it clean.
def printIntro():
    print("Welcome to my golf score sorting program!")
    print("In this program, you will provide 10 scores in your golf game,")
    print("And I'll sort them in ascending order for you!")

#Our main module, which does all the heavy lifting this program with lists.
def main():

    #First, we call our pretty introduction
    printIntro()
    #Then we declare our lists. I type out the score numbers for clarity.
    userScores = [0] * 10
    scoreNumber = ["One", "Two", "Three", "Four", "Five", "Six", "Seven",
                   "Eight", "Nine", "Ten"]

    #We start the repetition structure here to assign all our values for scores.
    index = 0
    while index < len(userScores):
        print("\nScore " + str((scoreNumber[index])))
        userScores[index] = int(input("Enter your score here: "))
        index += 1

    print("\nYour original score list was, ", userScores)
    #Print out the original list for the user, then apply the built-in sort
    #function and print out the pretty list that the user wants!
    print("Your list sorted in ascending order is, ", sorted(userScores))

#Last but not least, we call main for the user.
main()
