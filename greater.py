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

greaterThan = 90000

inPath = './countedData(2).txt'
outPath = './maxedData' + str(greaterThan) + '.txt'

inFile = open(inPath, 'r')
outFile = open(outPath, 'x')

cnt = 0

while True:
    line = inFile.readline()
    if not line:
        break

    if getNumber(line[:len(line) - 1]) > greaterThan :
        cnt = cnt + 1
        print("Processed ", cnt," Lines")
        outFile.write(line)
    
print("End of file")
