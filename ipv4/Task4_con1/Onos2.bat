curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000001" -d @flows_s1_h1-h5_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000001" -d @flows_s1_h5-h1_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000002" -d @flows_s2_h1-h5_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000002" -d @flows_s2_h5-h1_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000004" -d @flows_s4_h1-h5_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000004" -d @flows_s4_h5-h1_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000005" -d @flows_s5_h1-h5_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000005" -d @flows_s5_h5-h1_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"

pause
