h2 iperf -e -i 1 -s -p 5555 > h2.txt &
h5 iperf -e -i 1 -s -p 5111 > h5.txt &
h4 iperf -e -i 1 -c h5 -p 5111 -P 1 -S 0x08 -N -n 100m -l 256k -b 20m -w 80k > h4.txt &
h10 iperf -e -i 1 -c h2 -p 5555 -P 1 -S 0x08 -N -n 100m -l 256k -b 80m -w 80k > h10.txt & 

