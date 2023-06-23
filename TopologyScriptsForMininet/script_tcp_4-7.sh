h7 iperf -e -i 1 -s -p 5555 > h7.txt &
h4 iperf -e -i 1 -c h7 -p 5555 -S 0x08 -N -n 100m -l 256k -b 80m -w 80k > h4.txt &