class PayloadInjector:


    def __init__(self):
        return


    def inject(self, str_response):
        file_name = "./payload.js"
        file_itself = open(file_name, "r")
        payload = file_itself.read()
        str_response += payload
        return str_response
