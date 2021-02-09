import os
import requests
import time
import img2pdf


# from os.path import join


def createFolder(folder):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"建立資料夾 ==> {folder}")
        else:
            print(f"資料夾已經存在 => {folder}")
    except OSError:
        print(f"Error: Create directory. ==> {folder}")


def parserWebPages(path, url, pages):
    pageNums = "?p="
    prelink = url.index(pageNums)
    postlink = url.index("&f=")

    str1 = url[0:prelink+3]
    str2 = url[postlink:-1]

    for page in range(1, int(pages) + 5):
        ebookurl = str1 + str(page).zfill(3) + str2
        image_name = path + "\\" + str(page).zfill(3) + ".jpg"
        #print(image_name)
        #print(ebookurl)
        
        resp = requests.get(ebookurl)
        if resp.status_code == 200:
            with open(image_name, "wb") as file:
                file.write(resp.content)
            print(f"第 {page} 頁")
        else:
            print(f"error: => {resp.status_code}")
        time.sleep(1)



def getBooks(books):
    global currentDir
    for line in books:
        book = line.strip().split(";")
        createFolder(currentDir+"\\"+book[0])
        parserWebPages(currentDir+"\\"+book[0], book[2], book[1])


def setEbookDict(dir):
    books = []
    files = os.listdir(dir)
    for f in files:
        fullPath = os.path.join(dir, f)
        bookdic = {}
        if os.path.isdir(fullPath):
            # print(f)
            bookdic['name'] = f
            bookdic['path'] = fullPath
            books.append(bookdic)
    return books

def getBooklinks(txtPath):
    if os.path.exists(txtPath):
        # utf-8 編碼問題
        with open(txtPath, 'r', encoding="utf-8") as f:
            lines = f.readlines()
    else:
        print("Error: 書單列表不存在")
    return lines

def merge2pdf(ebookDict):

    for folder in ebookDict:
        global currentDir
        pdf_file = currentDir+"\\"+folder["name"] + ".pdf"
        #print(pdf_file)
        arr = []
        for img in os.listdir(folder['path']):
            arr.append(currentDir+"\\"+folder['name'] + "\\" + img)

        #print(arr)
        pdf_obj = img2pdf.convert(arr)
        with open(pdf_file, 'wb') as f:
            f.write(pdf_obj)
        print(f"Done => {pdf_file}")


if __name__ == '__main__':
    currentDir = os.path.dirname(os.path.realpath(__file__))
    print(currentDir)
    txtFilePath = currentDir + "\\books.txt"
    print(txtFilePath)
    txtContent = getBooklinks(txtFilePath)
    getBooks(txtContent)
    print("Download finished!")
    ebookDict = setEbookDict(currentDir)
    #print(ebookDict)
    merge2pdf(ebookDict)
    print("Finish")
