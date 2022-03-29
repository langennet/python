#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import base64


apikey = "xxxx"  # 这里填入hunter个人中心的key


def search(keywords):
    print("searching:"+keywords.strip("\n"),end="\r")
    keywords = base64.urlsafe_b64encode(keywords.strip("\n").encode("utf-8"))
    page = 0
    num = 0
    while True:
        try:
            page += 1
            url = "https://hunter.qianxin.com/openApi/search?api-key={}&search={}&page={}&page_size=100&is_web=1&status_code=200".format(apikey, keywords.decode(), page)
            r = requests.get(url, timeout=3)
            res = json.loads(r.text)
            loadurl = res['data']['arr']
            
            for i in loadurl:
                
                if len(i['company']) >0:
                    print("\033[42m"+i['url']+"\033[0m",i['company'],i['ip'])
                    with open("hunterurl.txt", "a+") as f:
                        num += 1
                        str1 = i['company']+","+i['url'] +","+i['ip']
                        f.write(str1 + "\n")
            
        except Exception as e:
            
            break

if __name__ == '__main__':
    f = open('ip.txt','r')
    r = f.readlines()
    f.close()
    for keyword in r:
       
        search(keyword)
    