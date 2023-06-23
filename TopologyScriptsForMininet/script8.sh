h2 iperf -e -i 1 -s -p 5555 > h2.txt &
h7 iperf -e -i 1 -s -p 5111 > h7.txt &
h8 iperf -e -i 1 -c h7 -p 5111 -P 1 -S 0x08 -N -n 100m -l 256k -b 20m -w 80k > h8.txt &
h9 iperf -e -i 1 -c h2 -p 5555 -P 1 -S 0x08 -N -n 100m -l 256k -b 50m -w 80k > h9.txt & 

