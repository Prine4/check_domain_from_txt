import requests


class Domens:

    def check_domens(ras):
        file = open('output.csv', 'x')
        for ele in ras:
            try:
                response = requests.get('http://' + ele)
                if response.status_code == 200:
                    file.write(ele + ',')
                    print(ele)
            except OSError:
                pass

    def geting_domens_from_file():
        print('Tape name of the file with domains:')
        name_of_file = input()
        file = open(name_of_file, 'r').readlines()
        ras = []
        for line in file:
            ras.append(line.strip())
        return ras

    check_domens(geting_domens_from_file())
