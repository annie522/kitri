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
            print("[+] file open error", e)
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
            print("[+] VIRUSTOTAL API : Number01")
            r = requests.post(base, data=parameters)
            resp = r.json()
            results = parse_resp(resp)
            return results
        except:
            try:
                base = self.base + 'file/report'
                parameters = {"resource": filemd5, "apikey": "30c7167cd6890a8e26e7bb29cc0c9c4354cdb5a7b6ec8a187fe16a1dad2f4a07"}
                print("[+] VIRUSTOTAL API : Number02")
                r = requests.post(base, data=parameters)
                resp = r.json()
                results = parse_resp(resp)
                return results
            except:
                try:
                    base = self.base + 'file/report'
                    parameters = {"resource": filemd5,
                                  "apikey": "c56069a2add618e2d5b8b9a08783c4503d3d240141edc4b485d23a59a8faccbe"}
                    print("[+] VIRUSTOTAL API : Number03")
                    r = requests.post(base, data=parameters)
                    resp = r.json()
                    results = parse_resp(resp)
                    return results
                except:
                    try:
                        base = self.base + 'file/report'
                        parameters = {"resource": filemd5,
                                      "apikey": "1debafcb5beab36b14e610bf8b8fdf33a86cd59bffc8413b36c212bf260284b7"}
                        print("[+] VIRUSTOTAL API : Number04")
                        r = requests.post(base, data=parameters)
                        resp = r.json()
                        results = parse_resp(resp)
                        return results
                    except:
                        try:
                            base = self.base + 'file/report'
                            parameters = {"resource": filemd5,
                                          "apikey": "92b754bf98f0cad80c68e335d61022701105812413c98b0a8837078d7d2c7aaf"}
                            print("[+] VIRUSTOTAL API : Number05")
                            r = requests.post(base, data=parameters)
                            resp = r.json()
                            results = parse_resp(resp)
                            return results
                        except:
                            try:
                                base = self.base + 'file/report'
                                parameters = {"resource": filemd5,
                                              "apikey": "4d6c4555648946ccf662bc89b1d0dc0955e72dd78fdf3e1ea7b69dfad33f30f8"}
                                print("[+] VIRUSTOTAL API : Number06")
                                r = requests.post(base, data=parameters)
                                resp = r.json()
                                results = parse_resp(resp)
                                return results
                            except:
                                try:
                                    base = self.base + 'file/report'
                                    parameters = {"resource": filemd5,
                                                  "apikey": "4275b38fa43013c2193acb1c7cd057d2c815644f3ea69c70e3fb464f54e0cacb"}
                                    print("[+] VIRUSTOTAL API : Number07")
                                    r = requests.post(base, data=parameters)
                                    resp = r.json()
                                    results = parse_resp(resp)
                                    return results
                                except:
                                    print("[+] U NEED MORE VIRUSTOTAL API KEY")

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

def get_mal_kind(fileName):
    main = Virustotal()
    var = main.md5(fileName)
    dic = main.rscReport(var)
    try:
        if dic['positives'] > 10:
            for key, value in dic['scans'].items():
                if value['result'] != None:
                    return dic['positives'], value['result'], dic['md5']
        else:
            return 0, None, None
    except:
        print("[+] dic['positives'] DOES NOT EXIST.")
        return 0, None, None
