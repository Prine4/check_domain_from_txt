import grequests
import asyncio


async def check_domens(urls: list):
    list_of_responses = []

    response = [grequests.get("http://" + url, timeout=60) for url in urls]

    for r in grequests.map(response):
        if r is not None:
            list_of_responses.append(f"{r.status_code};{r.url}\n")
        else:
            list_of_responses.append(str(r) + '\n')

    return list_of_responses


def geting_domens_from_file():
    file_name = 'Data_to_check'
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]


def save_checked_domens(list_of_responses):
    with open('output.csv', 'x') as file:
        [file.write(i) for i in list_of_responses]


if __name__ == '__main__':
    domens = geting_domens_from_file()

    event_loop = asyncio.get_event_loop()
    res = event_loop.run_until_complete(check_domens(domens))
    save_checked_domens(res)
