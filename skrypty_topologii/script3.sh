h8 iperf -e -i 1 -s -p 5555 -u > h8.txt &
h6 iperf -e -i 1 -c h8 -p 5555 -P 1 -u -S 0x10 -t 10 -b 20m -w 80k > h6.txt &
