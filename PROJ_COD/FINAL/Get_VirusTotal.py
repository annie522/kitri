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
#바이러스 토탈 클래스
class Virustotal():
    """ Virustotal API module """

    def __init__(self):
        self.host = "www.virustotal.com"
        self.base = "https://www.virustotal.com/vtapi/v2/"
        self.apikey = ""


    #MD5 값 가져오기(바이러스 토탈이 아니라 로컬에서 가져오는 파일)
    def md5(self,i, blocksize=8192):
        md5 = hashlib.md5()
        try:
            f = open(i, "rb")

        except IOError as e:
            print("[+] file open error", e)
            return
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            md5.update(buf)
        print("md5")
        print(md5.hexdigest())
        print("md5")
        return md5.hexdigest()

    #바이러스 토탈에 정보를 넘겨서 바이러스 토탈의 Report 값 가져오기
    def rscReport(self,filemd5):
        try:
            params = {'apikey': '7a20a8ed49ca09b249073a380e36b69830d4d58172fc5c9be7b42b24fdd4d183', 'resource': filemd5}
            headers = {
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "gzip,  My Python requests library example client or username"
            }
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)
            json_response = response.json()
            results = parse_resp(json_response)
            return results

        except:
            try:
                base = self.base + 'file/report'
                parameters = {"resource": filemd5,
                              "apikey": "30c7167cd6890a8e26e7bb29cc0c9c4354cdb5a7b6ec8a187fe16a1dad2f4a07"}
                print("[+] VIRUSTOTAL API : Number02")
                r = requests.post(base, data=parameters)
                resp = r.json()
                results = parse_resp(resp)
                return results
            except:
                try:
                    base = self.base + 'file/report'
                    parameters = {"resource": filemd5,
                                  "apikey": "8572f48edcf472921571b816260d668dbfcd9695568507f117682de63ae11e46"}
                    print("[+] VIRUSTOTAL API : 주승Number03")
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
                                                  "apikey": "a120f0984893b4d33b199baaa2e7929c61bb921918d8de1df36d629d12839905"}
                                    print("[+] VIRUSTOTAL API : Number07")
                                    r = requests.post(base, data=parameters)
                                    resp = r.json()
                                    results = parse_resp(resp)
                                    return results
                                except:
                                    print("[+] U NEED MORE VIRUSTOTAL API KEY")



def parse_resp(resp):
    """ Parses the response from the requests.gets/posts()
    then returns the data back to the function """
    buf = {}
    for item in resp:
        #print("parse :", buf[item], "ok : ", resp[item])
        buf[item] = resp[item]

    return buf
#바이러스 토탈에게 요청해서 받은 정보 중 악성코드 진단한 밴더 수, 악성코드 종류,  MD5 3개의 값을 리턴해준다.
def get_mal_kind(fileName):
    main = Virustotal()
    # dic1 = main.rscSubmit(fileName)
    var = main.md5(fileName)
    dic = main.rscReport(var)
    print(dic)
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















