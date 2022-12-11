import requests


class Domens:

    def check_domens(ras):
        for ele in ras:
            try:
                response = requests.get('http://' + ele)
                if response.status_code == 200:
                    print(ele)
            except OSError:
                pass

    def geting_domens_from_file():
        file = open('d1', 'r').readlines()
        ras = []
        for line in file:
            ras.append(line.strip())
        return ras

    check_domens(geting_domens_from_file())
