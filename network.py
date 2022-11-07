import netifaces as ni
from scapy.all import *
import socket
import json

mac_address_list = []
ip_address_list = []
devices_dictionary = []
ev3dev_devices_info = []



with open('dictionary.json') as json_file:
    data = json.load(json_file)
    print(data)

def get_ip_with_cidr():
    global adapters_name
    network_address = ''
    x = ni.interfaces()
    print(x)
    index = x.index("wlan0")
    info = ni.ifaddresses(x[index])
    netmask_value = info[ni.AF_INET][0]['netmask']
    ip_address = info[ni.AF_INET][0]['addr']
    _ = ip_address.split(".")
    for i in range(3):
        network_address = network_address + _[i] + "."
    network_address = network_address + '1'
    res = network_address + data[netmask_value]
    return res
"""
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff;ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 0.25, verbose = False)[0]
    
    clients_list = []
    for elements in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

main_ip = get_ip_with_cidr()
temp = main_ip.split(".")
print(temp)
ip = ".".join(str(temp[n]) for n in range(3))
ip = ip + "."
print(ip)
print(type(ip))
print("IP"+"\t\t\t"+"MAC")
for i in range(0,256):
    curr_ip = ip + str(i)
    scan_result = scan(curr_ip)
    if scan_result != []:
        print(scan_result[0]['ip']+"\t\t"+scan_result[0]['mac'])
"""

target_ip = get_ip_with_cidr()
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
result = srp(packet, timeout=3, verbose=0)[0]
clients = []

for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))