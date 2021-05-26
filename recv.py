#!/usr/bin/env -S python3 -u

import sys, serial, time

device = '/dev/ttyACM0'
baud = 115200
if len(sys.argv) > 1:
    device = sys.argv[1]

s = serial.Serial(device, baud)
i = 0
try:
    while True:
        c = s.read()
        if c:
            i += 1
            print(c.decode('utf8'), end='')
            if i % 80 == 0:
                print('')
except KeyboardInterrupt:
    print("")
    print("Received %d characters." % i)
