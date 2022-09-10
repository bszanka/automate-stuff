import requests, bs4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get('http://www.google.com/');

time.sleep(3) # Let the user actually see something!

driver.quit()

res = requests.get('https://hardverapro.hu/aprok/keres.php?stext=herman+miller&stcid_text=&stcid=&stmid_text=&stmid'
                   '=&minprice=&maxprice=&cmpid_text=&cmpid=&usrid_text=&usrid=&__buying=0&__buying=1&stext_none=')

soup = bs4.BeautifulSoup(res.text, 'html.parser')

cities = soup.select('div.media-body > div.uad-info > div.uad-light')
for i in cities:
    print(i.text)
