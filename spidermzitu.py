# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
 

def getimg(baseurl, title):
    #baseurl是第一张图片地址,输入变量后，可以获取此组图片，保存在文件夹内
    #name = name
    html = requests.get(baseurl, headers=headers)
    html_Soup = BeautifulSoup(html.text, 'lxml')
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    path = title.replace('?', '_').replace(' ', '_')
    mkdir(path)
    os.chdir("E:\mzitu\\"+path)
    for page in range(1, int(max_span)+1): ##不知道为什么这么用的小哥儿去看看基础教程吧
        page_url = baseurl + '/' + str(page) ##同上
        #print(page_url)
        img_html = requests.get(page_url, headers=headers)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_='main-image').find('img')['src'] ##这三行上面都说过啦不解释了哦
        #print(img_url)        
        name = img_url[-9:-4] ##取URL 倒数第四至第九位 做图片的名字
        img = requests.get(img_url, headers=headers)
        f = open(name+'.jpg', 'wb')##写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(img.content) ##多媒体文件要是用conctent哦！
        f.close()
def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(os.path.join("E:\mzitu", path))
    if not isExists:
        print(u'建了一个名字叫做', path, u'的文件夹！')
        os.makedirs(os.path.join("E:\mzitu", path))
        return True
    else:
        print(u'名字叫做', path, u'的文件夹已经存在了！')
        return False

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
a=[];
a.append('/')
#datafile = open('data.txt','w')
for pagenum in range(2,77):
    a.append('/page/'+str(pagenum))
for pagenum in a:
    nexturl = 'http://www.mzitu.com/xinggan'+pagenum
    start_html = requests.get(nexturl, headers=headers)
    Soup = BeautifulSoup(start_html.text, 'html5lib')
    all_li = Soup.find('ul', id="pins").find_all('li')
    
    try:
        for li in all_li:
        #print(li.find('a'))
            #datafile.write(li.find('a')['href']+'\n'+li.find('a').find('img')['alt']+'\n\n')
            getimg(li.find('a')['href'], li.find('a').find('img')['alt'])        
        print(str(pagenum))
    except:
        print('error'+str(pagenum))
        continue
    print(nexturl)          
#datafile.close()
    


    
    

