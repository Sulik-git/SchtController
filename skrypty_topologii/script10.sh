h1 iperf -e -i 1 -s -p 5555 -u > h1.txt &
h3 iperf -e -i 1 -s -p 5111 -u > h3.txt &
h5 iperf -e -i 1 -c h1 -p 5555 -P 1 -u -S 0x10 -t 10 -b 80m -w 80k > h5.txt &
h4 iperf -e -i 1 -c h3 -p 5111 -P 1 -u -S 0x10 -t 10 -b 30m -w 80k > h4.txt & 

