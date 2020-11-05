import requests
from bs4 import  BeautifulSoup
import re

def main():
    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html')
    soup = BeautifulSoup(resp.text,"html.parser")
    # 找出所有 'h' 開頭的標題文字

    titles = soup.find_all(['h1','h2','h3','h4','h5','h6'])
    for title in titles:
        print(title.text.strip())

    # 利用 regex 找出所有 'h' 開頭的標題文字
    for title in soup.find_all(re.compile('h[1-6]')):
        print(title.text.strip())
    # 找出所有 .png 結尾的圖片
    imgs = soup.find_all('img')
    for img in imgs:
        if 'src' in img.attrs:
            if img['src'].endswith('.png'):
                print(img['src'])
    # 利用 regex 找出所有 .png 結尾的圖片
    for img in soup.find_all('img', {'src': re.compile('\.png$')}):
        print(img['src'])

    # 找出所有 .png 結尾且含 'beginner' 的圖片
    imgs = soup.find_all('img')
    for img in imgs:
        if 'src' in img.attrs:
            if 'beginner' in img['src'] and img['src'].endswith('.png'):
                print(img['src'])

    # 利用 regex 找出所有 .png 結尾且含 'beginner' 的圖片
    for img in soup.find_all('img', {'src': re.compile('beginner.*\.png$')}):
        print(img['src'])

    #總共有幾篇 blog 貼文
    print("共幾篇 %d BLOG文章" %len(soup.find_all('div','card card-blog')))
    #總共有幾張圖片網址含有 'crawler' 字串
    print("包含crawler字串:%d" %len(soup.find_all('img',{'src': {re.compile('.crawler.')}})))
    #總共有幾堂課程
    resp = requests.get("http://blog.castman.net/web-crawler-tutorial/ch2/table/table.html")
    soup = BeautifulSoup(resp.text, 'html.parser')
    print("總共有幾堂課程: %d " %len(soup.find('tbody').find_all('tr')))



if __name__ == '__main__':
    main()