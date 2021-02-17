from get_links import get_links
from get_content import get_html, get_date, get_content, save
from tqdm import tqdm

for i in tqdm(range(1, 570)):
    url = f'https://vnexpress.net/kinh-doanh/chung-khoan-p{i}'
    try:
        links = get_links(url)
        for link in links:
            try:
                soup = get_html(link)
                content = get_content(soup)
                date, year = get_date(soup)
                save(link.replace("https://vnexpress.net/", "").replace(".html", ".txt"), content, year, date, "vnexpress-data")
            except:
                print("error:", link)
    except:
        print("error:", url)