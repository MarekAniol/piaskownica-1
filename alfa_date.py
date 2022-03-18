from alfa_list import separate_data

# Program which sort 1st column in a list called (Date)
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
result = only_date(date_list)
print(result)
# print(clean_date)
# clean_date = only_date(date_list)
# print(clean_date)

