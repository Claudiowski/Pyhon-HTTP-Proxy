from datetime import *


class UserErrorLogger:


    def __init__(self):
        return


    def log(self, url, addr):
        date = str(datetime.now())
        self.file_log = open("./proxy-logs.txt", "a+")
        self.file_log.write("User " + addr[0] + " refused at " + date + ". Url = " + url + "\n")
        self.file_log.close()
