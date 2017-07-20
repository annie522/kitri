# -*-coding:utf-8-*-
# 2014. 04. 02 coded by g0n4k00
# http://malc0de.com/database/

import urllib, urllib2
from bs4 import BeautifulSoup

index_no = 1
for page in range(8):
    try:
        url = "http://malc0de.com/database/?&page=" + str(page)
        req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})  # because 403 forbidden
        html = urllib2.urlopen(req).read()
        print "[+] %d Page read complete" % page

        soup = BeautifulSoup(html)
        element = soup.findAll('tr', {'class': 'class1'})
        print "[+] %d Page parsing complete" % page

        print "[+] %d Page malware download start" % page
        for i in range(0, 77):
            try:
                item = element[i].text.split()
                url = "http://" + item[1]
                name = str(index_no) + "_" + str(
                    item[-1])  # item[1]=file_download_url item[-1]=md5  filename=index_no+"_"+item[-1]

                urllib.urlretrieve(url, name)
                print "\t[-] %d file down complete..." % index_no
                index_no = index_no + 1
            except:
                print "\t[-] Excpetion occur, pass!"
    except:
        print "\t[-] Excpetion occur, pass!"

    print "[-] %d Page work complete\n" % page
