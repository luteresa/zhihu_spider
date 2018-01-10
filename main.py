#coding:utf-8
"""
__tile__=''
__auther__='leon'
__mtime__='2018/1/8'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from bs4 import *
from urllib3 import *
disable_warnings()

url='https://www.zhihu.com/people/matongxue/activities'

disable_warnings()

http = PoolManager()
r = http.request('GET',url)
soup = BeautifulSoup(r.data,'lxml')

from spyder import *
for tag in soup.find_all(True):
    if tag.name == 'a':
        if tag.get('target') == '_blank' and tag.parent.name=='div' and\
                tag.parent.get('itemprop') == 'zhihu:question':
            print(tag.text)
            html ='https://www.zhihu.com{}'.format(tag.get('href'))
            print(html)
            print('https://www.zhihu.com/question/23149768/answer/282842210')
            getContent(html)

