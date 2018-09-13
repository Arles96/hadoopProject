def getNumber(st):
    c = 0
    con = ""
    while True:
        c = c - 1
        if st[c] != '\t':
            con = st[c] + con
        else :
            break
    return float(con)

greaterThan = 1
lessThan = 500

inPath = './countedData(2).txt'
outPath = './maxedData' + str(greaterThan) + '.txt'

inFile = open(inPath, 'r')
outFile = open(outPath, 'x')

cnt = 0
while lessThan < 10000:
    outPath = './rangedData(' + str(greaterThan) + ", " + str(lessThan) + ').txt'
    outFile = open(outPath, 'x')
    while True:
        line = inFile.readline()
        if not line:
            break
        numberLine = getNumber(line[:len(line) - 1])

        if numberLine > greaterThan and numberLine < lessThan :
            cnt = cnt + 1
            print("Processed ", cnt," Lines in range(",greaterThan, ",", lessThan,")")
            outFile.write(line)
    cnt = 0
    inFile.seek(0)
    greaterThan = greaterThan + 500
    lessThan = lessThan + 500
    
print("End of file")
