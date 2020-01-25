import requests as rq
import json


def ParseData(data):
    for dicV in data:
        # print(data.get(dicV))
        # print(type(data.get(dicV)))
        if type(data.get(dicV)) == type(data):
            ParseData(data.get(dicV))
        else:
            print(str(dicV)+" : "+str(data.get(dicV)))


r = rq.get('https://api.github.com/user', auth=('user', 'pass'))
# r.status_code()
# print(r.headers['content-type']
# print(r.json())
if r.status_code == 200:
    data = r.json()
    ParseData(data)

