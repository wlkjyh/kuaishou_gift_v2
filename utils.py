from DrissionPage import ChromiumPage
import running
import config
import re
import base64
import os
import requests
import hashlib
import handle

def has_login():
    html = running.DRIVER.html
    if '登录发弹幕，参与主播互动' in html:
        return False
    else:
        return True
    

def start_qrcode_login():
    try:
        running.DRIVER.ele('.login').click()
        qrcode_tag = running.DRIVER.ele('xpath:html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div/img/@src')
        qrcode_tag = str(qrcode_tag)
        qrcode_url = re.findall(r'src=\'(.*?)\'', qrcode_tag)[0].replace('data:image/png;base64,', '')
    
        with open('qrcode.png', 'wb') as f:
            f.write(base64.b64decode(qrcode_url))
        os.system('start qrcode.png')
        print('>>> 二维码获取成功，请扫描二维码后继续')
    except:
        print('>>> 二维码获取失败，请手动在浏览器窗口扫码')


""" 
    异步获取礼物名称，因为获取礼物名称需要发送请求，所以需要异步获取
"""
def queue_get_gift_name(url,username):
    r = requests.get(url).content
    md5 = hashlib.md5(r).hexdigest()
    if md5 in running.GIFT_LIST:
        gift_name = running.GIFT_LIST[md5]
        print(f'>>>>> 用户名： {username} 送出了 {gift_name} 。')
        handle.gift(username, gift_name)

    else:

        storage_file = config.UNKNOWN_GIFT_PATH + md5 + '.png'
        if os.path.exists(storage_file) == False:
            with open(storage_file, 'wb') as f:
                f.write(r)

        
        print(f'>>>>> 用户名： {username} 送出了 未知礼物 。')
        handle.gift(username, None)


    pass