# 基于DrissionPage实现的获取快手直播间实时礼物、聊天、点赞信息


## 环境要求
建议使用conda虚拟环境部署，python版本要求大于或等于``3.6``

## 环境安装
首先你需要将本项目克隆到你本地。


然后您只需要使用下面命令即可一键安装所需的环境
```bash
pip3 install -r requirements.txt
```
如果pip下载速度较慢，请使用下面这个命令
```
pip3 install -r requirements.txt -i http://pypi.douban.com/simple/
```


## 配置
在使用前，你需要完成一些基本配置

所有配置你只需要在``config.py``文件中完成，如果你不懂任何技术，请不要修改除``config.py``文件外的任何文件。


你主要是需要去配置``LIVE_URL``选项，去指定直播间的地址，配置实例
```py
LIVE_URL = r"https://live.kuaishou.com/u/KPL704668133"
```
上面这个代码我指定了KPL直播间地址。


其次，你需要配置``BROWSER_PATH``选项，该选项需要你指定浏览器可执行文件的路径，在默认的配置中，我使用了``edge``浏览器作为驱动。

你可以配置任何使用``chromium``内核构建的浏览器，例如``Microsoft Edge``或者是``Google Chrome``等。
```py
BROWSER_PATH = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
```

其他选项对于本项目的运行影响不大，你可以看选项上面的注释进行配置

## 运行
如果你完成了上述的配置，使用以下命令进行启动本项目
```bash
python main.py
```

## 未知礼物
由于时效性问题，可能导致一些礼物无法识别，此时，你需要额外配置一些未知的礼物。

程序会将获取到的未知的例如默认存放到``unknow_gift``目录（你可以在``config.py``中修改这个路径），名称为：礼物图片md5.png，你需要将``礼物图片md5``改为礼物真实的名称，例如，原始文件名``580c253e0bd3cc4212f7087d110691ed.png``，你需要改为``粉丝团.png``

最后你需要执行以下命令完成礼物的导入

```shell
python import_git.py
```


## 事件开发
如果你在获取到礼物、收到聊天信息、收到点赞后想实现一些业务流程处理，你需要在``handle.py``中实现。

该文件中共实现了三个方法，分别为``message``、``like``、``gift``分别代表了``消息``、``点赞``、``礼物``

代码如下
```py

""" 
    收到弹幕消息会调用这个函数
"""
def message(username,text):
    pass


""" 
    收到点赞消息会调用这个函数
"""
def like(username):
    pass

""" 
    收到礼物消息会调用这个函数，如果未知礼物，gift_name 为 None
"""
def gift(username,gift_name):
    pass

```

``message``函数会传入两个参数，分别为``username``和``text``，顾名思义``username``就是谁发的消息，``text``就是发的什么消息。

``like``函数会传入一个参数，为``username``，就是谁点了赞。

``gift``函数会传入两个参数，为`username`和``gift_name``，``username``是送礼物的人，``gift_name``就是礼物名称，如果遇到了未知礼物，则传入的为None




## 郑重提示
请勿将 本项目 应用到任何可能会违反法律规定和道德约束的工作中，请友善使用 本项目，遵守蜘蛛协议，不要将 本项目 用于任何非法用途。如您选择使用 本项目 即代表您遵守此协议，作者不承担任何由于您违反此协议带来任何的法律风险和损失，一切后果由您承担。


## 作者信息
QQ：3139505131

WECHAT：laravel_debug

E-Mail：wlkjyy@vip.qq.com


## 后言

参考文献：
    
- http://g1879.gitee.io/drissionpagedocs/
- https://github.com/wlkjyh/kuaishouLiwu



开发不易，如果本项目对你有用，让我喝杯咖啡吧。

