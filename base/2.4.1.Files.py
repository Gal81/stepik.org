with open('base\\dump\\fileIn.txt', 'r') as fileIn, open('base\\dump\\fileOut.txt', 'w') as fileOut:
    lines = fileIn.read().splitlines()
    fileOut.write('\n'.join(reversed(lines)))