h1 iperf -e -i 1 -s -p 5555 > h1.txt &
h5 iperf -e -i 1 -c h1 -p 5555 -S 0x08 -N -n 100m -l 256k -b 80m -w 80k > h5.txt &
