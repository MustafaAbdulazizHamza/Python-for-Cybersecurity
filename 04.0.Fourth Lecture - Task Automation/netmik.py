from netmiko import ConnectHandler

device = ConnectHandler(host="IP", username='user', password = 'pass', device_type="cisco_ios", secret="enable_pass")

out = device.send_command("show whatever")
print(out)
# en
# conf t
device.send_config_set([])

device.send_config_from_file("path")

device.establish_connection()

device.disconnect()

device.open_session_log("path")