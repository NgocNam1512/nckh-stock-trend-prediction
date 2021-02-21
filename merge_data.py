import os
import shutil
from tqdm import tqdm

merge_folder = 'merged-data'
for year in tqdm(os.listdir(merge_folder)):
    for file_name in tqdm(os.listdir(os.path.join(merge_folder, year))):
        content = ""
        for file in os.listdir(os.path.join(merge_folder, year, file_name)):
            with open(os.path.join(merge_folder, year, file_name, file), encoding='utf8') as f:
                content += f.read() + "\n"
        
        with open(os.path.join("data", file_name + ".txt"), "w", encoding='utf8') as writer:
            writer.write(content)