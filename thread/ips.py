import ipaddress

ip = "192.169.0.1"

adress = ipaddress.ip_address(ip)



rede = "192.169.0.100/24"

network = ipaddress.ip_network(rede, strict = False)

print(network) 