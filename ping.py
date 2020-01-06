#!/usr/bin/env python3

import os

hostname = "1.1.1.1"
response = os.system("ping -c 1 " + hostname)

if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')