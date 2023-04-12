""" 
    导入未知礼物数据
"""

import os
import config
import hashlib


list_file = os.listdir(config.UNKNOWN_GIFT_PATH)


for i in list_file:
    name = i.split('.')[0]
    if len(name) == 32:
        print('>>> 跳过文件：', i, ' 因为没有配置礼物名称')
    else:
        md5 = hashlib.md5(open(config.UNKNOWN_GIFT_PATH + i, 'rb').read()).hexdigest()
        print('>>> 导入礼物：', name, 'md5:', md5)
        with open(config.GIFT_LIST_PATH, 'a',encoding='utf-8') as f:
            f.write('\n' + md5 + ':' + name)
        
        os.remove(config.UNKNOWN_GIFT_PATH + i)
        print('>>> 删除文件：', i)

print('>>> 原始数量：', len(list_file))
print('>>> 导入数量：', len(list_file) - len(os.listdir(config.UNKNOWN_GIFT_PATH)))
print('>>> 剩余数量：', len(os.listdir(config.UNKNOWN_GIFT_PATH)))
print('>>> 导入完成')


    