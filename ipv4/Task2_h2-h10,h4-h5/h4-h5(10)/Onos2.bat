curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000004" -d @flows_s4_h4-h10.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000004" -d @flows_s4_h10-h4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000009" -d @flows_s9_h4-h10.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000009" -d @flows_s9_h10-h4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:000000000000000a" -d @flows_s10_h4-h10.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:000000000000000a" -d @flows_s10_h10-h4.json -H "Content-Type: application/json" -H "Accept: application/json"

pause
