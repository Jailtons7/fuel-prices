from urllib import request


class DadosGov:
    URL = ''

    def get_data(self):
        req = request.urlopen(self.URL)

