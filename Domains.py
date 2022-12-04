import requests


class domens:

    async def check_domens(ras):
        for ele in ras:
            try:
                response = await requests.get('http://' + ele)
                if response.status_code == 200:
                    print(ele)
            except:
                pass

    def geting_domens_from_file():
        file = open('domenki.txt', 'r').readlines()
        ras = []
        for line in file:
            ras.append(line.strip())
        return ras

    await check_domens(geting_domens_from_file())
