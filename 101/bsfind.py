import requests
from bs4 import BeautifulSoup

def main():
    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html')
    soup = BeautifulSoup(resp.text,"html.parser")
    """
    print("取得第一篇 blog (h4)")
    print(soup.find('h4'))
    print(soup.h4)
    print("取得第一篇 blog 主標題")
    print(soup.h4.a.text)
    print("取得所有 blog 主標題, 使用 tag")
    titles = soup.find_all('h4')
    for title in titles:
        print(title.a.text)
    
    print("取得所有 blog 主標題, 使用 class")
    print(soup.find_all('h4', 'card-title'))
    print(soup.find_all('h4', {'class': 'card-title'}))
    print(soup.find_all('h4', class_="card-title"))
    
    titles = soup.find_all('h4', 'card-title')
    for title in titles:
        print(title.a.text)
    print(soup.find(id='mac-p'))
    """
    #print(soup.find(data-foo='mac-foo'))
    #print(soup.find('', {'data-foo':'mac-foo'}))
    print("取得各篇 blog 的所有文字")
    divs = soup.find_all('div','content')
    for div in divs:
        #print(div.text)
        #print(div.h6.text.strip(),div.h4.a.text.strip(),div.p.text.strip()®)
        print([s for s in div.stripped_strings])

if __name__ == '__main__':
    main()
