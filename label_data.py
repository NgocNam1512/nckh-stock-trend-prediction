import pandas as pd
import os
import shutil
import datetime

price_path = 'crawl-data/vnindex/price-datafull.csv'
data_folder = 'data'

price_path = 'crawl-data/vnindex/price-datafull.csv'
df = pd.read_csv(price_path)


for file_name in os.listdir(data_folder):
    name = file_name

    # get info from name
    year = name[:4]
    month = name[4:6]
    day = name[6:8]

    date_news = datetime.datetime(int(year), int(month), int(day))
    date_price = date_news + datetime.timedelta(days=1)
    date_price_str = date_price.strftime("%d/%m/%Y")
    # print(date_price_str)

    price = df[df['date']==date_price_str].change.tolist()
    if len(price) > 0:
        price = float(price[0].replace("%", ""))

        src = os.path.join(data_folder, file_name)
        dst = ""
        if price > 0:
            dst = "labeled-data/" + file_name.replace(".txt", "_0.txt")
        elif price < 0:
            dst = "labeled-data/" + file_name.replace(".txt", "_1.txt")
        else:
            dst = "labeled-data/" + file_name.replace(".txt", "_2.txt")
            print(dst)

        shutil.copy(src, dst)
            

    else:
        continue