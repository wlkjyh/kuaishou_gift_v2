""" 
    处理一些消息，你可以在这里实现你的业务逻辑
"""


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