# -*- coding: utf8 -*-
from socket import *

def main_handler(event, context):
	IP=event["queryString"]["ip"]
	port=event["queryString"]["port"]
	try:
		conn=socket(AF_INET,SOCK_STREAM)
		res=conn.connect_ex((str(IP),int(port)))
		conn.send('Hello,World!'.encode("utf8"))
		results=conn.recv(25)
		if res==0:
			conn.close()
			return port
	except Exception as err:
		print(err)
	finally:
		print("")
		conn.close()
	
	return None