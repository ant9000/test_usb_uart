#!/usr/bin/env -S python3 -u

import sys, serial, time

device = '/dev/ttyACM1'
baud = 115200
count = -1
if len(sys.argv) > 1:
    device = sys.argv[1]
if len(sys.argv) > 2:
    count = int(sys.argv[2])

s = serial.Serial(device, baud, timeout=0)
i = 0
try:
    while True:
        for c in range(32,127):
            i += 1
            s.write(bytes([c]))
            print(chr(c), end='')
            if i % 80 == 0:
                print('')
            if count > 0 and i == count:
                raise KeyboardInterrupt
except KeyboardInterrupt:
    print("")
    print("Sent %d characters." % i)
