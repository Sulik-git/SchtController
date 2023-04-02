# Reader class responsible for opening topology file, determining number of lines in file, reading and 
# returning links written in topology file 

class Reader: 
    
    # Constructor accepts path to the topology file
    def __init__(self, open):
        self.file = open
        self.lineNumber = int(self.file.readline())
        self.lines = self.file.read().splitlines()
    
    # Returns nubmer of written lines in file
    def getLineNumber(self):
        return self.lineNumber

    def getFile(self):
        return self.file

    def closeFile(self):
        self.file.close()
    
    # Returns topology file's line of a given number
    def getLine(self,number):
        try:
            return self.file.readline(number)
        except:
            print("ERR: Given line doesn't exist in given file")
    
    # Reads and returns links from given topology file
    def readLinks(self,lineNumber):
        link = []
        chosenLine = self.lines[lineNumber-1]
        chosenLine = chosenLine.split('-')
        for x in chosenLine:
            link.append(int(x))
        return link