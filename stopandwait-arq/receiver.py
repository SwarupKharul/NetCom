import socket
import threading
import time

s = socket.socket()
print("Code by Swarup Kharul - 20BCT0073\n")
port = 4000
s.connect(("127.0.0.1", port))
numberOfFrames = int(s.recv(2).decode())
frames = []
for i in range(numberOfFrames):
    frames.append(i % 2)
acknowledgement = -1


def send():
    global acknowledgement
    s.send(str(acknowledgement).encode())


idx = 0
flag = 0
flag2 = 1
while True:
    msg = s.recv(1).decode()
    print("Received " + msg + " frame with value " + str(idx + 1))
    if int(msg) == frames[idx]:
        print("frame accepted")
        acknowledgement = (int(msg) + 1) % 2
        idx += 1
    else:
        print("frame discarded")
    if idx == numberOfFrames:
        print("sending closing acknowledgement")
        s.send("c".encode())
        break
    print("sending acknowledgement for " + str(acknowledgement) + " frame")
    send_thread = threading.Thread(target=send)
    send_thread.start()
    time.sleep(0.2)
print("Done")
time.sleep(1)
s.close()
