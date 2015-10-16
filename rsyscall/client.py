import socket
import sys
import pickle

MAX_BUFFER = 2048

def conn_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        return sock
    except Exception as ex:
        print("Error connect: {}".format(ex))


def main(argv):
    conn = None
    if len(argv) != 3:
        print("Error.... Usage Ex: python cliente.py localhost 8003")
        exit(1)
    host = argv[1]
    port = int(argv[2])
    try:
          conn = conn_server(host, port)
    except Exception as ex:
        print("Error: {}".format(ex))

    if conn:
        while True:
            my_msg = raw_input("# ")
            if my_msg and my_msg != 'exit':
                comm = my_msg.split()
                conn.send(pickle.dumps(comm))
                data_rcv = conn.recv(MAX_BUFFER)
                if data_rcv:
                    print(data_rcv.decode('utf-8'))
            else:
                sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
