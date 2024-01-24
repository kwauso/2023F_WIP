import socket
import sys

#server: python s hostname.local port_number extension
#clienr: python c hostname.local port_number extension

def server(hostname, port, extention):
    ip = socket.gethostbyname(str(hostname))
    output_list = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
                filename = extention
                with open(filename, mode="ab") as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                        conn.sendall(b'Received done')
                    exit()

def client(hostname, port, filename):
    ip = socket.gethostbyname(str(hostname))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        try:
            with open(filename, mode='rb') as f:
                for line in f:
                    s.sendall(line)
                    data = s.recv(1024)
                print(repr(data.decode()))
        except:
            pass

if __name__ == "__main__":
    if (sys.argv[1] == "s"):
        server((sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    if (sys.argv[1] == "c"):
        client((sys.argv[2]), int(sys.argv[3]), sys.argv[4])
