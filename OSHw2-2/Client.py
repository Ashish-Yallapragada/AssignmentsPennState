import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        input_str = input("Enter a pair of (x,y) integers and an operator (add, subtract, multiply, divide), or type 'change' to enter new x and y: ")
        inputs = input_str.split()
        if len(inputs) == 3:
            try:
                x = int(inputs[0])
                y = int(inputs[1])
                op = inputs[2]
            except ValueError:
                print("Invalid input")
                continue
            message = f"{x} {y} {op}"
            s.sendall(message.encode())
            data = s.recv(1024)
            print(data.decode())
        elif input_str == "change":
            x = input("Enter new x: ")
            y = input("Enter new y: ")
        else:
            print("Invalid input")
