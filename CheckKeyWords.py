class CheckKeyWords:


    def __init__(self):
        self.wordlist = self.get_key_words()


    def get_key_words(self):
        wordlist = []
        with open("./forbidden_words.txt", "r") as fichier:
            content = fichier.read()
            return content.split("\n")[:-1]


    def validate_url(self, url):
        for w in self.wordlist:
            if w in url:
                return False
        return True
