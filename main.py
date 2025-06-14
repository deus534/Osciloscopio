import sys
import re
import serial

from serial.tools.list_ports import comports


def choose_port():
    ports = comports()
    size = 0
    ports_filter = []
    for p in ports:
        if not re.match(r'/dev/ttyS\d+', str(p)):
            print(f'{size}: {p}')
            size+=1
            ports_filter.append(re.sub(r' .*','',str(p)))
    ports_filter.append('')
    print(f'{size}: exit')
    return ports_filter[int(input('Select de port: '))]

if __name__=='__main__':

    port = choose_port()
    if port=='':
        exit(1)
    
    com = serial.Serial(port, 9600)
    while True:
        mssg_received = com.readline()
        print(mssg_received)

