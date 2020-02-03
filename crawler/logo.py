from bs4 import BeautifulSoup
import ssl
import urllib.request
from crawler.utils import headers, get_cleaned_text

pages = [
    'https://www.chemknock.com/view.do?no=137&pageIndex=1&sw=&pgMode=list&pageUnit=100&dvsn=cp&srcTob=&idx=&srchLctnSido=&srchLctnSigungu=',
    'https://www.chemknock.com/view.do?no=137&pageIndex=2&sw=&pgMode=list&pageUnit=100&dvsn=cp&srcTob=&idx=&srchLctnSido=&srchLctnSigungu=',
    'https://www.chemknock.com/view.do?no=137&pageIndex=3&sw=&pgMode=list&pageUnit=100&dvsn=cp&srcTob=&idx=&srchLctnSido=&srchLctnSigungu=',
    'https://www.chemknock.com/view.do?no=137&pageIndex=4&sw=&pgMode=list&pageUnit=100&dvsn=cp&srcTob=&idx=&srchLctnSido=&srchLctnSigungu=',
    'https://www.chemknock.com/view.do?no=137&pageIndex=5&sw=&pgMode=list&pageUnit=100&dvsn=cp&srcTob=&idx=&srchLctnSido=&srchLctnSigungu=',
    'https://www.chemknock.com/view.do?no=137&pageIndex=6&sw=&pgMode=list&pageUnit=100&dvsn=cp&srcTob=&idx=&srchLctnSido=&srchLctnSigungu=',
    'https://www.chemknock.com/view.do?no=137&pageIndex=7&sw=&pgMode=list&pageUnit=100&dvsn=cp&srcTob=&idx=&srchLctnSido=&srchLctnSigungu=',
]
site_url = 'https://www.chemknock.com'
for page in pages:
    print(page)
    request = urllib.request.Request(page, headers=headers)
    html_data = urllib.request.urlopen(request, context=ssl._create_unverified_context()).read()
    parsed_html = BeautifulSoup(html_data, 'html.parser')
    corps = parsed_html.findAll('div', {'class':'box_info cp'})
    for corp in corps:
        try:
            img_url = site_url + corp.find('img')['src']
            img_name = get_cleaned_text(corp.select_one('.title').get_text())
            print(img_name)
            img_req = urllib.request.urlretrieve(img_url, './logo_images/'+img_name+'.png')
        except:
            pass
