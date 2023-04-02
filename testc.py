from mininet.topo import Topo

class MyTopo(Topo):
	def __init__(self):
            Topo.__init__(self)	
            #Adding host for every city in England
            chesterH = self.addHost('h1')
            manchesterH = self.addHost('h2')
            yorkH = self.addHost('h3')
            nottinghamH = self.addHost('h4')
            oxfordH = self.addHost('h5')
            bristolH = self.addHost('h6')
            bathH = self.addHost('h7')
            cambridgeH = self.addHost('h8')
            londonH = self.addHost('h9')
            brightonH = self.addHost('h10')
            #Adding switches for every host
            chesterS = self.addSwitch('s1')
            manchesterS = self.addSwitch('s2')
            yorkS = self.addSwitch('s3')
            nottinghamS = self.addSwitch('s4')
            oxfordS = self.addSwitch('s5')
            bristolS = self.addSwitch('s6')
            bathS = self.addSwitch('s7')
            cambridgeS = self.addSwitch('s8')
            londonS = self.addSwitch('s9')
            brightonS = self.addSwitch('s10')
            #Links between every host and it's switch
            self.addLink( chesterS,chesterH)
            self.addLink( manchesterS,manchesterH)
            self.addLink( yorkS,yorkH)
            self.addLink( nottinghamS,nottinghamH)
            self.addLink( oxfordS,oxfordH)
            self.addLink( bristolS,bristolH)
            self.addLink( bathS,bathH)
            self.addLink( cambridgeS,cambridgeH)
            self.addLink( londonS,londonH)
            self.addLink( brightonS,brightonH)
            #Links between switches
            self.addLink( chesterS,manchesterS,delay='4ms')
            self.addLink(manchesterS,yorkS,delay='6ms')
            self.addLink(manchesterS,nottinghamS,delay='7ms')
            self.addLink(nottinghamS,oxfordS,delay='7ms')
            self.addLink(oxfordS,londonS,delay='4ms')
            self.addLink(londonS,cambridgeS,delay='5ms')
            self.addLink(bristolS,londonS,delay='1ms')
            self.addLink(brightonS,londonS,delay='5ms')
            self.addLink(bristolS,bathS,delay='1ms')
            self.addLink(chesterS,nottinghamS,delay='7ms')
            self.addLink(yorkS,nottinghamS,delay='8ms')
            self.addLink(manchesterS,bristolS,delay='14ms')
            self.addLink(bristolS,oxfordS,delay='7ms')
            self.addLink(bathS,brightonS,delay='10ms')
            self.addLink(oxfordS,cambridgeS,delay='7ms')
            self.addLink(nottinghamS,londonS,delay='10ms')
            self.addLink(nottinghamS,cambridgeS,delay='8ms')
topos = {'MyTopo':(lambda: MyTopo())}


