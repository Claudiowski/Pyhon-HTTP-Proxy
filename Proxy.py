import socket
from _thread import *
from RequestParser import *
from CheckKeyWords import *
from UserErrorLogger import *
from PayloadInjector import *


class Proxy:
    """ The proxy itself """

    def __init__(self):
        self.port = 15000

        #Reception socket
        self.recept_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_list = []

        #Parses the packets
        self.request_parser = RequestParser()

        #Validate the packet
        self.word_checker = CheckKeyWords()

        #Logs the client forbidden requests
        self.user_error_logger = UserErrorLogger()

        self.payload_injector = PayloadInjector()


    def run(self):
        """ Runs the proxy's basis """

        # Initiate the main socket
        self.recept_socket.bind(("0.0.0.0", self.port))
        self.recept_socket.listen(8)

        print("Proxy server started on port " + str(self.port))

        # Loops on the socket, build new thread for each new connection
        while True:
            sockhttp, addr = self.recept_socket.accept()
            new_conn = start_new_thread(self.exchange, (sockhttp, addr))
            self.connection_list.append(new_conn)


    def exchange(self, sock, addr):
        """ Manages the exchanges between the client and the server """

        sock_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Receive and depackages the HTTP packet coming from the client
        packet = sock.recv(4096)
        url = self.request_parser.get_url(packet)
        dn = self.request_parser.get_dn(url)
        ip = socket.gethostbyname(dn)

        if self.word_checker.validate_url(url):
            sock_to_serv.connect((ip, 80))
            sock_to_serv.send(packet)
            response = sock_to_serv.recv(4096)

        else:
            self.user_error_logger.log(url, addr)
            response = HttpResponse()

        manipulated = str(response)
        true_response = self.payload_injector.inject(manipulated).encode()

        sock.send(true_response)

        sock_to_serv.close()
        sock.close()
