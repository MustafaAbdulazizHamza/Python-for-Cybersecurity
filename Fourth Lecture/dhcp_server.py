from netmiko import ConnectHandler
IP = "10.1.1.5"
user = "admin"
passwd = "admin"
deviceType = "cisco_ios"
enable_password = "1234" # enable secret 1234

device = ConnectHandler(host=IP, username=user, password = passwd, device_type=deviceType, secret=enable_password)
# Configure a DHCP server for each of the following networks:
#  192.168.4.0/24, 192.168.5.0/24, 192.168.6.0/24, 192.168.7.0/24
# Gateway = net.1
networks = ["192.168.4", "192.168.5", "192.168.6", "192.168.7"]
for network in networks:
    config_cmds = ["ip dhcp excluded-address {}.1".format(network),
                   "ip dhcp pool Pool{}".format(network.split(".")[2]), # network.split(".")[2] = 4, 5, 6, 7
                   "network {}.0 255.255.255.0".format(network),
                   "default-router {}.1".format(network)]
    device.send_config_set(config_cmds)
device.disconnect()