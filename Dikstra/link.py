class Link:

    def __init__(self,rawLink):
        self.rawLink = rawLink
        self.sp = {}
        self.latency = 0
        self.bandwith = 0
        self.switches = []
        self.ports = []
        self.divideRawklink()
    
    def getSwitch(self,number):
        return self.switches[number]
    
    def getPort(self,number):
        return self.ports[number]
    
    def getBandwith(self):
        return self.bandwith
        
    def getLatency(self):
        return self.latency
    def getPortBySwitch(self,switch):
        if switch in self.sp:
            return self.sp.get(switch)
        else:
            print("ERR: No item in the dictionary")
    
    def linkMatch(self,switch1,switch2):
        if switch1 in self.switches and switch2 in self.switches:
            return True
        else:
            return False
        
    def divideRawklink(self):
        self.switches.append(self.rawLink.pop(0))
        self.switches.append(self.rawLink.pop(0))
        self.ports.append(self.rawLink.pop(0))
        self.ports.append(self.rawLink.pop(0))
        self.latency = self.rawLink.pop(0)
        self.bandwith = self.rawLink.pop(0)
        self.sp.update({self.switches[0]:self.ports[0]})
        self.sp.update({self.switches[1]:self.ports[1]})