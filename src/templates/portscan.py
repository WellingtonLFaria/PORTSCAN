import socket
import os

def portscan(enderecoip="192.168.042"):
	""" PORTSCAN
	enderecoip: Ex > 192.168.042
	"""
	PORTASREL = [80, 443, 3306, 8080, 5000]
	portasabertas = {}
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(2)
	for c in range(1,256):
		portasabertas[f"{enderecoip}.{str(c)}"] = []
		print(f"IP: {enderecoip}.{str(c)}")
		for porta in PORTASREL:
			res = sock.connect_ex((f"{enderecoip}.{str(c)}", porta))
			print(f"PORTA:{porta}	STATUS:{res}")
			if res == 0:
				portasabertas[f"{enderecoip}.{str(c)}"].append(f"{porta}:OPEN")
			else:
				portasabertas[f"{enderecoip}.{str(c)}"].append(f"{porta}:CLOSED")
	return portasabertas
