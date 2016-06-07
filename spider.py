import urllib.request
import re
import time


def gethtml(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=header)
    data = urllib.request.urlopen(req).read().decode('utf-8')
    return data


def gettopic(html):
    url = r'https://www.douban.com/group/topic/\d+'
    topiclist = re.findall(url, html)
    x = 0
    return topiclist


def download(html):
    reg = r'https://img3.doubanio.com/view/group_topic/large/public/.+\.jpg'
    imglist = re.findall(reg, html)
    i = 1
    download_img = None
    for imgurl in imglist:
        img_numlist = re.findall(r'p\d{8}', imgurl)
        for img_num in img_numlist:
            download_img = urllib.request.urlretrieve(imgurl, 'G:\python\download\%s.jpg' % img_num)
            time.sleep(1.51)
            i += 1
            print(imgurl)
    return download_img


group_name = str(input('请输入小组英文缩写：'))
page_end = int(input('请输入结束时的页码：'))
num_end = page_end * 25
num = 0
page_num = 1
while num <= num_end:
    html2 = gethtml('http://www.douban.com/group/h' + group_name + '/discussion?start=%d' % num)
    topiclist = gettopic(html2)
    # 限制下载的图片数
    for topicurl in topiclist:
        topic_page = gethtml(topicurl)
        download_img = download(topic_page)
        num = page_num * 25
        page_num += 1

else:
    print('采集完成！')
