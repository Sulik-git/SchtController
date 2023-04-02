curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000003" -d @flows_s3_h3-h5_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000003" -d @flows_s3_h5-h3_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000004" -d @flows_s4_h3-h5_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000004" -d @flows_s4_h5-h3_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000005" -d @flows_s5_h3-h5_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"
curl --user karaf:karaf -X POST "http://192.168.1.30:8181/onos/v1/flows/of:0000000000000005" -d @flows_s5_h5-h3_ipv4.json -H "Content-Type: application/json" -H "Accept: application/json"

pause
