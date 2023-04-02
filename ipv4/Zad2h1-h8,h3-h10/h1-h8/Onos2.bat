curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000001" -d @flows_s1_h1-h6.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000001" -d @flows_s1_h6-h1.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000002" -d @flows_s2_h1-h6.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000002" -d @flows_s2_h6-h1.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000006" -d @flows_s6_h1-h6.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000006" -d @flows_s6_h6-h1.json -H "Content-Type: application/json" -H "Accept: application/json"

pause
