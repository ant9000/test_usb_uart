PoC: RIOT driver for STDIO CDC ACM drops characters
---------------------------------------------------

The STDIO over CDC ACM read callback copies received data [withouth checking if there is space available](https://github.com/RIOT-OS/RIOT/blob/master/sys/usb/usbus/cdc/acm/cdc_acm_stdio.c#L79).

The file `riot_usbus_cdc_acm_stdio.patch` can be used for visualizing the problem: it simply turns LED0 on when a drop occurs.

AFAIKT, the problem originates in the [_transfer_handler function](https://github.com/RIOT-OS/RIOT/blob/master/sys/usb/usbus/cdc/acm/cdc_acm.c#L347) in CDC ACM, which has no way of knowing if the callback correctly fetched all data or not.
