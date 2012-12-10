
import getopt
from BeautifulSoup import BeautifulSoup
import re
import urllib
from urllib2 import Request, urlopen, URLError, HTTPError
import socket
import os
import sys
import pwd

url = 'http://news.ycombinator.com/'

def main():
    soup = BeautifulSoup(get_hn(url))
    for tr in soup.findAll('tr'):
        if tr.find('td', {'class':'title'}):
            if len(tr.findAll('td')) > 3:
                pass
            else:
                print "=======" 
                get_hn_info(str(tr.nextSibling))

                print str(tr.contents[-1])

def get_hn_info(info):
    hni_s = BeautifulSoup(info)
    ref = hni_s.findAll('td', {'class':'subtext'})
    for ref in ref[0]:
        #get_hn_item(str(ref))
        print str(ref)

def get_hn_item(line):
    if re.search(r' by *$', line) is not None:
        pass

    m = re.search(r'(\d+)\s+point', line)
    if m is not None:
        print m.group(1) 

    m = re.search(r'(\d+)\s+comment', line)
    if m is not None:
        print m.group(1) 

    m = re.search(r'^\s*(.*)\s+ago\s+|', line)
    if m is not None:
        print m.group(1) 

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
