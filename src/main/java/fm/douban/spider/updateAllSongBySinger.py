import pymongo
import requests
import time


print()
header = {}
header['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
header["Referer"] = "https://fm.douban.com/"

cookies = 'bid=Ixdu8ZtzEXw; gr_user_id=68d4e16d-24f6-45a1-bad5-e354cbb2dd56; _ga=GA1.2.1510717963.1638194508; douban-fav-remind=1; ll="118099"; viewed="6839186_26259017"; dbcl2="235075073:+t2Fhdku5f4"; _pk_id.100002.f71f=bf29fd269589323f.1642832705.2.1646031969.1642832716.; _pk_ref.100002.f71f=%5B%22%22%2C%22%22%2C1646031969%2C%22https%3A%2F%2Fgraph.qq.com%2F%22%5D; push_noty_num=0; push_doumail_num=0; __utmv=30149280.23507; _gid=GA1.2.1831699055.1646149114; ck=Jw3S; ap_v=0,6.0; __utma=30149280.1510717963.1638194508.1646031996.1646287191.5; __utmc=30149280; __utmz=30149280.1646287191.5.5.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.f71f=%5B%22%22%2C%22%22%2C1646287202%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.100001.f71f=97dee38d0a3f8eaf.1642772724.21.1646287624.1646204330.'
header["cookie"] = cookies

client = pymongo.MongoClient('mongodb://admin:zxc123@39.101.185.54:27017/')

db = client['practice']

singers = db['singer']

result = singers.find()

songs = db["song"]

olddit = {}

def spider(url):
    data = requests.get(url, headers=header)
    data = data.json()
    return data

def indb(dit):
    olddit["_id"] = dit["_id"]
    song = songs.find_one(olddit)
    if(song==None):
        songs.insert_one(newdit)
    else:
        myquery = {"_id": dit["_id"]}
        newvalues = {"$set": newdit}
        songs.update_one(myquery, newvalues)

urls = []
i1 = 1
for item in result:
    url = "https://fm.douban.com/j/v2/artist/"+str(item["_id"])+"/"
    data = spider(url)
    print(i1)
    i1 += 1
    try:
        list = data["songlist"]["songs"]
        for i in list:
            newdit = {}
            newdit["_id"] = i["sid"]
            newdit["name"] = i["title"]
            newdit["cover"] = i["picture"]
            newdit["beSpidered"] = False
            newdit["gmtCreated"] = time.strftime('%Y-%m-%dT%X.827+00:00', time.localtime(time.time()))
            newdit["gmtModified"] = time.strftime('%Y-%m-%dT%X.827+00:00', time.localtime(time.time()))
            newdit["url"] = i["url"]
            lis = []
            for j in i["singers"]:
                lis.append(j["id"])
            newdit["singerIds"] = lis
            newdit["publishedDate"] = i["public_time"]
            newdit["like"] = int(i["like"])
            indb(newdit)
    except KeyError:
        continue
