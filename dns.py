#!/usr/bin/env python3

import ipaddress

ipHost = input('Host IP/mask: ')

print('')
print('DNS PTR:', ipaddress.ip_address(ipHost).reverse_pointer)
print('')