#!/usr/bin/env python3

from tcping import Ping

print('')
print('TCP Ping Test')
print('------------------')
pingHost = input('Host: ')
pingPort = input('TCP Port: ')
pingCount = input('Count: ')
print('------------------')
print('')
ping = Ping(pingHost, pingPort)
ping.ping(int(pingCount))