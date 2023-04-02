class Reader: 
    def __init__(self,open):
        self.file = open
        self.lineNumber = int(self.file.readline())
        self.lines = self.file.read().splitlines()
    
    def getLineNumber(self):
        return self.lineNumber

    def getFile(self):
        return self.file

    def closeFile(self):
        self.file.close()
    
    def getLine(self,number):
        return self.file.readline(number)
    
    def read(self,lineNumber):
        link = []
        chosenLine = self.lines[lineNumber-1]
        chosenLine = chosenLine.split('-')
        for x in chosenLine:
            link.append(int(x))
        return link