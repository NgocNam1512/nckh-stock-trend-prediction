from bs4 import BeautifulSoup
import requests
from utils import pdate2date

URLpage = "https://cafef.vn/duc-long-gia-lai-dlg-nam-2020-bao-lo-lon-894-ty-dong-20210203162100299.chn"
article = requests.get(URLpage)
soup2 = BeautifulSoup(article.content, 'html.parser')

data = soup2.findAll("span", {"class":"pdate"})[0]
date = pdate2date(data.text)
print(date)

sumary = soup2.findAll("h2", {"class":"sapo"})[0]
print(sumary.text.strip())

results2 = soup2.find(id="mainContent")
all_p = results2.findAll('p')
main_content = ""
for p in all_p:
    main_content += p.text
# print(main_content + "\n----------------------------------------")


