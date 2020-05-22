'''
Project: Bili-Luckydog
BiliBili�������齱 (������,�ظ���Ч)
Coder: Alkey Sheng [i.2017.work]
2020.5.21
'''

import requests
import random
import time
import datetime

# setting  ����""
# ----------------------------------------------------------
bvid = ""  # ��ƵBV��   ��: "BV1NZ4y147X6"
num = ""   # �齱����   ��: "1"
# ----------------------------------------------------------

# ��BվBV��ת��ΪAV��


def getAid(bvid):
    root = requests.get(
        "https://api.bilibili.com/x/web-interface/view?bvid={}".format(bvid)).json()
    aid = root["data"]["aid"]
    return aid

# ��ȡĳһҳJSON


def getJson(aid, page=1):
    url = "http://api.bilibili.com/x/v2/reply?jsonp=jsonp&;pn={}&type=1&oid={}"
    re = requests.get(url.format(page, aid))
    root = re.json()
    return root


# ��ȡJSON��������ӵ��б�
def addLi(root, li):
    members = root["data"]["replies"]
    for member in members:
        uname = member["member"]["uname"]
        message = member["content"]["message"]
        li.append([uname, message])
        time.sleep(0.01)
        print("{:>3d}: {}".format(len(li), uname))


# ������齱
def getDog(n, li):
    lucky_indexs = set()
    while len(lucky_indexs) < n:
        randomNum = random.randint(0, len(li)-1)
        lucky_indexs.add(randomNum)
    return lucky_indexs


if bvid == "":
    bvid = input("��ƵBV�� ��: BV1NZ4y147X6\n")
if num == "":
    num = input("�齱���� ��: 1\n")

aid = getAid(bvid)
n = int(num)
li = []


print("members:\n-----------------------------")
page_1 = getJson(aid)
pages = (page_1["data"]["page"]["count"]) // (
    page_1["data"]["page"]["size"]) + 1
# print(pages)
for i in range(1, pages+1):
    root = getJson(aid, i)
    addLi(root, li)


print("-----------------------------")
time.sleep(1)
lucky_indexs = list(getDog(n, li))
for i in range(n):
    print("\n", " Luckydog:", li[lucky_indexs[i]][0],
          "\n  comment:", li[lucky_indexs[i]][1])
    time.sleep(1)

print("\nDate-Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
