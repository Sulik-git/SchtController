import requests
import sys

host = "192.168.11.20"
host2 = "192.168.1.30"
host3 = "192.168.247.20"
port = "8181"
service1 = "flows/of:000000000000000a"
service2 = "flows/of:0000000000000007"
username = "karaf"
password = "karaf"
url1 = f"http://{host2}:{port}/onos/v1/{service1}"
url2 = f"http://{host2}:{port}/onos/v1/{service2}"
headers = {'Content-type': 'application/json'}


#file = open('flows.json','w')
file1 = open('ipv4/flows_s10_h4-h7_ipv4.json','rb').read()
file2 = open('ipv4/flows_s10_h7-h4_ipv4.json','rb').read()
file3 = open('ipv4/flows_s7_h4-h7_ipv4.json','rb').read()
file4 = open('ipv4/flows_s7_h7-h4_ipv4.json','rb').read()
#print(file.read())
resp1 = requests.post(url1,data=file1,auth=(username,password))
resp2 = requests.post(url2,data=file3,auth=(username,password))
resp3 = requests.post(url1,data=file2,auth=(username,password))
resp4 = requests.post(url2,data=file4,auth=(username,password))
#file.write(str(requests.get(url,auth=(username,password)).text))

print(resp1.text)
print(resp2.text)

