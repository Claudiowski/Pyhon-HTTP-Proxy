import os, sys


class RequestParser:


    def __init__(self):
        return


    def get_url(self, paquet):
        paquet = str(paquet)
        return paquet.split('\n')[0]


    def get_dn(self, url):
        print(url)
        return url.split('/')[2]
