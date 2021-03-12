
import requests
from  bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
#  strochka maskirujushaja nas kak budto my zahodim cherez browser dlja obhoda blokirovki
r=requests.get('https://www.gammatest.net/course/python/', timeout=5)
soup=BS(r.content, 'html.parser')
# print(soup.title.text)
# print(soup.h2.text)
# print(soup.title)


# match=soup.find('div',class_="col-md-12 col-sm-12")
# match = soup.find_all('div',class_="col-md-12 col-sm-12")
# print(match[0])#mozhem indeksirovat
# print(len(match))#mozhem uznat skolko nashel
# for item in match:
#     print(item.a.text)
#
# match2 =soup.findALL('div',class_="col-md-12 col-sm-12")

# r=requests.get('https://xkcd.com/353/', timeout=5, headers=headers)
r=requests.get('https://imgs.xkcd.com/comics/python.png', timeout=5)
with open('python.png', 'wb') as file:#wb write
    file.write(r.content)
# print(r)
# print(r.status_code)# poluchaem status code
# print(r.text)# poluchim html code stranici
# print(r.content)# tozhe samoe chto i text tolko kompaktnee
# print(dir(r))
# print(r.headers)
# 200 success
# 300 redirect
#400 client error
# 500 server

<div jsname="oQYOj" class="EikfZ IFC-animate"