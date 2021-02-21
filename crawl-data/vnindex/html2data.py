#!/usr/bin/python

from bs4 import BeautifulSoup
import pandas as pd

with open('datafull.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    resultSet = soup.findAll("table", {"class":"genTbl closedTbl historicalTbl"})
    table = resultSet[0]

    # for i in resultSet:
    #     print(i)
    # print(table.tbody)
    print("date,price_open,price_close,high,low,vol,change")
    rows = table.tbody.findAll('tr')
    for row in rows:
        cols = row.findAll('td')
        date = cols[0].text
        price_close = cols[1].text.replace(",","")
        price_open = cols[2].text.replace(",","")
        high = cols[3].text.replace(",","")
        low = cols[4].text.replace(",","")
        vol = cols[5].text
        change = cols[6].text
        print(date, price_open, price_close, high, low, vol, change, sep=",")