
import getopt
from BeautifulSoup import BeautifulSoup
import re
import urllib
from urllib2 import Request, urlopen, URLError, HTTPError
import socket
import os
import sys
import pwd

url = 'http://news.ycombinator.com/news2'
#url = 'http://news.ycombinator.com/x?fnid=uPcNC241wo'

def main():
    soup = BeautifulSoup(get_hn(url))
    #link = soup.find(text='More').findParent()
    print soup.find(text='More').findParent()['href']
    #print link['href']

    #for tr in soup.findAll('tr'):
        #if tr.find('td', {'class':'title'}):
            #if len(tr.findAll('td')) > 3:
                #pass
                #print "xxxxxxx" 
                #print str(tr) 
            #else:
                #print "=======" 
                #print str(tr) 

    #print soup.prettify()

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
