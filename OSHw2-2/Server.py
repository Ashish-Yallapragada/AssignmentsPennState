import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                x, y, op = data.decode().split()
                x = int(x)
                y = int(y)
                result = None
                if op == "add":
                    result = x + y
                elif op == "subtract":
                    result = x - y
                elif op == "multiply":
                    result = x * y
                elif op == "divide":
                    result = x / y
                else:
                    conn.sendall(b"Invalid operator")
                    continue
                conn.sendall(str(result).encode())
