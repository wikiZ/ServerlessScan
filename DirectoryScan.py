#!/usr/bin/env python
# encoding: utf-8
'''
@author: 风起
@contact: onlyzaliks@gmail.com
@File: scan.py
@Time: 2021/11/29 17:48
'''
import random
import requests


def dict_read(dict_file, num):
    dict_list = []
    with open(dict_file, "r", encoding='utf-8') as ip_text:
        lines = ip_text.readlines()[:7] if num == 1 else ip_text.readlines()[7:]
        for line in lines:
            dict_list.append(line.strip("\n"))
    return dict_list


def main():
    from get_ua_header import UA
    number = 0
    severless = ["https://service-7pdfhbye-1259312707.gz.apigw.tencentcs.com",
                 "https://service-lz5qmdaf-1259312707.sh.apigw.tencentcs.com"]
    try:
        url = input("\033[31;32mplease input url:\033[0m")
        dict_file_path = input("\033[32;32mplease input crash dict path:\033[0m")
        print("")
        for server in severless:
            number += 1
            for path in dict_read(dict_file_path, number):
                headers = {
                    "User-Agent": random.choice(UA),
                }
                serverless_one = f"{server}?path={path}&url={url}"
                r = requests.get(serverless_one, headers=headers)
                print(r.text)

    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
