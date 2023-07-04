from dijkstar import Graph, find_path
from reader import Reader
from switch import Switch
from link import Link
import requests
from makejson import Makejson
from pathlib import Path
import sys

arguments = sys.argv[1:]

mode = ''
source = 0
destination = 0
file_path = ''

arg = 0
for a in arguments:                                     # Reading given console arguments
    if '--mode' in a:
        mode = arguments[arguments.index(a) + 1]
        arg = arg + 1
    if '--src' in a:
        source = int(arguments[arguments.index(a) + 1])
        arg = arg + 1
    if '--dst' in a:
        destination = int(arguments[arguments.index(a) + 1])   
        arg = arg + 1
    if '--file' in a:
        file_path = arguments[arguments.index(a) + 1]
        arg = arg + 1



if arg < 4:                                                                            
    print("ERR: Not enough arguments. Program needs 4 args: --mode --src --dst --file")                      # Instantiates links from link txt file
else: 
    links = []
    try:
        graph = Graph()
    except:
        print("ERR: Graph init error")

    try:
        p1 = Path(__file__).with_name(file_path)
        r = Reader(p1.open("r"))
        num = 1
        for x in range(0,r.getLineNumber()): 
            link = Link(r.readLinks(num))               
            links.append(link)
            num = num + 1
    except:
        print("ERR: Reader error")



    try:                                                                            # Depending on given arguments chooses wright mode
        if mode == 'tcp': 
            for x in links:
                graph.add_edge(x.getSwitch(0),x.getSwitch(1),(1/x.getBandwith()))
        elif mode == 'udp':                                                                        
            for x in links:
                graph.add_edge(x.getSwitch(0),x.getSwitch(1),x.getLatency())
        else:
            print("ERR: Wrong mode choosen")
    except:
        print("ERR: Adding switches to graph failed")

    try:
        path = find_path(graph,int(source),int(destination))[0]             # Finding shortest path
    except:
        print("ERR: Finding path failed")




    switches = []
    num = 1
    isInList = 0

    for x in range(0,len(path)-1):                          # Creating switches
        for t in links:
            check = t.linkMatch(path[num-1],path[num])
            if check:
                if switches:
                    for s in t.switches:
                        for z in switches:

                            if z.getNumber() == s:
                                isInList = 1    
                                z.addPort(t.getPortBySwitch(s))

                        if isInList == 0:
                            switch = Switch(s,int(source),int(destination))
                            switch.addPort(t.getPortBySwitch(s))
                            switches.append(switch)
                        isInList = 0 

                else:
                    for s in t.switches:
                        switch = Switch(s,source,destination)
                        switch.addPort(t.getPortBySwitch(s))
                        switches.append(switch) 

        num = num + 1



    for s in switches:                                                                  # Creating two configuration json files for every created switch
        if s.getNumber() == 10:
            url1 = f"http://192.168.1.30:8181/onos/v1/flows/of:000000000000000a"
        else:
            url1 = f"http://192.168.1.30:8181/onos/v1/flows/of:000000000000000{s.getNumber()}"
            

        json_output = str(Makejson().makeJson(s.getNumber(),s.getPort(0),s.getPort(1),s.destination))
        p2 = Path(__file__).with_name('test.json')


        with p2.open("w") as outfile:
            outfile.write(json_output)

        file = open('test.json','rb')
        output = file.read()
        resp1 = requests.post(url1,data=json_output,auth=("karaf","karaf"))
        file.close()


        if str(resp1) == '<Response [201]>':
            print(f"Topology updated for switch {s.getNumber()}")
        else:
            print(f"ERR: Topology not updated for switch {s.getNumber()}")

        json_output = str(Makejson().makeJson(s.getNumber(),s.getPort(1),s.getPort(0),s.source))
        p2 = Path(__file__).with_name('test.json')

        with p2.open("w") as outfile:
            outfile.write(json_output)

        file = open('test.json','rb')
        output = file.read()
        resp1 = requests.post(url1,data=json_output,auth=("karaf","karaf"))
        file.close()

        if str(resp1) == '<Response [201]>':
            print(f"Topology updated for switch {s.getNumber()}")
        else:
            print(f"ERR: Topology not updated for switch {s.getNumber()}")