h1 iperf -e -i 1 -s -p 5555 -u > h1d.txt &
h10 iperf -e -i 1 -c h1 -p 5555 -P 1 -S 0x10 -u -w 150k > h10d.txt &
