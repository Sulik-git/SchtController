import json

class Makejson:


    def __init__(self):
        self.my_json = {
    "priority": 40000,
    "timeout": 0,
    "isPermanent": True,
    "deviceId": "of:000000000000000a",
    "treatment": {
        "instructions": [
        {
            "type": "OUTPUT",
            "port": "1"
        }
        ]
    },
    "selector": {
        "criteria": [
        {
            "type": "IN_PORT",
            "port": "2"
        },
        {
            "type": "ETH_TYPE",
            "ethType": "0x0800"
        },
        {
            "type": "IPV4_DST",
            "ip": "10.0.0.a/32"
        }
        ]
    }
    }



    def makeJson(self,device,portIn,portOut,destination):
        if device != 10:
            self.my_json.update({"deviceId":f"of:000000000000000{device}"})
        self.my_json.update({"treatment":{"instructions":[{"type":"OUTPUT","port":f"{portOut}"}]}})
        self.my_json.update({"selector":{"criteria":[
            {"type":"IN_PORT","port":f"{portIn}"},{"type":"ETH_TYPE","ethType":"0x0800"},{"type":"IPV4_DST","ip":f"10.0.0.{destination}/32"}]}})

            
        myJson = json.dumps(self.my_json)
        #print(myJson)
        return myJson