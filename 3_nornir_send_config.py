from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_netmiko.tasks import netmiko_send_config
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
import time


nr = InitNornir(config_file="config.yaml")

def nornir_send_config(config):
	print("###########SENDING CONFIGURATION COMMANDS##########")
	time.sleep(3)
	results = nr.run(task=netmiko_send_config, config_commands=config)
		
	print_result(results)
	time.sleep(10)

commands = ["router ospf 1", "router-id 192.168.164.137", "network 0.0.0.0 0.0.0.0 area 0"]

nornir_send_config(commands)
