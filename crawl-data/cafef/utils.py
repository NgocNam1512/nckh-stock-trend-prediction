import os

def pdate2date(pdate:str) -> str:
    datetime = pdate.split(" ")[0]
    date, month, year = datetime.split("-")
    return year + month + date

def save(name:str, content:str, datetime:str, path:str):
    path_datetime = os.path.join(path, datetime)
    if not os.path.exists(path_datetime):
        os.makedirs(path_datetime)

    save_path = os.path.join(path_datetime, name)
    with open(save_path, "w", encoding='utf8') as writer:
        writer.write(content)    