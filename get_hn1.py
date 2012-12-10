
import getopt
from BeautifulSoup import BeautifulSoup
import re
import urllib
from urllib2 import Request, urlopen, URLError, HTTPError
import socket
import os
import sys
import pprint

url = 'http://news.ycombinator.com/'

def main():
    news  = [] 
    soup = BeautifulSoup(get_hn(url))
    for tr in soup.findAll('tr'):
        if tr.find('td', {'class':'title'}):
            if len(tr.findAll('td')) > 3:
                pass
            else:
                news_item  = {}
                info = tr.nextSibling
                if info is not None:
                    ref = info.find('td', {'class':'subtext'})
                    if ref is not None:
                        for i in ref.contents:
                            if hasattr(i, 'contents'):
                                info_d = ''.join(i.contents)
                                #print info_d
                                m = re.search(r'(\d+)\s+point', info_d)
                                if m is not None:
                                    news_item['p'] = m.group(1)

                                m = re.search(r'(\d+)\s+comment', info_d)
                                if m is not None:
                                    news_item['c']  = m.group(1) 

                            else:
                                #print str(i)
                                m = re.search(r'^\s*(.*)\s+ago\s+\|', i)
                                if m is not None:
                                    news_item['t'] = m.group(1) 

                #print str(tr.contents[-1])
                news_item['n'] = str(tr.contents[-1])
                news.append(news_item)

    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint(news)
    gen_news()

    print 'done ......'

def get_hn(url):
    # timeout in seconds
    timeout = 30
    socket.setdefaulttimeout(timeout)

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    #data = urllib.urlencode(info)
    data = '' 

    req = Request(url, data, headers)

    try:
        response = urlopen(req)
    except HTTPError, e:
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    except URLError, e:
        print 'Failed to reach a server.'
        print 'Reason: ', e.reason
    else:
        # everything is fine
        return response.read()

if __name__ == "__main__":
    main()
