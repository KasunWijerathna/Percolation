def randomGenarate():
    import random
    #creating varibles
    number = 10
    randomList = [" "]
    select = ""
    while number < 100:
        if number % 10 == 0 or number == 99:
            randomList.append(number)
            randomList.append(" ") #How to get spaces and 10-99 numbers randomly between the random list
            number += 1
        else:   
            randomList.append(number)
            number += 1
    select = str(random.choice(randomList))
    return select

def percolation(user):
    #creating varibles
    global mainList
    mainList = []
    subList = []
    count1 = 0
    count2 = 0
    try:
        if 3 <= int(user[0]) <= 9 and 3 <= int(user[2]) <= 9 and user[1] == "x" or user[1] =="X": #If user enter the numbers as dimention this is how it showing
            print("1. The above creates a "+user+" grid")
            while count1 < int(user[2]):
                subList = []
                count2 = 0
                while count2 <= int(user[0]):
                    if count2 == int(user[0]):
                        if " " in subList:
                            subList.append("NO")
                            break
                        else:
                            subList.append("OK")
                            break
                    else:
                        subList.append(randomGenarate())
                        count2 += 1
                mainList.append(subList)
                count1 += 1
        else:
            print("1. The above creates a 5x5 default grid ")  #if user doesn't enter the numbers as dimentions show default one.
            while count1 < 5:
                subList = []
                count2 = 0
                while count2 <= 5:
                    if count2 == 5:
                        if " " in subList:
                            subList.append("NO")
                            break
                        else:
                            subList.append("OK")
                            break
                    else:
                        subList.append(randomGenarate())
                        count2 += 1
                mainList.append(subList)
                count1 += 1
            
    except:
        print("1. The above creates a 5x5 default grid ")
        while count1 < 5:
            subList = []
            count2 = 0
            while count2 <= 5:
                if count2 == 5:
                    if " " in subList:
                        subList.append("NO")#space in there show NO
                        break
                    else:
                        subList.append("OK") #If space isn't in there show OK
                        break
                else:
                    subList.append(randomGenarate())
                    count2 += 1
            mainList.append(subList)
            count1 += 1       
    return mainList


#How to make a pretty table
def printResult():
    from prettytable import PrettyTable
    #creating varibles
    count = 1
    table = PrettyTable()
    for item in mainList:
        table.add_column(str(count),item)
        count += 1
    print(table)





