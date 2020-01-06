#!/usr/bin/env python3

import ipaddress

ipHost = str('Host IP/mask: ')

print('')
print('Subnet; ' , ipHost.network)
print('DNS PTR: ', ipaddress.ip_address(ipHost).reverse_pointer)
print('')