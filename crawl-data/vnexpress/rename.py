import os

folder = 'vnexpress-data'
sub_folders = os.listdir(folder)
for sub in sub_folders:
    dates = os.listdir(os.path.join(folder, sub))
    for date in dates:
        files = os.listdir(os.path.join(folder, sub, date))
        for f in files:
            filename = os.path.join(folder, sub, date, f)
            os.rename(filename, filename.replace(".html", ".txt"))