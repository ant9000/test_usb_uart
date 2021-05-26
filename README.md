PoC: RIOT driver for STDIO CDC ACM drops characters
---------------------------------------------------

The STDIO over CDC ACM read callback copies received data [withouth checking if there is space available](https://github.com/RIOT-OS/RIOT/blob/master/sys/usb/usbus/cdc/acm/cdc_acm_stdio.c#L79).

AFAICT, the problem originates in the [_transfer_handler function](https://github.com/RIOT-OS/RIOT/blob/master/sys/usb/usbus/cdc/acm/cdc_acm.c#L347) in CDC ACM, which has no way of knowing if the callback correctly fetched all data or not.


TESTING
-------

The PoC is written for a samr34-xpro, but it's not really board-specific. The basic requirements are an USB port for STDIO, an UART port where the traffic received from USB will be forwarded, and a LED to show that a drop has occurred.

The file `riot_usbus_cdc_acm_stdio.patch` needs to be applied to the RIOT tree: it is a straightforward patch to `sys/usb/usbus/cdc/acm/cdc_acm_stdio.c` that turns on LED0 when a character gets dropped.

Connect both the USB and the UART to your PC. Launch `./recv.py`: by default it listens to /dev/ttyACM0 - if the UART port is attached to a different device node, you can pass it as a first argument.

On a different shell, launch `./send.py` to send some data. The first argument is again a device name - /dev/ttyACM1 by default, which is expected to be the USB port. A second optional argument specifies how many bytes to send.

With the default 128 bytes buffer, sending 130 bytes with

```
./send.py /dev/ttyACM1 130
```

is enough for seeing the LED turn on.
