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
    # date = "/".join([day, month, year])

    date 


    price = df[df['date']==date].change.tolist()
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

        # shutil.copy(src, dst)
            print(dst)

    else:
        continue
        
