#include "board.h"
#include "periph/uart.h"
#include "stdio_base.h"
#include "xtimer.h"

static void rx_cb(void *arg, uint8_t data)
{
    (void)arg;
    stdio_write(&data, 1);
}

int main(void)
{
    uint8_t c;

    uart_init(UART_DEV(0), 115200, rx_cb, NULL);

    while(1) {
        if (stdio_read(&c, 1) == 1) {
            uart_write(UART_DEV(0), &c, 1);
            xtimer_usleep(30000);
        }
    }
    return 0;
}
