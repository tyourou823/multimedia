# -*- coding: utf-8 -*-
import feedparser
import httplib2
import os
import time
import datetime


def download_picture(q, count):
    u"""qの画像をcount件 取ってくる。"""
    count = str(count)
    feed = feedparser.parse("https://picasaweb.google.com/data/feed/base/all?q=" + q + "&max-results=" + count)
    pic_urls = []
    http = httplib2.Http(".chache")
    for entry in feed['entries']:
        url = entry.content[0].src
        d = datetime.datetime.today()
        date = str(d)
        open('./landview/'+os.path.basename("land")+date,'wb').write(http.request(url)[1])
        print('download:' + url)

if __name__ == "__main__":
    time1=time.time()
    download_picture("landscape", 10)
    time1_2=str(time.time()-time1)
    print("complete!("+time1_2+")")