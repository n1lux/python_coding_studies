import sys
import socket
import threading
import subprocess
import pickle


class RsysSever:
    MAX_BUFFER = 1024

    def __init__(self, h_server="localhost", p_server=8023):
        self.host = h_server
        self.port = p_server
        self.sock = None

    def crate_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(10)

    def run(self):
        print("Server wait for connections....")
        while True:
            try:
                (c_conn, c_address) = self.sock.accept()
                if c_conn and c_address:
                    print("[{}] connected".format(c_address))
                    threading.Thread(target=self.comm, args=(c_conn,)).start()
            except Exception as ex:
                print("Error: {}".format(ex))

    def comm(self, fd_conn):
        while True:
            data = fd_conn.recv(RsysSever.MAX_BUFFER)
            if data:
                cmd = ['/bin/sh', '-c'] + list(pickle.loads(data))
                try:
                    # r_command = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
                    r_command = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
                    ret = r_command
                except subprocess.CalledProcessError as ex:
                    ret = str(ex)
                finally:
                    fd_conn.send(ret)


def main():
    server = RsysSever()
    server.crate_server()
    server.run()


if __name__ == "__main__":
    main()
