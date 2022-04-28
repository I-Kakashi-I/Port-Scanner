import pyfiglet

check = {}
result = pyfiglet.figlet_format("Port Scanner", font = "slant")
print(termcolor.colored(result,'blue'))

def scan(target, ports):
	print('\n' + termcolor.colored('Starting Scan For ' + str(target),'cyan'))
	check.update({target: False})
	for port in range(1,ports):
		scan_port(target,port)
	if not check[target]:
		print(termcolor.colored("No open ports in this range",'red'))
def scan_port(target, port):
	try:
		sock = socket.socket()
		sock.connect((target, port))
		check.update({target: True})
		print(termcolor.colored("[+] Port Opened " + str(port), 'green'))
		sock.close()
	except:
		pass

targets = input("[*] Enter Targets To Scan(split them by -): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if '-' in targets:
	print(termcolor.colored("[*] Scanning Multiple Targets", 'cyan'))
	for ip_addr in targets.split('-'):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
