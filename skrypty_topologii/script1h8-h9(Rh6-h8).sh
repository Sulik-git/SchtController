h8 iperf -e -i 1 -s -p 5555 > h8.txt &
h6 iperf -e -i 1 -c h8 -p 5555 -P 1 -N -S 0x08 -n 100m -l 10m -b 5m -w 80k > h9.txt &
