#Class resposnible for creating switches 

class Switch:
    source = 0
    destination = 0

    def __init__(self,number,source,destination):
        self.number = number
        self.source = source
        self.destination = destination
        self.ports = []
        self.host = False
    
    def getNumber(self):
        return self.number
    
    def getPort(self,num):
        return self.ports[num]
    
    def setHost(self):
        self.host = True
    
    def getHost(self):
        return self.host
    
    def addPort(self,port):
        if self.number == self.source:
            self.ports.append(1)
            self.ports.append(port)
        elif self.number == self.destination:
            self.ports.append(port)
            self.ports.append(1)
        else:
            self.ports.append(port)


