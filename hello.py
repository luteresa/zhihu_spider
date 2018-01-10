from urllib3 import *
url2='https://www.zhihu.com/equation?tex=0.5%5Ctimes+0.5%3D0.25'
url='https://pic1.zhimg.com/v2-aafc4dddb4fd9e7a47fb222841fdf06d_b.gif'
http=PoolManager()
r = http.request('GET',url)
f = open('t3.jpg','wb')
f.write(r.data)
f.close()