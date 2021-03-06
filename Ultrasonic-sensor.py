from machine import UART

uart = UART(1)
uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=190)

while True: #Oneindige loop
    header_bytes = uart.read(1)
    data_header = int(uart.read(1)[0])
    data_high = int(uart.read(2)[0])
    data_low = int(uart.read(3)[0])
    distance = data_high*256 + data_low
    #Is de data/Getal kleiner dan 1000 dan print hij die anders print hij niets
    if int(distance/10) < 1000:
        print("afstand",int(distance/10), "cm") #print "afstand" + getal + "cm"
