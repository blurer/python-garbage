#!/usr/bin/env python3

from tcping import Ping

print('Network Test')
print('')
pingHost = input('Host: ')
pingPort = input('Port: ')
pingCount = input('Count: ')

ping = Ping(pingHost, pingPort)
ping.ping(int(pingCount))