import init
from utils import *
import time
import threading
import handle


while True:    
    if has_login():
        break

    
    if running.IS_QRCODE_START == False:
        start_qrcode_login()
        running.IS_QRCODE_START = True
    print('>>> 未检测到登录状态，将在10秒后重试')
    time.sleep(10)

while True:
    if '请求过快，请稍后重试' in running.DRIVER.html:
        print('>>> [ERROR:1] 正在尝试刷新页面')
        running.DRIVER.get(config.LIVE_URL)
    else:
        print('>>> 已完成。')
        break

""" 
    加载礼物列表
"""
print('>>> 开始加载礼物信息')
try:
    with open(config.GIFT_LIST_PATH, 'r', encoding='utf-8') as f:
        gift_list = f.readlines()
        gift_list = [i.replace('\n', '') for i in gift_list]
        gift_list = [i.split(':') for i in gift_list]
        gift_list = {i[0]:i[1] for i in gift_list}
except:
    print('>>> 无法加载礼物信息，请检查相关配置是否正确')
    exit(0)
running.GIFT_LIST = gift_list
print('>>> 礼物信息加载成功')


frist_length = 0
print('>>> 开始监听弹幕')
while True:
    try:
        chat_history_container = running.DRIVER.ele('.chat-history').ele('.history')

        chat_info = chat_history_container.eles('.chat-info')
        chat_info_length = len(chat_info)
        if chat_info_length == frist_length:
            continue
        else:
            frist_length = chat_info_length

        last_chat_info = chat_info[-1]
        type_text = last_chat_info.text
        # 先判断类型
        if '点亮了' in type_text:
            username = type_text.split('点亮了')[0]
            print(f'>>>>> 用户名： {username} 点赞了。')
            handle.like(username)
        elif '送' in type_text:
            try:
                username = type_text.split('送')[0]

                liwu_name = last_chat_info.ele('.gift-img').attrs['src']
                thread = threading.Thread(target=queue_get_gift_name, args=(liwu_name,username))
                thread.setDaemon(True)
                thread.start()

            except Exception as e:
                print(e)
                continue
        elif '：' in type_text:
            split = type_text.split('：')
            username = split[0]
            if username == '快手平台账号' and config.IS_IGNORE_OFFICIAL == False:
                continue
            send_text = split[1]
            if send_text == '请求过快，请稍后重试':
                print('>>> 被系统风控了，现在需要等待10秒后继续')
                time.sleep(10)

            print(f'>>>>> 用户名：{username} 发送了弹幕   {send_text}')
            handle.message(username, send_text)
        

        if frist_length > config.REFRESH_MESSAGE_NUMBER:
            print('>>> 弹幕数量过多，正在尝试刷新页面。')
            frist_length = 0
            running.DRIVER.get(config.LIVE_URL)


    except Exception as e:
        print('>>> [ERROR:2] 程序出现错误，尝试刷新页面后重试')
        print(e)
        running.DRIVER.get(config.LIVE_URL)
        continue
