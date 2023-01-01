import requests
import asyncio


async def check_domens(ras):
    list_of_responses = []

    for ele in ras:
        try:
            response = requests.get('http://' + ele, timeout=4)
            response_str = str(response)
            list_of_responses.append(response_str + ';' + ele)
        except:
            pass
    return list_of_responses


async def geting_domens_from_file():
    name_of_file = 'test.txt'
    file = open(name_of_file, 'r').readlines()
    ras = []
    for line in file:
        ras.append(line.strip())

    res = await check_domens(ras)
    return res

    # def file(list_of_responses):
    #     file = open('output.csv', 'x')
    #     file.write(list_of_responses)
    #     file.close

loop = asyncio.get_event_loop()
res = loop.run_until_complete(geting_domens_from_file())
print(res)
