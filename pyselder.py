import os
import requests
import threading

def getImg(keyword, localPath, imgCont=50):
    params = []
    for i in range(30, imgCont+90, 30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': 'rj',
            "ie": "utf-8",
            'word': keyword,
            'pn': i
        })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        while 1:
            try:
                urls.append(requests.get(url, params=i).json(strict=False).get('data'))
                break
            except:
                print("连接超时，正在重试...")
    if not os.path.exists(localPath):
        os.makedirs(localPath)
    x = 1
    for imgs in urls:
        for img in imgs:
            if img.get('thumbURL'):
                print('正在下载%s%d：%s' % (keyword, x, img.get('thumbURL')))
                while 1:
                    try:
                        ir = requests.get(img.get('thumbURL'))
                        break
                    except:
                        print("连接超时，正在重试...")
                f = open(localPath + r'\\' + '%d.%s' % (x,img.get("type")), 'wb')
                f.write(ir.content)
                f.close()
                x += 1
                if x > imgCont:
                    return
            else:
                print('图片链接不存在')

if __name__ == "__main__":

    keyword = input("输入图片关键字：")
    pnum = int(input("输入爬取图片数量："))
    threading.Thread(target=getImg(keyword, os.getcwd()+"\\img\\"+keyword, pnum)).start()
    print("下载完成！")
