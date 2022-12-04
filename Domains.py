import requests
import asyncio


class Domens:

    async def check_domens(ras):
        for ele in ras:
            try:
                response = await requests.get('http://' + ele)
                if response.status_code == 200:
                    print(ele)
            except:
                pass

    def geting_domens_from_file():
        file = open('d1', 'r').readlines()
        ras = []
        for line in file:
            ras.append(line.strip())
        return ras

    asyncio.run(check_domens(geting_domens_from_file()))
