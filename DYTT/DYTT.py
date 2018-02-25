# -*- coding:utf-8 -*-
import requests
import re
import time
import codecs


a_url = 'http://www.dytt8.net/html/gndy/dyzz/20180217/56339.html'
# print(a_url)
html_1 = requests.get(a_url)
html_1.encoding = 'gb2312'
# print(html_1.status_code) # 200 访问正常
# print(html_1.text) # 查看网页源代码
list1 = re.findall('<a href=\'(.*?)\'>2018', html_1.text)
for i in range(len(list1)):
    b_url = 'http://www.dytt8.net' + str(list1[i])
    # print(b_url)

    html_2 = requests.get(b_url)
    html_2.encoding = 'gb2312'
    # print(html_2.text)
    """(.*?)就是提取想要的信息， 不加()就不提取"""
    list2 = re.findall('<a href="(.*?)">.*?</a></td>', html_2.text)
    """只拿一个链接"""
    result = list2[0]
    print(result)
    with codecs.open('/home/luyifan/Project/Web_Crawler/DYTT/dytt.txt', 'a', encoding='utf-8') as f:
        f.write(result+'\n')


