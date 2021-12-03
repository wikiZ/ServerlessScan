#!/usr/bin/env python
# encoding: utf-8
'''
@author: 风起
@contact: onlyzaliks@gmail.com
@File: test.py
@Time: 2021/11/30 14:15
'''
import grequests


def main():
    serverless = ["https://service-eiqw47lb-xxxxxx.cd.apigw.tencentcs.com",
                  "https://service-9steegcp-xxxxxx.sh.apigw.tencentcs.com"]
    resp, num = [], 0
    port_one = [22, 53, 80, 81, 82, 83, 111, 9096, 9291, 9080, 6379, 5900, 9090, 443]
    port_two = [8088, 8080, 4566, 6666, 10001, 2443, 3306, 3389, 7001, 9099, 135, 23]
    try:
        ip = input("\033[31;32mPlease Input IP Address:\033[0m")
        print("")
        for server in serverless:
            num += 1
            port_list = port_one if num == 1 else port_two
            for port in port_list:
                serverless_one = f"{server}?ip={ip}&port={port}"
                resp.append(grequests.get(
                    serverless_one,
                    timeout=5
                )
            )
            res_list = grequests.map(resp)
            for res in res_list:
                if res.text != "null" and res.text.find("errorCode") == -1:
                    print('[+]{}/tcp OPEN'.format(res.text))
    except Exception as err:
        print(err)
        pass


if __name__ == '__main__':
    main()
