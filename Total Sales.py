#Sabrina Turney
#October 8, 2018
#Total Sales
#The purpose of this program is to get a user's input for sales on each day of
#the week, store the values in an array, and then calculate the
#total sales amount for the week and display it to the user.

#I start with an introduction module for a pretty start to our program
def printIntro():
    print("Welcome to my program!")
    print("If you input the sales for the week,")
    print("I'll display your total sales for the week!")

#Our main module. I start off by declaring the days of the week in their
#own array, which we'll assign values to later.
#salesCost is set to an empty array because the user will input the data.
#And totalSales is set to a float value because we're using money in sales.
def main():
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    salesCost = [0] * 7
    totalSales = 0.0
#I call all my modules here, just to keep my main one nice and concise.
    printIntro()
    getSales(weekdays, salesCost)
    getTotal(salesCost, totalSales)

#This module runs a loop to get the sales values for each day of the week
#from the user, and returns it to main. It also prints out a pretty
#summary of the numbers entered by the user before the final
#calculation is made.
def getSales(weekdays, salesCost):
    index = 0
    while index < len(weekdays):
        print("\t\n" + (weekdays[index]))
        salesCost[index] = float(input("Enter your sales for this day! "))
        index += 1
    print("\nThese were the sales numbers entered for this week: \n",(salesCost))
    return weekdays, salesCost

#This module does the actual calculation to get the total sales for the week
#for the user. I use the sum operator built-in to python to make it clear,
#and then print out a nice display to the user of their sales, making
#sure to keep it looking like money, and not an endless decimal.
def getTotal(salesCost, totalSales):
    totalSales = sum(salesCost)
    print("\nWow! Your total sales for the week added up to: $%0.02f" %totalSales)
    return salesCost, totalSales

#Finally, we call the main function for the user.
main()
