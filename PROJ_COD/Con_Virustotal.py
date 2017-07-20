import requests
import json
import hashlib
import sys

"""
작성일   : 2017-07-??(최초작성)
수정일   : 
버전     : v1.0(수정시 버전 올려주세요)
프로그램 : 
"""

class Virustotal():
    """ Virustotal API module """

    def __init__(self):
        self.host = "www.virustotal.com"
        self.base = "https://www.virustotal.com/vtapi/v2/"
        self.apikey = ""
        # self.filepath = input("file path :")    #


    def md5(self,i, blocksize=8192):
        md5 = hashlib.md5()
        try:
            f = open(i, "rb")
            # f = open("C:\\Users\kitri\PycharmProjects\shutdown\PROJ_COD\pika.exe", "rb")
        except IOError as e:
            print("file open error", e)
            return
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            md5.update(buf)
        return md5.hexdigest()



    def rscReport(self,filemd5):
        """ Get latest report of resource """
        try:
            base = self.base + 'file/report'
            parameters = {"resource": filemd5, "apikey": "1debafcb5beab36b14e610bf8b8fdf33a86cd59bffc8413b36c212bf260284b7"}
            r = requests.post(base, data=parameters)
            resp = r.json()
            results = parse_resp(resp)
            return results
        except:
            base = self.base + 'file/report'
            parameters = {"resource": filemd5, "apikey": "30c7167cd6890a8e26e7bb29cc0c9c4354cdb5a7b6ec8a187fe16a1dad2f4a07"}
            r = requests.post(base, data=parameters)
            resp = r.json()
            results = parse_resp(resp)
            return results

    def urlReport(self, rsc, scan=0):
        """ Get latest report URL scan report of resource """

        base = self.base + 'url/report'
        parameters = {"resource": rsc, "scan": scan, "apikey": self.apikey}
        r = requests.post(base, data=parameters)
        resp = r.json()
        results = parse_resp(resp)
        return results

    def ipReport(self, rsc):
        """ Get latest report for IP Address """

        base = self.base + 'ip-address/report'
        parameters = {"ip": rsc, "apikey": self.apikey}
        r = requests.get(base, params=parameters)
        resp = r.json()
        results = parse_resp(resp)
        return results

    def domainReport(self, rsc):
        """ Get latest report for IP Address """

        base = self.base + 'domain/report'
        parameters = {"domain": rsc, "apikey": self.apikey}
        r = requests.get(base, params=parameters)
        resp = r.json()
        results = parse_resp(resp)
        return results

    def scanURL(self, rsc):

        """ Send RSC/URL for scanning; Its encouraged to check for last scanusing urlReport()
        To submit batch rsc should be example.com\nexample2.com"""

        base = self.base + 'url/scan'
        parameters = {"url": rsc, "apikey": self.apikey}
        r = requests.post(base, data=parameters)
        resp = r.json()
        results = parse_resp(resp)
        return results

    def rscSubmit(self, rsc):

        """ Submit potential malicious file to virustotal for analyzing """
        base = self.base + 'file/scan'
        f = open(rsc, 'rb')
        parameters = {"apikey": self.apikey}
        r = requests.post(base, data=parameters, files={'file': f})
        resp = r.json()
        results = parse_resp(resp)
        return results

    def rscRescan(self, rsc):

        """ Rescan potential malicious file to virustotal for analyzing without uploading the file again """
        base = self.base + 'file/rescan'
        parameters = {"resource": rsc, "apikey": self.apikey}
        r = requests.post(base, data=parameters)
        resp = r.json()
        results = parse_resp(resp)
        return results

    def postComment(self, rsc, comment):

        """ Post comment to files or urls """
        base = self.base + 'comments/put'
        parameters = {"resource": rsc, "comment": comment, "apikey": self.apikey}
        r = requests.post(base, data=parameters)
        resp = r.json()
        results = parse_resp(resp)
        if results['response_code'] == 0:
            print
            "Oh no something happen...cant post comment"
        else:
            print
            "Your comment was successfully posted"
            call = self.rscReport(rsc)
            for item in call:
                if item == "permalink":
                    print
                    "Report link:", call[item]


def parse_resp(resp):
    """ Parses the response from the requests.gets/posts()
    then returns the data back to the function """
    buf = {}
    for item in resp:
        buf[item] = resp[item]

    return buf

def get_mal_kind(i):
    main = Virustotal()
    var = main.md5(i)
    dic = main.rscReport(var)

    if dic['positives'] > 4:
        for key, value in dic['scans'].items():
            if value['result'] != None:
                return dic['positives'], value['result'], dic['md5']
    else:
        return 0, None, None




# main = Virustotal()
# # print (main.md5())
# var = main.md5()
# dic = main.rscReport(var)
# print(dic)

# if dic['positives'] > 4:
#     for key, value in dic['scans'].items():
#         if value['result'] != None:
#             print( value['result'])




"""
if dic['positives'] >= 10:
    print("VIRUS!!!")
else:
    print("NOMAL FILE")
print ("total = " , dic['total'],"positives = " , dic['positives'])"""