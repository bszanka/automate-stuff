import requests, bs4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import openpyxl, os

# driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
#
# driver.get('https://hardverapro.hu/index.html')
#
# searchBar = driver.find_element(By.CSS_SELECTOR, '#top > div.search-bar.search-bar-ha > div.search-bar-search > div > '
#                                                  'form > div.form-group.mb-0.d-flex.justify-content-center.flex-wrap '
#                                                  '> div > input')
# searchBar.send_keys('herman miller')
# searchBar.submit()
#
# cities = driver.find_elements(By.CSS_SELECTOR, 'div.media-body > div.uad-info > div.uad-light')
# for i in cities:
#     print(i.text)
#
# time.sleep(10)  # Let the user actually see something!
#
# driver.quit()

# res = requests.get('https://hardverapro.hu/aprok/keres.php?stext=herman+miller&stcid_text=&stcid=&stmid_text=&stmid'
#                    '=&minprice=&maxprice=&cmpid_text=&cmpid=&usrid_text=&usrid=&__buying=0&__buying=1&stext_none=')
#
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
#
# cities = soup.select('div.media-body > div.uad-info > div.uad-light')
# for i in cities:
#     print(i.text)

workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook['Sheet1']
# cell = sheet['A1']
print(sheet['A1'].value)
print(sheet.cell(row=1, column=1).value)

# searchTerm = ''
# while searchTerm != '0':
#     if searchTerm != '':
#         print(sheet[searchTerm].value)
#     searchTerm = input()

