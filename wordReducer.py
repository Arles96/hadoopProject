def remove(line):
    notWanted = ["is", "the", "and", "of", "to", "a", "or", "for", "in", "at", "than", "my", 
    "you", "me", "an", "but", "do", "fuck", "shit", "that", "he", "she", "i", "ah", "oh", "no", "yes",
    "ok", "so", "us", "am", "ass", "be", "bro", "does", "did", "dr", "etc", "go", "jpg", "too", "it", 
    "gg", "gt", "if", "its", "her", "aren t", "isn t", "this", "sir", "on", "not", "him", "don", "doesn",
    "www", "com", "http", "one", "re", "can", "has", "r", "lw", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "f", "porn", "by", "off", "s", "t", "\t", "source", "fb"]

    line = " " + line
    for word in notWanted:
        spaced = " " + word + " "
        line = line.replace(spaced, " ")

    return line[1:]

inPath = './ReducedFile.txt'
outPath = './removedWords.txt'

inFile = open(inPath, 'r')
outFile = open(outPath, 'x')

cnt = 0

while True:
    line = inFile.readline()

    if not line:
        break

    line = remove(line.lower())
    cnt = cnt + len(line)
    print("Processed", (cnt / 1024) / 1024,"MB")
    outFile.write(line)
    
print("End of file")