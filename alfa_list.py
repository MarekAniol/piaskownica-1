import requests

def get_alfa_list(url):
    raw_info = requests.get(url)
    text = raw_info.text
    return text


def separate_data(url):
    text_from_site = get_alfa_list(url)
    list_of_datas = text_from_site.split("</p>")[0].split("<p>")[-1]
    list_of_datas = list_of_datas.strip()
    list_of_datas = list_of_datas.split(",")
    return list_of_datas


def only_date(date_list):
    lst = [l.split("\n") if "\n" in l else l for l in date_list]
    separate_datas = []
    for el in lst:
        if len(el) == 2:
            for e in el:
                separate_datas.append(e)
        else:
            separate_datas.append(el)
    result = [separate_datas[i:i + 13] for i in range(0, len(separate_datas), 13)]
    return result

url = 'http://www.po-prostu-adam.pl/alfa'
date_list = separate_data(url)
final_data = only_date(date_list)