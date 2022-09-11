import bs4
import requests

res = requests.get('https://hardverapro.hu/aprok/keres.php?stext=herman+miller&stcid_text=&stcid=&stmid_text=&stmid'
                   '=&minprice=&maxprice=&cmpid_text=&cmpid=&usrid_text=&usrid=&__buying=0&__buying=1&stext_none=')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
cities = soup.select('div.media-body > div.uad-info > div.uad-light')
for i in cities:
    print(i.text)
