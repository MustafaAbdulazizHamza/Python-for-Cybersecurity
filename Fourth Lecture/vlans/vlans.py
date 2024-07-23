from netmiko import ConnectHandler
for i in [2, 3]:
    try:
        device = ConnectHandler(device_type = "cisco_ios",
                                host=f"10.1.1.{i}", username='admin', password = 'admin', secret='1234')
        # Create the Vlans
        for v in [2,3]:
            device.send_config_set([f"vlan {v}", f"name vlan{v}"])
        # Configure the access ports
        vlans = [[ "0/2-0/6", "vlan 2"], ["0/7-0/12", "vlan 3"]]
        for i in vlans:
            conf_int = [f"int range fa {i[0]}",
                        "switchport mode access",
                        f"switchport access {i[1]}"]
            device.send_config_set(conf_int)
        # Configure the trunk port:
        device.send_config_set(["int fa 0/1", "switchport mode trunk"])
        # show vlan brief
        vlan_brief = device.send_command("show vlan brief")
        print(vlan_brief)
    except Exception as e:
        print(e)
    finally:
        device.disconnect()
