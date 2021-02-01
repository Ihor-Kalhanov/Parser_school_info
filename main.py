from bs4 import BeautifulSoup
import requests
import csv
import time
start_time = time.time()





URL_TABLE = 'https://if.isuo.org/authorities/schools-list/id/626 '
URL_PAGE = 'https://if.isuo.org/'

HEAD = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', 'accept': '*/*'}

PATH = 'school.csv'

def get_table(url, params = None):
    r = requests.get(url, headers=HEAD, params=params)
    return r
def get_head(url, params = None):
    str(url)
    r = requests.get(url, headers=HEAD, params=params)
    page = BeautifulSoup(r.content, 'html.parser')
    cll = page.select('odd')
    items = page.find_all('tr', cll)
    head_full = []

    for item in items:
        cll = page.select('odd')
        head_full.append(
            (item.find('td')).get_text()
        )

    if url == str('https://if.isuo.org/schools/view/id/10680'):
        head = [head_full[18]]
        return str(head)
    elif url == 'https://if.isuo.org/schools/view/id/10661':
        head = [head_full[20]]
        return str(head)
    elif url == 'https://if.isuo.org/schools/view/id/10669':
        head = [head_full[18]]
        return str(head)
    elif url == 'https://if.isuo.org/schools/view/id/11737':
        head = [head_full[18]]
        return str(head)
    elif url == 'https://if.isuo.org/schools/view/id/10708':
        head = [head_full[20]]
        return str(head)
    elif url == 'https://if.isuo.org/schools/view/id/10667':
        head = [head_full[20]]
        return str(head)
    elif url == 'https://if.isuo.org/schools/view/id/10711':
        head = [head_full[20]]
        return str(head)
    elif url == 'https://if.isuo.org/schools/view/id/10699':
        head = [head_full[20]]
        return str(head)
    elif url == 'https://if.isuo.org/schools/view/id/10679':
        head = [head_full[20]]
        return str(head)
    else:
        head = [head_full[19]]
        return str(head)

def get_phone_number(url, params = None):
    str(url)
    r = requests.get(url, headers=HEAD, params=params)
    page = BeautifulSoup(r.content, 'html.parser')
    cll = page.select('odd')
    items = page.find_all('tr', cll)
    phone_num_full = []

    for item in items:
        cll = page.select('odd')
        phone_num_full.append(
            (item.find('td')).get_text()
        )
    if url =='https://if.isuo.org/schools/view/id/10680' or url =='https://if.isuo.org/schools/view/id/10669' or url =='https://if.isuo.org/schools/view/id/10669' or url =='https://if.isuo.org/schools/view/id/11737'  or url =='https://if.isuo.org/schools/view/id/10698' or url =='https://if.isuo.org/schools/view/id/10706':
        num = [phone_num_full[11]]
        return str(num)
    elif url =='https://if.isuo.org/schools/view/id/10661' or url =='https://if.isuo.org/schools/view/id/10708' or url =='https://if.isuo.org/schools/view/id/10708' or url =='https://if.isuo.org/schools/view/id/10667' or url =='https://if.isuo.org/schools/view/id/10711' or url =='https://if.isuo.org/schools/view/id/10699' or url =='https://if.isuo.org/schools/view/id/10679' :
        num = [phone_num_full[13]]
        return str(num)

    else:
        num = [phone_num_full[12]]
        return str(num)







def get_content(table):
    soup = BeautifulSoup(table, 'html.parser')
    cll = soup.select('odd')
    items = soup.find_all('tr', cll)
    school = []
    for item in items:
        href = (item.find_all('a'))#.get('href')
        for item in href:

            href = ('https://if.isuo.org'+ item.get('href'))
            name = ' '.join( item.text.split('\n')).strip()

            get_phone_number(href)

            school.append({
                'href':href,
                'name_of_school':(name),
                'head': get_head(href),
                'phone': get_phone_number(href)
            })

    return (school)





def save_csv(items, path):
    with open(path, 'w', newline='') as file:
        write = csv.writer(file, delimiter=';')
        write.writerow(['Name', 'Link', 'Head', 'Phone' ])
        for i in items:
            write.writerow([i['name_of_school'], i['href'], i['head'], i['phone']])


def parse():
    print('Start parcing')
    html = get_table(URL_TABLE)
    school = get_content(html.text)
    save_csv(school, PATH)

    print("""Parce end
 --- %s seconds ---
    """% (time.time() - start_time))



parse()
