# -*- coding:utf-8 -*-
import urllib2
import re
import time

def saveImg(imageURL, fileName):
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
    headers = {'User-Agent': user_agent}

    request = urllib2.Request(imageURL, None, headers)
    response = urllib2.urlopen(request)
    # u = urllib.urlopen(imageURL)
    data = response.read()
    with open(fileName, 'wb') as f:
        f.write(data)
        f.close()

page = 2
if page == 1:
    url = 'https://www.666lu.vip/html/tupian/siwa/index.html'
else:
    url = 'https://www.666lu.vip/html/tupian/siwa/index_'+ str(page) +'.html'

"""F12, 看Network里面的一个GET的Request headers"""
user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"
headers = {'User-Agent' : user_agent}

request = urllib2.Request(url, None, headers)
response = urllib2.urlopen(request)
html_1 = response.read().decode('utf-8')

pattern1 = re.compile('<li><a href="(.*?)" target="_blank">.*?</a> <span>.*?</span></li>', re.S)
list1 = re.findall(pattern1, html_1)
i = 0
for item in list1:
    # print(item)
    url2 = 'https://www.666lu.vip' + item
    request = urllib2.Request(url2, None, headers)
    response = urllib2.urlopen(request)
    html_2 = response.read().decode('utf-8')

    pattern2 = re.compile('<p><img alt="" src="(.*?)" /></p>', re.S)
    list2 = re.findall(pattern2, html_2)
    for item2 in list2:
        if(len(item2) < 60):
            i = i + 1
            # print(item2)
            img_url = 'https:' + item2
            print('正在抓取第'+str(i)+'张照片')
            saveImg(img_url, str(i)+'.jpg')
            time.sleep(0.1)
            print('第' + str(i) + '张照片抓取完毕')
