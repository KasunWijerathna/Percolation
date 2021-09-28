import sys
import package.percolationGenarate
import dataStore.data

#creating varibles
user = ""
mainList = ""


try:  
    user = sys.argv[1]
    mainList = package.percolationGenarate.percolation(user)
    package.percolationGenarate.printResult()
    dataStore.data.dataText(mainList)
    dataStore.data.dataHtml(mainList)
    
except:
    user = ""
    mainList = package.percolationGenarate.percolation(user)
    package.percolationGenarate.printResult()
    dataStore.data.dataText(mainList)
    dataStore.data.dataHtml(mainList)
