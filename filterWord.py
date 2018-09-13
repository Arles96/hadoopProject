filterWord = "attack"

inPath = './countedData.txt'
outPath = './filteredData(' + filterWord + ').txt'

inFile = open(inPath, 'r')
outFile = open(outPath, 'x')

cnt = 0

while True:
    line = inFile.readline()
    if filterWord in line.lower():
        cnt = cnt + 1
        print("Processed ", cnt," Lines")
        outFile.write(line)

    if not line:
        break
print("End of file")
