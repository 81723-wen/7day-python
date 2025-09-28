import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

HEADERS = {'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac Os X 10_15_7)'
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safair/537.36'
}
BASE_URL = 'http://movie.douban.com/top250?start={}'

data = []
for start in range(0, 250, 25):    #0 25 50 … 225
    url = BASE_URL.format(start)
    resp = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')
    items = soup.select('div.item')
    for item in items:
        rank = item.select_one('em').text
        title = item.select_one('span.title').text
        score = item.select_one('span.rating_num').text
        quote_tag = item.select_one('span.inq')
        quote = quote_tag.text if quote_tag else ''
        data.append([rank, title, score, quote])
    print(f'已爬完{start//25 + 1}页')
    time.sleep(1)   #礼貌等待1秒

    df = pd.DataFrame(data, columns=['排名','电影名','评分','引言'])
    df.to_csv('douban_top250.csv', index=False, encoding='utf-8-sig')
    print('已保存 douban_top250.csv,共',len(df),'部影片')

import os 
os.system('open douban_top250.csv')  #Mac
#