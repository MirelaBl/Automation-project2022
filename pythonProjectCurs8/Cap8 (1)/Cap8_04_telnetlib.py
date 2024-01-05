"""
804 Module
Modulul telnetlib - exemple
PF - 29.06.2021 v6
"""  #

import telnetlib

host = 'route-server.he.net'
obiect = telnetlib.Telnet(host)

obiect.read_until(b'Login: ', 2)
obiect.read_until(b'Password: ', 2)

obiect.write('show ip bgp summary'.encode('utf-8') + b'\r\n')
s = obiect.read_until(b'free', 2)
for i in str(s).split(','):
    print(i)
i.split("\\r\\n")

obiect.write('show ip bgp neighbors'.encode('ascii') + b'\r\n')
str(obiect.read_until(b'free', 2)).split("\\r\\n")

obiect.write('show version'.encode('ascii') + b'\r\n')
print(obiect.read_until(b'free', 2))

obiect.write('show ip bgp 8.8.8.8'.encode('ascii') + b'\r\n')
result = obiect.read_until(b'free', 2)
str(result).split("\\r\\n")

obiect.close()
