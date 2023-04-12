
# 直播间地址
LIVE_URL = r"https://live.kuaishou.com/u/KPL704668133"

# 浏览器可执行文件路径，支持chrome、edge等chromium内核浏览器
BROWSER_PATH = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# 是否忽略官方弹幕
IS_IGNORE_OFFICIAL = True


# 礼物列表路径
""" 
    如果有未知类型的礼物，你需要在这个文件里面添加这个例如，格式为 图片md5值:礼物名称
"""
GIFT_LIST_PATH = r'./gift.txt'


# 未知礼物存储路径，你需要将里面的文件名改为礼物名称，然后运行python import_gift.py即可导入新礼物
UNKNOWN_GIFT_PATH = r'./unknown_gift/'

# 处理多少条弹幕后刷新页面（防止弹幕过多导致程序卡死）
REFRESH_MESSAGE_NUMBER = 1000


