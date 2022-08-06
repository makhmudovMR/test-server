import socket
import os
import time


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen()

def child_process():
  print('childprocess')
  time.sleep(10)

  client_sock.sendall(str.encode("HTTP/1.0 200 OK\n",'iso-8859-1'))
  client_sock.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
  client_sock.sendall(str.encode('\r\n'))
  client_sock.sendall(str.encode('Hello it\'s Makhmudov Server'))


  client_sock.close()
  print('close client')
  if not pid:
    os._exit(0)



while True:
  client_sock, client_addr = server_socket.accept()
  pid = os.fork()
  if pid:
    client_sock.close()
    continue
  else:
    child_process()

