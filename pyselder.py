import os
import requests
import threading
import time


def getImg(keyword, localPath, imgCont=50):
    params = []
    for i in range(30, imgCont+90, 30):
        params.append({
            'tn': 'resultjson_com',
            'ipn' : 'rj',
            "ie" : "utf-8",
            'word': keyword,
            'pn': i
        })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        urls.append(requests.get(url, params=i).json(strict=False).get('data'))
    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)
    x = 1
    for imgs in urls:
        for img in imgs:
            if img.get('thumbURL'):
                print('正在下载%s%d：%s' % (keyword, x, img.get('thumbURL')))
                ir = requests.get(img.get('thumbURL'))
                f = open(localPath + r'\\' + '%d.jpg' % x, 'wb')
                f.write(ir.content)
                f.close()
                x += 1
                if x > imgCont:
                    return
            else:
                print('图片链接不存在')


if __name__ == "__main__":

    keywords = set()
    # while keywords.__len__() < 3:
    keyword = input("输入图片关键字：")
    if keyword in keywords:
        print("%s 元素已存在！" % keyword)
    else:
        keywords.add(keyword)
    imgcont = int(input("输入爬取张数："))
    for cls in keywords:
        threading.Thread(target=getImg(cls, os.getcwd()+"\\"+cls,imgcont)).start()
    print("下载完成！")
    os.system("pause")