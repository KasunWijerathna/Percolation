#creating varibles
count = 0
fo = ""

fo = open("count.txt","r")
count = fo.read()
fo = open("count.txt","w") #when the program running count+1 in the text file which called count.txt
fo.write(str(int(count)+1))
fo.close()

def dataText(mainList):
    #creating varibles
    fo = ""
    count1 = 0
    count2 = 0
    fo = open(str(count)+".txt","w") #how to get separate text files
    while count1 < len(mainList[0]):
        for item in mainList:
            if item[count1] == " ":   
                fo.write(item[count1])
                fo.write("  ")
                count2 += 1
            else:
                fo.write(item[count1])
                fo.write(" ")
                count2 += 1
                
        fo.write("\n")
        count1 += 1
    fo.close()

def dataHtml(mainList):  #how to save showing results in html file
    #creating varibles
    start = "<html><head><title>"+str(count)+"html</title></head><body><table border=1>"
    end = "</table></body></html>"
    fullText = ""
    fo = ""
    count1 = 0
    count2 = 0
    fo = open(str(count)+".html","w")
    fullText = start
    while count1 < len(mainList[0]):
        fullText = fullText + "<tr>"
        for item in mainList: 
            fullText = fullText + "<th>" + item[count1] + "</th>"
            count2 += 1
        fullText = fullText + "</tr>"
        count1 += 1
    fullText = fullText + end
    fo.write(fullText)
    fo.close()

