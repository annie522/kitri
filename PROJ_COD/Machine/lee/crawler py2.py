#!/usr/bin/python
# Copyright (C) 2012 Ricardo Dias
#
# Malware Crawler Module v0.4
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Requirements:
# - BeautifulSoup 3.0.8
from bs4 import BeautifulSoup
import sys
import hashlib
import re
import urllib2
import magic
import os
import socket
import datetime
import vtquery
import time
import pymongo

# By default thug analyis is disabled
isthug = False

# variable for date value manipulation
now = datetime.datetime.now()
str(now)

# maximum wait time of http gets
timeout = 15
socket.setdefaulttimeout(timeout)

def md5(filename):
    """Calculate the md5 hash of a file. Memory-friendly solution, it reads the file piece by piece.
    http://stackoverflow.com/questions/1131220/get-md5-hash-of-a-files-without-open-it-in-python"""
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), ''):
            md5.update(chunk)
    return md5.hexdigest()


# load thug function, also checks if thug is installed
def loadthug():
    try:
        sys.path.append('../thug/src')


        import thug

        isthug = True
        print("- Thug module loaded for html analysis")
    except ImportError:
        print("- No Thug module found, html code inspection won't be available")


# determine file type for correct archival
def gettype(file_):


# ms = magic.open(magic.MAGIC_NONE)
    ms = magic.from_buffer(file_)
# ms.load()
# return ms.buffer(file)
    return ms


# beautifulsoup parser
def parse(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1)')
    try:
        http = BeautifulSoup(urllib2.urlopen(request), "lxml")
    except:
        print "- Error parsing %s" % (url)
    return
    return http

    #request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1)')
    #try:
    #    http = BeautifulSoup(urllib3.urlopen(request), "lxml")
    #except:
    #    print("- Error parsing %s" % (url))
    #return
    #return http


def decisor(site, url):
    if not re.match('http', url):
        url = 'http://' + url


        try:
            url_dl = urllib2.urlopen(url).read()
        except Exception as e:
            print("-- %s Error: %s %s" % (site, str(e), url))
        return
        filetype = gettype(url_dl).split(' ')[0]

    if (filetype == 'HTML'):
        if isthug:
            print("-- Thug candidate: HTML code in %s" % url)

        try:
            thug.Thug([url])()
        except Exception as e:
            print("- Thug error: %s" % e)
        return

    else:
        dest = './malware/' + filetype
        temp_fpath = dest + '/temp'

    if not os.path.exists(dest):
        os.makedirs(dest)

    if not os.path.exists(temp_fpath):
        file = open(temp_fpath, 'wb')
        file.write(url_dl)
        file.close
        md5_val = md5(temp_fpath)

        os.rename(temp_fpath, dest + "/" + md5_val)
        fpath = dest + "/" + md5_val
        time.sleep(1)
        print("-- " + site + " Saved file type %s with md5: %s" % (filetype, md5_val))
        try:
            vtquery.get_vt_result(md5_val, fpath, url, site)
        except:
            pass


def malwaredl(soup):
    print("- Fetching from Malware Domain List")


    mdl = []
    for row in soup('description'):
        mdl.append(row)
        del mdl[0]
        mdl_sites = []
    for row in mdl:
        site = re.sub('&', '&', str(row).split()[1]).replace(',', '')
    if site == '-':
        mdl_sites.append(re.sub('&', '&', str(row).split()[4]).replace(',', ''))
    else:
        mdl_sites.append(site)
        print("-- Found %s urls" % len(mdl))
    for row in mdl_sites:
        decisor("malwaredl", row)


def vxvault(soup):
    print("- Fetching from VXVault")


    vxv = []
    for row in soup('pre'):
        vxv = row.string.split('\r\n')
        del vxv[:2]
        del vxv[-1]
        print("-- Found %s urls" % len(vxv))
    for row in vxv:
        decisor("vxvault", row)


def malc0de(soup):
    print("- Fetching from Malc0de")


    mlc = []
    for row in soup('description'):
        mlc.append(row)
        del mlc[0]
        mlc_sites = []
    for row in mlc:
        site = re.sub('&', '&', str(row).split()[1]).replace(',', '')
        mlc_sites.append(site)
        print("-- Found %s urls" % len(mlc_sites))
    for row in mlc_sites:
        decisor("malc0de", row)


def malwarebl(soup):
    print("- Fetching from Malware Black List")


    mbl = []
    for row in soup('description'):
        site = str(row).split()[1].replace(',', '')
        mbl.append(site)
        print("-- Found %s urls" % len(mbl))
    for row in mbl:
        decisor("malwarebl", row)


def minotaur(soup):
    print("- Fetching from NovCon Minotaur")


    min = []
# for row in soup('td'):
#  try:
#  if re.match('http',row.string):
#  min.append(row.string)
#  except:
#  pass
    minota_body = soup.find("div", {"id": "mtabs-2"})
    parse_tr = minota_body.findAll("tr")
    for row in parse_tr:
        list_td = row.findAll("td")
        if len(list_td) == 0:
            continue
        try:
            min.append(list_td[3].text)
        except:
            pass
        print("-- Found %s urls" % len(min))
    for row in min:
        decisor("minotaur", row)


def sacour(soup):
    print("- Fetching from Sacour.cn")


    for url in soup('a'):
        min = []
        if re.match('list/', url['href']):
            suburl = parse('http://www.sacour.cn/' + url['href'])
            for text in suburl('body'):
                for urls in text.contents:
                    if re.match('http://', str(urls)):
                        min.append(str(urls))
                        if len(min) > 0:
                            print("-- Found %s urls in %s" % (len(min), url['href']))
                        for row in min:
                            decisor("sacour", row)


def main():
    print("Malware Parser v0.4")
    try:
        if sys.argv[1] == '-t':
            loadthug()
    except:
        print("- Thug analysis not enabled (use -t to enable thug)")
    while True:
        try:
            # source list
            try:
                minotaur(parse('http://minotauranalysis.com'))
            except:
                pass
            try:
                malwaredl(parse('http://www.malwaredomainlist.com/hostslist/mdl.xml'))
            except:
                pass
            try:
                vxvault(parse('http://vxvault.siri-urz.net/URL_List.php'))
            except:
                pass
            try:
                malc0de(parse('http://malc0de.com/rss'))
            except:
                pass
            try:
                malwarebl(parse('http://www.malwareblacklist.com/mbl.xml'))
            except:
                pass
            # sacour(parse('http://www.sacour.cn/showmal.asp?month=%d&year=%d' % (now.month, now.year))) #site die
            time.sleep(30)
        except Exception as e:
            print (e)
            time.sleep(30)

if __name__ == "__main__":
    main()