import os
import shutil
from tqdm import tqdm

if not os.path.exists("stock-data"):
    os.makedirs("stock-data")

listdir = os.listdir("crawl-data")

# print(listdir[:10])

for file in tqdm(listdir):
    year = file[:4]
    src = os.path.join("crawl-data", file)
    dst = os.path.join("stock-data", year, file)
    shutil.copytree(src, dst)