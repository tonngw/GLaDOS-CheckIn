from json import dumps
from time import sleep
from logger import logger
from requests import post, get


def send_msg_serverJ(SendKey, title, Text):

    if not SendKey:
        # 无SendKey则拦截推送
        return 'Sever酱: 未配置SendKey，无法进行消息推送。'
    logger.info('========================================')
    logger.info('Sever酱: 开始推送消息！')
    Text = Text.replace('\n', '\n\n')
    url = f'https://sctapi.ftqq.com/{SendKey}.send'
    data = {'title': title, 'desp': Text, 'channel': 9}
    rsp = post(url=url, data=data)
    pushid = rsp.json()['data']['pushid']
    readkey = rsp.json()['data']['readkey']
    state_url = f'https://sctapi.ftqq.com/push?id={pushid}&readkey={readkey}'

    count = 1
    while True:
        status_rsp = get(url=state_url)
        result = status_rsp.json()['data']['wxstatus']
        logger.info(f'查询消息推送是否成功ing : {count}')

        if result:
            return '消息推送成功！'
        elif count >= 60:   # 防止程序一直运行
            return '程序运行结束！推送结果未知！'
        count += 1
        sleep(1)

def send_msg_pushplus(token, title, Text):

    if not token:
        # 无token则拦截推送
        return 'PushPlus: 未配置token，无法进行消息推送。'
    logger.info('========================================')
    logger.info('PushPlus: 开始推送消息！')
    url = 'http://www.pushplus.plus/send/'
    headers = {'Content-Type':'application/json'}
    data = {
        "token": token,
        "title": title,
        "content": Text,
        "template": "txt",
        "channel": "wechat"
    }
    data = dumps(data).encode(encoding='utf-8')
    rsp = post(url=url, data=data, headers=headers)
    return rsp.json()['msg']