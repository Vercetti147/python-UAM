# -*- coding: cp1250 -*-
# Michal Wierzchowski YouTybe Downloader 1.0
import urllib2, re, pytube, os

result = False
links = []
try:
    while result == False:
        response = urllib2.urlopen('https://www.youtube.com/watch?v=k6U-i4gXkLM&list=PL57FCE46F714A03BC')
        ps = response.read()
        tab = re.findall(r'/watch\?v=([a-zA-Z0-9-=_]*&amp;list=PL57FCE46F714A03BC&amp;index=[0-9]+)"', ps)
        lista = list(set(tab))
        if len(lista)==24:
            result = True
        
    print str(len(lista))
    for x in lista:
        index = x.index('&')
        slink = x[0:index]
        link ='https://www.youtube.com/watch?v='+slink
        links.append(link)

    for video in links:
        yt = pytube.YouTube(video)
        if os.path.isfile(os.getcwd()+ '\\' +(yt.filename)+'.mp4'):
            print 'File: ' + (yt.filename)+'.mp4 already exist'
            continue
        print 'Downloading: ' + (yt.filename)
        video = yt.filter('mp4')[-1]
        video.download(os.getcwd())
        print 'OK'
except:
        import sys
        print sys.exc_info()[0]
        import traceback
        print traceback.format_exc()
finally:
        print "Press Enter to continue ..." 
        raw_input()      

