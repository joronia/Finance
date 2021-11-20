def calculatePoints():
    print("Welcome to Point Calculator Enter 'EXIT' to leave")
    
    userInput = input("Should we exit?")

    while (userInput != 'EXIT'):
        
        cashValue = input("What is the cost of the flight in Cash?")
        yourValue = input("What do you value the trip? Is it your priorty for the current cost?")
        feesTaxes = input("What taxes and fees are on this flight ticket?")
        points = input("What is the cost of the flight if using points?")
        pointsForgone = input("How many X number of points per dollar can you earn if purchased with cash eg 5X per dollar spent")
        pointsForgoneCalculation = float(cashValue) * float(pointsForgone)
        print(str(pointsForgoneCalculation))

        centsPerMile = 100 * (float(yourValue) - float(feesTaxes)) / (float(points) + float(pointsForgoneCalculation))

        doubleChaseEarningPerPoint = 1.25 * 2

        if (centsPerMile >= doubleChaseEarningPerPoint):
            print("You are most definetly getting 2X what a Chase point is worth! What a deal! Use Points!\n")
            print("Cents per Mile Value of Award " + str(centsPerMile) + "\n")
        else:
            print("You are better off paying cash for this trip")
            print("Cents per Mile Value of Award " + str(centsPerMile) + "\n")
        
        userInput = input("Should we exit?")

def calculatePointsSecond():
    chasePortalCost = input("What is the cost of the flight in Cash through Chase Portal?")
    transferPartner = input("What is the total points needed with the Chase Partner?")
    totalCostChasePortal = float(chasePortalCost) / float(transferPartner)

    doubleChaseEarningPerPoint = 0.0125 * 2

    if (totalCostChasePortal >= doubleChaseEarningPerPoint):
        print("You are most definetly getting 2X what a Chase point is worth! What a deal! Use Points!\n")
        print("Cents per Mile Value of Award " + str(totalCostChasePortal) + "\n")
    else:
        print("You are better off paying cash for this trip")
        print("Cents per Mile Value of Award " + str(totalCostChasePortal) + "\n")

calculatePointsSecond()
calculatePoints()

