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

def travelPartnerPoints():
    chase = set(("Aer Lingus","Air Canada Aeroplan","British Airways","Emirates","Flying Blue (Air France/KLM)","Hyatt","Iberia","IHG","JetBlue","Marriott","Singapore Airlines","Southwest","United","Virgin Atlantic"))
    bilt = set(("American Airlines AAdvantage","Air Canada Aeroplan","Emirates","Flying Blue (Air France/KLM)","Turkish Miles & Smiles","Virgin Atlantic","Hawaiian Airlines HawaiianMiles","Hyatt","IHG"))
    capitalOne = set(("Aeromexico Club Premier","Air Canada Aeroplan","Flying Blue (Air France/KLM)","ALL Accor Live Limitless","Avianca LifeMiles","British Airways","Cathay Pacific Asia Miles","Emirates","Etihad Guest","EVA Infinity MileageLands","Finnair Plus","Qantas Frequent Flyer","Singapore Airlines KrisFlyer","Turkish Miles & Smiles","TAP Portugal Miles&Go","Wyndham Rewards"))
    ableToCombine = set(('Air Canada Aeroplan', 'Emirates', 'Flying Blue (Air France/KLM)','Turkish Miles & Smiles','British Airways','Hyatt', 'Virgin Atlantic','IHG'))

    combinedChaseAndBiltCommon = (chase & bilt)
    combinedChaseAndCaptialOneCommon = (chase & capitalOne)
    combinedBiltAndCapitalOneCommon = (bilt & capitalOne)
    combinedUnique = (combinedChaseAndBiltCommon & capitalOne)
    
    print("Places to combine all credit cards points are, " + str(sorted(combinedUnique)))
    print("Places to combine both bilt and Capital One miles are, " + str(sorted(combinedBiltAndCapitalOneCommon.difference(combinedUnique))))
    print("Places to combine both Chase and Capital One miles are, " + str(sorted(combinedChaseAndCaptialOneCommon.difference(combinedUnique))))
    print("Places to combine both Chase and bilt miles are, " + str(sorted(combinedChaseAndBiltCommon.difference(combinedUnique))))
    print("\n")
    print("Unique to Chase Transfer Partners " + str(sorted(chase.difference(ableToCombine))))
    print("Unique to Bilt Transfer Partners " + str(sorted(bilt.difference(ableToCombine))))
    print("Unique to Capital Transfer Partners " + str(sorted(capitalOne.difference(ableToCombine))))
    
    print("\n")
    print("Use Turkish and Aeroplan to book United Airlines, use KLM or Air France or Virgin Atlantic to book Delta flights, you can use Emirates & Hawaiian Airlines HawaiianMiles to book Jet Blue, use British Airways for American Airlines and Alaska Airlines")

travelPartnerPoints()
#calculatePointsSecond()
#calculatePoints()

