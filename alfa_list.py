import requests 

url = 'http://www.po-prostu-adam.pl/alfa'
def get_alfa_list(url):
    raw_info = requests.get(url)
    text = raw_info.text
    return text

def separate_data(url):
    '''
    Show every separate data from text in list
    '''
    text_from_site = get_alfa_list(url)
    list_of_datas = text_from_site.split(',')
    
    return list_of_datas
        
        
        
print(separate_data(url))