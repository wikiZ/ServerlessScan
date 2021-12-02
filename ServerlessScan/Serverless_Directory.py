# -*- coding: utf8 -*-
import requests

def main_handler(event, context):
    headers=event["headers"]
    url=event["queryString"]["url"]
    path = event["queryString"]["path"]
    crake_url=str(url+path)
    try:
        r = requests.get(crake_url,timeout=5,headers=headers,verify=False)
        status = r.status_code
    except Exception:
        status = None
        pass

    return status,crake_url