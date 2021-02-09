import os
import shutil
from tqdm import tqdm

if not os.path.exists("vietstock-sorted-data"):
    os.makedirs("vietstock-sorted-data")

listdir = os.listdir("vietstock-data")

# print(listdir[:10])

for file in tqdm(listdir):
    year = file[:4]
    src = os.path.join("vietstock-data", file)
    dst = os.path.join("vietstock-sorted-data", year, file)
    shutil.copytree(src, dst)