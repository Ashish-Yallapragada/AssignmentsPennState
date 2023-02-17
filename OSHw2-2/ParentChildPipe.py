import os
from multiprocessing import Pipe, Process

def parent(conn):
    message = "COMP 512 pipe programming parent"
    try:
        conn.send(message.encode())
    except OSError:
        print("Parent pipe is closed!")
    conn.close()
    print("Parent sent message to child:", message)
    try:
        response = conn.recv()
    except OSError:
        print("Parent pipe is closed!")
    else:
        print("Parent received message from child:", response.decode())

def child(conn):
    try:
        message = conn.recv().decode()
    except OSError:
        print("Child pipe is closed!")
    else:       
        message = message.upper()        
        message += " CHILD"
        try:
            conn.send(message.encode())
        except OSError:
            print("Child pipe is closed!")
        conn.close()
        print("Child sent message to parent:", message)

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    parent_process = Process(target=parent, args=(parent_conn,))
    child_process = Process(target=child, args=(child_conn,))
    parent_process.start()
    child_process.start()
    parent_process.join()
    child_process.join()
