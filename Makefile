APPLICATION = test_usb_uart
BOARD ?= samr34-xpro
RIOTBASE ?= $(CURDIR)/../RIOT
QUIET ?= 1
DEVELHELP ?= 1

USEMODULE += stdio_cdc_acm
USEMODULE += periph_uart
USEMODULE += xtimer

CFLAGS += -DCONFIG_SKIP_BOOT_MSG=1

include $(RIOTBASE)/Makefile.include
