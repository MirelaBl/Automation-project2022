"""
803 Module
Modulul ntplib - exemple
PF - 29.06.2021 v6
"""  #

import ntplib
import time

# Servere ntp Romania: 0.ro.pool.ntp.org;	1.ro.pool.ntp.org;	2.ro.pool.ntp.org;	3.ro.pool.ntp.org
# Lista servere din toata lumea http://support.ntp.org/bin/view/Servers/StratumOneTimeServers
# (click pe campul ISO)

ob = ntplib.NTPClient()
host_ro = "1.ro.pool.ntp.org"
host_fr = "ntp-p1.obspm.fr"

r = ob.request(host_ro, 2, 123, 5)  # Ex: server Romania
time.ctime(r.tx_time)

v = ob.request(host_fr, 2, 123, 5)  # Ex: server Franta
time.ctime(v.tx_time)

print(v.orig_time)

if time.ctime(ob.request(host_fr, 2, 123, 5).tx_time) == time.ctime(ob.request(host_ro, 2, 123, 5).tx_time):
    print('Ceasuri sincronizate!')
