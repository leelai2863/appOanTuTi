import socket, cv2, pickle, struct, time, math
import threading, imutils
import pyshine as ps # pip install pyshine
import cv2
from predict import match_rersult

server_status = ''
def start_server():
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	# server_socket.settimeout(5)
	host_ip = "26.232.164.220"
	print('HOST IP:',host_ip)
	port = 9999
	socket_address = (host_ip, port)
	server_socket.bind(socket_address)
	server_socket.listen(2)
	client = []
	while True:
		client_socket, addr = server_socket.accept()
		thread = threading.Thread(target=handle_client, args=(addr, client_socket, client))
		thread.start()
		print("TOTAL CLIENTS ",threading.active_count() - 1, "\n")

def handle_client(address, client_socket, client):
    global stop_event
    if not client:
        client.append(client_socket)
    else:
        client.append(client_socket)
        show_client(address, client[0], client)

def send_frame(frame, client_socket):
    frame = imutils.resize(frame,width=380)
    a = pickle.dumps(frame)
    message = struct.pack("Q",len(a))+a
    client_socket.sendall(message)

def show_client(addr, client_socket, client):
	start_time = time.time()
	server_frame = None
	client_frame = None
	try:
		vid = cv2.VideoCapture(r"c:\Users\Le Minh Tri\Videos\keobuabao.mp4", cv2.CAP_FFMPEG)
		if client_socket: # if a client socket exists
			data = b""
			payload_size = struct.calcsize("Q")
			while True:
				img, server_frame = vid.read()
				send_frame(server_frame, client_socket)
				while len(data) < payload_size:
					packet = client_socket.recv(4*1024) # 4K
					if not packet: break
					data+=packet
				packed_msg_size = data[:payload_size]
				data = data[payload_size:]
				msg_size = struct.unpack("Q",packed_msg_size)[0]
				
				while len(data) < msg_size:
					data += client_socket.recv(4*1024)
				frame_data = data[:msg_size]
				data  = data[msg_size:]
				client_frame = pickle.loads(frame_data)
				client_frame = cv2.resize(client_frame, (640, 480))
				second = math.floor(time.time() - start_time)
				text = f"{3 - second}"
				cv2.imshow(f"FROM {addr}",client_frame)
				key = cv2.waitKey(1) & 0xFF
				if key == ord('q'):
					break
	except Exception as e:
		pass
	finally:
		result1, result2 = match_rersult(server_frame, client_frame)
		print(result1)
		print(result2)
		client[1].send(result2.encode())
		client_socket.close()

def connect_to_opponent(client_socket, result_socket):
	vid = cv2.VideoCapture(r"c:\Users\Le Minh Tri\Videos\keobuabao.mp4", cv2.CAP_FFMPEG)
	if client_socket:
		final_frame = ''
		while (vid.isOpened()):
			try:
				img, server_frame = vid.read()
				send_frame(server_frame, client_socket)
				data = b""
				payload_size = struct.calcsize("Q")
				while len(data) < payload_size:
						packet = client_socket.recv(4*1024) # 4K
						if not packet: break
						data+=packet
				packed_msg_size = data[:payload_size]
				data = data[payload_size:]
				msg_size = struct.unpack("Q",packed_msg_size)[0]
				
				while len(data) < msg_size:
					data += client_socket.recv(4*1024)
				frame_data = data[:msg_size]
				data  = data[msg_size:]
				frame = pickle.loads(frame_data)
				frame = cv2.resize(frame, (640, 480))
				cv2.imshow("yeet", frame)
				key = cv2.waitKey(1) & 0xFF
				if key == ord("q"):
					break
			except Exception as e:
				print('VIDEO FINISHED!')
				print(e)
				cv2.destroyAllWindows()
				break
		client_socket.close()

		message = result_socket.recv(4096).decode()
		print(message)
		result_socket.close()
		

def find_match():
	global server_status
	try:
		client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		port = 9999
		client_socket.connect(("26.217.160.37",port))
		result_socket.connect(("26.217.160.37",port))
		return connect_to_opponent(client_socket, result_socket)
	except:
		start_server()
		print(server_status)

if __name__ == "__main__":
	find_match()