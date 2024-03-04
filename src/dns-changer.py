import os
from time import sleep
import msvcrt 


def change_dns(primary:str=None,secondary:str=None,clear=False):
	try:
		if clear:
			os.system('netsh interface ip set dnsservers "Ethernet" dhcp')
			os.system('netsh interface ip set dnsservers "Wi-Fi" dhcp')
		else:
			os.system(f'netsh interface ip set dnsservers "Ethernet" static {primary} primary')
			os.system(f'netsh interface ip set dnsservers "Wi-Fi" static {primary} primary')
			if secondary:
				os.system(f'netsh interface ip add dnsservers "Ethernet" {secondary} index=2')
				os.system(f'netsh interface ip add dnsservers "Wi-Fi" {secondary} index=2')
				sleep(1.5)	
			print("DNS changed successfully")


	except Exception as e:
		raise "Error couldn't change the dns server"

def show_dns():
	print("="*60)
	print("Ethernet DNS is :")
	os.system('netsh interface ip show dnsservers "Ethernet"')
	print("="*60)
	print("Wi-Fi DNS is :")
	os.system('netsh interface ip show dnsservers "Wi-Fi"')
	print("="*60)

def clear_terminal():
	print("\n"*400)


dns_list = [
("185.55.225.25","185.55.226.26",False),
("10.202.10.10" , "10.202.10.11",False),
("178.22.122.100","185.51.200.2",False),
("78.157.42.100","78.157.42.101",False),

("172.29.0.100","172.29.2.100",False),
("85.15.1.14","85.15.1.15",False),
("10.202.10.202","10.202.10.102",False),
("10.202.10.202","10.202.10.102",False),

("8.26.56.10","8.20.247.10",False),
("8.8.8.8","8.8.4.4",False),
("77.88.8.1","77.88.8.8",False),
("4.2.2.4","5.200.200.200",False),

("9.9.9.9","149.112.112.112",False),
("81.218.119.11","209.88.198.133",False),
("208.67.222.222","208.67.220.220",False),
("1.1.1.1","1.0.0.1",False),

("","",True),
]


# for i,v in enumerate(dns_list):
# 	print("index :",i)
# 	print("value :",v)

while True:
	show_dns()

	print("""
	-------------------------------------------------------------------
	|\tWelcome to Python Dns changer 				  |
	-------------------------------------------------------------------
	|0.bogzar\t4.host iran\t8.comodo\t12.Quad9\t  |
	|1.radar\t5.shuttel\t9.Google\t13.GreenTeam\t  |
	|2.shecan\t6.403\t\t10.yandex\t14.OpenDNS\t  |
	|3.electro\t7.online\t11.mokhaberat\t15.Cloudflare\t  |
	-------------------------------------------------------------------
	|16.No Dns							  |
	|17.Custom							  |
	-------------------------------------------------------------------
	Enter your desiered dns:

	""")


	try:
		dns_type = int(input("Desiered dns type:"))


		if dns_type == 17 :
			dns_1 = input("Enter the primary dns: ")
			dns_2 = input("Enter the secondary dns: ")
			change_dns(dns_1,dns_2)
		else:
			primary,secondary,clear = dns_list[dns_type]
			change_dns(primary,secondary,clear)

		print("Dns is changed , current config is:")
		show_dns()

		print("Are you done changing dns?(y,n):")
		quit = msvcrt.getch()
		quit = quit.decode('utf-8')

		if quit.upper() == "Y":
			print("have a nice day!")
			sleep(3)
			break
		else:
			clear_terminal()

	except Exception as e:
		print(f"failed during dns changing process , error code :{e.args}")
		break