oo0o ='''
cron: 30 */30 8-22 * * *
new Env('百事通阅读');
活动入口：http://zyyegr.dhreoejerhjfb.cn/?fid=7416227&st=2&rd=5966&t=1726811620
使用方法：
1.入口,WX打开：http://zyyegr.dhreoejerhjfb.cn/?fid=7416227&st=2&rd=5966&t=1726811620
'''
'''
请先尝试手动阅读几篇在使用脚本
请先尝试手动阅读几篇在使用脚本
请仔细阅读下面的使用方式：
1.入口1,http://zyyegr.dhreoejerhjfb.cn/?fid=7416227&st=2&rd=5966&t=1726811620
入口无法打开可以尝试到浏览器打开
入口无法打开可以尝试到浏览器打开
2.电脑微信无法打开或者无法登录，无法抓包的解决办法（仅电脑）
2.1.fiddler抓包，打开fiddler过滤器功能，找到‘请求标头’这一项下的设置请求标头
2.2.本行第一个框输入User-Agent 
2.3第二个框输入Mozilla/5.0 (Linux; Android 13; M2104K10AC Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110017 MMWEBSDK/20231002 MMWEBID/2545 MicroMessenger/8.0.43.2480(0x28112BE1) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64
2.4.点击刚才复制的链接，正常抓包。
2.5抓包的任意ltai.litianwm.com域名接口headers中的Token参数
3.青龙菜单项《配置文件》，添加本脚本环境变量
填写变量参数时为方便填写可以随意换行
单账户：export bstyd="[{'name':'备注名','Token': 'xxxx-xxxx-xxx-xxx-xxx','key':'xxxxxxx','uids':'xxxxxxx'}]"
多账户：export bstyd="[
{'name':'备注名','Token': 'xxxx-xxxx-xxx-xxx-xxx','key':'xxxxx','uids':'xxxxxxx'},
{'name':'备注名','Token': 'xxxx-xxxx-xxx-xxx-xxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','Token': 'xxxx-xxxx-xxx-xxx-xxx','key':'xxxxxxx','uids':'xxxxxxx'}
]"
参数说明：
name:备注名随意填写
Token:打开活动入口，抓包的任意接口headers中的Token参数
key：每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送应用后，会在推送管理后台(https://wxpusher.zjiecode.com/admin/main)的'用户管理-->用户列表'中显示
用户在推送页面点击’我的-->我的UID‘也可以获取

4.青龙菜单项《配置文件》，添加本脚wxpusher环境变量(不需要重复添加)
export push_config="{'printf':0,'threadingf':1,'threadingt':3,'appToken':'xxxx'}"
参数说明：
printf:0是不打印调试日志，1是打印调试日志
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
threadingt:并行运行时每个账号的间隔时间默认3s
appToken 这个是填wxpusher的appToken,wxpusher如何使用可以百度
5.脚本运行时，检测到需要手动阅读的文章，将会推送到你的微信（需要填写好推送参数），你需要手动点击推送，阅读文章，这时脚本会继续运行，否则60秒后将检查超时，停止脚本。
定时运行每半个小时一次
'''#line:47
import requests #line:48
import re #line:49
import random #line:50
import os #line:51
import threading #line:52
import json #line:53
import hashlib #line:54
import time #line:55
from urllib .parse import urlparse ,parse_qs ,quote #line:56
checkDict ={'ischeck':['检测标注','检测标注请勿修改']}#line:59
push_num =[-1 ]#line:60
def getmsg ():#line:61
    global checkDict #line:62
    OOOOOO0OO0O000000 ='v1.0'#line:63
    try :#line:64
        OOO0000O000OOOO00 ='http://175.24.153.42:8881/getmsg'#line:65
        O0O00OOOO000OO0O0 ={'type':'yuanbao'}#line:66
        O0OOO00O000O0OO0O =requests .get (OOO0000O000OOOO00 ,params =O0O00OOOO000OO0O0 ,timeout =2 )#line:67
        OOOO00000OOOO0OOO =O0OOO00O000O0OO0O .json ()#line:68
        OO0O00O0O00OOOO00 =OOOO00000OOOO0OOO .get ('version')#line:69
        O00O0OO0OOOO0OO00 =OOOO00000OOOO0OOO .get ('gdict')#line:70
        OO0OO00O00OO000OO =OOOO00000OOOO0OOO .get ('gmmsg')#line:71
        print ('系统公告:',OO0OO00O00OO000OO )#line:72
        print (f'最新版本{OO0O00O0O00OOOO00},当前版本{OOOOOO0OO0O000000}')#line:73
        if OOOOOO0OO0O000000 !=OO0O00O0O00OOOO00 :#line:74
            print ('版本不一致，可能要更新脚本了')#line:75
        print (f'系统的公众号字典{len(O00O0OO0OOOO0OO00)}个:{O00O0OO0OOOO0OO00}')#line:76
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:77
        checkDict ={}#line:78
        for O0OO0OOOOO0O0O0O0 in O00O0OO0OOOO0OO00 :#line:79
            checkDict .update ({O0OO0OOOOO0O0O0O0 :['','']})#line:80
    except Exception as O00O0O000OO0OOO0O :#line:81
        print (O00O0O000OO0OOO0O )#line:82
        print ('公告服务器异常')#line:83
def push (OO0O00O0O000O0000 ,OO0O00OO0OOOO0O00 ,O0O0000O0OO0OO00O ,O0O000OO00OOOOOO0 ,O000O0O00000OO0OO ,O000OO000000O00OO ):#line:84
    O0O0O0OOOOOOO0OOO ='''
<body onload="window.location.href='LINK'">
<p>TEXT</p><br>
<p><a href="http://175.24.153.42:8882/lookstatus?key=KEY&type=TYPE">查看状态</a></p><br>
</body>
    '''#line:90
    O0O00OO0OO00O00OO =O0O0O0OOOOOOO0OOO .replace ('TITTLE',OO0O00O0O000O0000 ).replace ('LINK',OO0O00OO0OOOO0O00 ).replace ('TEXT',O0O0000O0OO0OO00O ).replace ('TYPE',O0O000OO00OOOOOO0 ).replace ('KEY',O000OO000000O00OO )#line:92
    O0O00O00OOO0000O0 ={"appToken":appToken ,"content":O0O00OO0OO00O00OO ,"summary":OO0O00O0O000O0000 ,"contentType":2 ,"uids":[O000O0O00000OO0OO ]}#line:99
    OO000OOOOOOOOOOOO ='http://wxpusher.zjiecode.com/api/send/message'#line:100
    try :#line:101
        O0O00O0O000OO0OO0 =requests .post (url =OO000OOOOOOOOOOOO ,json =O0O00O00OOO0000O0 ).text #line:102
        print ('推送结果：',O0O00O0O000OO0OO0 )#line:103
        return True #line:104
    except Exception as O0O00000O0OOOOO00 :#line:105
        print ('推送失败！')#line:106
        print ('推送结果：',O0O00000O0OOOOO00 )#line:107
        return False #line:108
def getinfo (OOO0OOO0000O00O0O ):#line:109
    try :#line:110
        OOOO0OOO0OO0OO00O ={'Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090b19) XWEB/9193 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language':'zh-CN,zh;q=0.9','Cookie':'rewardsn=; wxtokenkey=777; devicetype=Windows11x64; version=73020b18; lang=zh_CN;',}#line:117
        O0OO0OO0O0OO0O00O =requests .get (OOO0OOO0000O00O0O ,headers =OOOO0OOO0OO0OO00O )#line:118
        O00O00O0O000OOO00 =re .sub ('\s','',O0OO0OO0O0OO0O00O .text )#line:119
        OOO0OOO00OO0OO00O =re .findall ('varbiz="(.*?)"\|\|',O00O00O0O000OOO00 )#line:120
        if OOO0OOO00OO0OO00O !=[]:#line:121
            OOO0OOO00OO0OO00O =OOO0OOO00OO0OO00O [0 ]#line:122
        if OOO0OOO00OO0OO00O ==''or OOO0OOO00OO0OO00O ==[]:#line:123
            if '__biz'in OOO0OOO0000O00O0O :#line:124
                OOO0OOO00OO0OO00O =re .findall ('__biz=(.*?)&',OOO0OOO0000O00O0O )#line:125
                if OOO0OOO00OO0OO00O !=[]:#line:126
                    OOO0OOO00OO0OO00O =OOO0OOO00OO0OO00O [0 ]#line:127
        O0O0OOOO00OOOOOO0 =re .findall ('varnickname=htmlDecode\("(.*?)"\);',O00O00O0O000OOO00 )#line:128
        if O0O0OOOO00OOOOOO0 !=[]:#line:129
            O0O0OOOO00OOOOOO0 =O0O0OOOO00OOOOOO0 [0 ]#line:130
        O0000OO0000OOO000 =re .findall ('varuser_name="(.*?)";',O00O00O0O000OOO00 )#line:131
        if O0000OO0000OOO000 !=[]:#line:132
            O0000OO0000OOO000 =O0000OO0000OOO000 [0 ]#line:133
        OOO000OOO0O00O00O =re .findall ("varmsg_title='(.*?)'\.html\(",O00O00O0O000OOO00 )#line:134
        if OOO000OOO0O00O00O !=[]:#line:135
            OOO000OOO0O00O00O =OOO000OOO0O00O00O [0 ]#line:136
        OOO00O000O0O0OOO0 =re .findall ("varoriCreateTime='(.*?)';",O00O00O0O000OOO00 )#line:137
        if OOO00O000O0O0OOO0 !=[]:#line:138
            OOO00O000O0O0OOO0 =OOO00O000O0O0OOO0 [0 ]#line:139
        O0O0OO00000OOO00O =re .findall ("varcreateTime='(.*?)';",O00O00O0O000OOO00 )#line:140
        if O0O0OO00000OOO00O !=[]:#line:141
            O0O0OO00000OOO00O =O0O0OO00000OOO00O [0 ]#line:142
            O0O0OO00000OOO00O =O0O0OO00000OOO00O [:-5 ]+' '+O0O0OO00000OOO00O [-5 :]#line:143
        O0OO0O000OOOOO0O0 =f'公众号唯一标识：{OOO0OOO00OO0OO00O}|文章:{OOO000OOO0O00O00O}|作者:{O0O0OOOO00OOOOOO0}|账号:{O0000OO0000OOO000}|文章时间戳:{OOO00O000O0O0OOO0}|文章时间:{O0O0OO00000OOO00O}'#line:144
        print (O0OO0O000OOOOO0O0 )#line:145
        return O0O0OOOO00OOOOOO0 ,O0000OO0000OOO000 ,OOO000OOO0O00O00O ,O0OO0O000OOOOO0O0 ,OOO0OOO00OO0OO00O ,OOO00O000O0O0OOO0 ,O0O0OO00000OOO00O #line:146
    except Exception as O0O0OOOOO00OOO00O :#line:147
        print (O0O0OOOOO00OOO00O )#line:148
        print ('异常')#line:149
        return False #line:150
class WXYD :#line:151
    def __init__ (OOOO00OO0OO0000OO ,OOO000O000O00O0O0 ,O0O0OOO000OOO0000 ):#line:152
        OOOO00OO0OO0000OO .indexs =str (O0O0OOO000OOO0000 +1 )#line:153
        OOOO00OO0OO0000OO .name =OOO000O000O00O0O0 ['name']#line:154
        OOOO00OO0OO0000OO .key =OOO000O000O00O0O0 ['key']#line:155
        OOOO00OO0OO0000OO .uids =OOO000O000O00O0O0 ['uids']#line:156
        OOOO00OO0OO0000OO .count =0 #line:157
        OOOO00OO0OO0000OO .User_Agent ='Mozilla/5.0 (Linux; Android 13; M2104K10AC Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110017 MMWEBSDK/20231002 MMWEBID/2545 MicroMessenger/8.0.43.2480(0x28112BE1) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64'#line:158
        OOOO00OO0OO0000OO .hostUrl =OOOO00OO0OO0000OO .getAuthUrl3 ()#line:159
        OOOO00OO0OO0000OO .headers ={'Host':'ltai.litianwm.com','Connection':'keep-alive','User-Agent':OOOO00OO0OO0000OO .User_Agent ,'Token':OOO000O000O00O0O0 ['Token'],'Content-Type':'application/json','Accept':'*/*','Origin':f'http://{OOOO00OO0OO0000OO.hostUrl[1]}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':f'http://{OOOO00OO0OO0000OO.hostUrl[1]}/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9',}#line:174
    def printjson (OO00000000OOOO0O0 ,O0OOOO0000OOO0OOO ):#line:175
        if printf ==0 :#line:176
            return False #line:177
        print (OO00000000OOOO0O0 .name ,O0OOOO0000OOO0OOO )#line:178
    def setstatus (O0OO0OOO00OOO0000 ):#line:179
        try :#line:180
            OOO0OOO0OO00O0O00 ='http://175.24.153.42:8882/setstatus'#line:181
            OO00OO0000O0000O0 ={'key':O0OO0OOO00OOO0000 .key ,'type':'yuanbao','val':'1','ven':oo0o }#line:182
            OOO00OO0O0O0OOO00 =requests .get (OOO0OOO0OO00O0O00 ,params =OO00OO0000O0000O0 ,timeout =5 )#line:183
            print (O0OO0OOO00OOO0000 .name ,OOO00OO0O0O0OOO00 .text )#line:184
            if '无效'in OOO00OO0O0O0OOO00 .text :#line:185
                exit (0 )#line:186
        except Exception as OO00000O000OO0OOO :#line:187
            print (O0OO0OOO00OOO0000 .name ,'设置状态异常')#line:188
            print (O0OO0OOO00OOO0000 .name ,OO00000O000OO0OOO )#line:189
            return 99 #line:190
    def getstatus (O000O0O0000O0O0OO ):#line:191
        try :#line:192
            O0O000O0O0O00OOOO ='http://175.24.153.42:8882/getstatus'#line:193
            O00000OOO000O00O0 ={'key':O000O0O0000O0O0OO .key ,'type':'yuanbao'}#line:194
            OOOOO0OO000O000OO =requests .get (O0O000O0O0O00OOOO ,params =O00000OOO000O00O0 ,timeout =3 )#line:195
            return OOOOO0OO000O000OO .text #line:196
        except Exception as OOO000OOOOOOOOO0O :#line:197
            print (O000O0O0000O0O0OO .name ,'查询状态异常',OOO000OOOOOOOOO0O )#line:198
            return False #line:199
    def getAuthUrl3 (OO0O00O000O0O000O ):#line:200
        OO0000O000OOO0000 ='https://ltai.litianwm.com/v1/user/getAuthUrl3'#line:201
        OO00O0000O0O0O0O0 ={'Host':'ltai.litianwm.com','Connection':'keep-alive','Accept':'application/json, text/javascript, */*; q=0.01','User-Agent':OO0O00O000O0O000O .User_Agent ,'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Origin':'https://weixin.litianwm.cn','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://weixin.litianwm.cn/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9',}#line:215
        OOO00O0O0OO00O0O0 =requests .post (OO0000O000OOO0000 ,headers =OO00O0000O0O0O0O0 ,data ='url=https%3A%2F%2Fweixin.litianwm.cn%2Fwxlogin.html&st=2')#line:216
        if 'success'in OOO00O0O0OO00O0O0 .text :#line:217
            O0OOOOOO000O000O0 =OOO00O0O0OO00O0O0 .json ()#line:218
            OO00OOO0000OOO0O0 =O0OOOOOO000O000O0 ['data']#line:219
            OOO000O0OOOOOO00O =urlparse (OO00OOO0000OOO0O0 )#line:220
            OOOOO00OOO000O000 =parse_qs (OOO000O0OOOOOO00O .query )#line:221
            OO000OO00OOO0OO0O =OOOOO00OOO000O000 .get ('redirect_uri')[0 ]#line:222
            O0O00O00O0OO00OO0 =urlparse (OO000OO00OOO0OO0O )#line:223
            OO0O0OOO00O0O0O0O =parse_qs (O0O00O00O0OO00OO0 .query )#line:224
            O00OOOOOOOO0OO000 =OO0O0OOO00O0O0O0O .get ('jpurl')[0 ]#line:225
            OO0OOO0O000OOOO0O =urlparse (O00OOOOOOOO0OO000 ).netloc #line:226
            OO00OO0O0O000OOOO =quote ('http://'+OO0OOO0O000OOOO0O +'/',safe ='')#line:227
            return OO00OO0O0O000OOOO ,OO0OOO0O000OOOO0O #line:228
        else :#line:229
            print (OOO00O0O0OO00O0O0 .text )#line:230
            return 'http%3A%2F%2F4eky9f.whnxvxnxm.cn%2F','4eky9f.whnxvxnxm.cn'#line:231
    def amountValue (OOO0OO0O0OOOO0O00 ):#line:232
        O0O0OO0000O00OOOO ='https://ltai.litianwm.com/v1/user_center/amountValue'#line:233
        OO0OOO0OOO000OO00 =requests .get (O0O0OO0000O00OOOO ,headers =OOO0OO0O0OOOO0O00 .headers )#line:234
        if 'success'in OO0OOO0OOO000OO00 .text :#line:235
            OOO0O0OOO000O0O00 =OO0OOO0OOO000OO00 .json ()#line:236
            OO0OOOOO0OOO0000O =OOO0O0OOO000O0O00 ['data']['amount']#line:237
            print (OOO0OO0O0OOOO0O00 .name ,f'剩余{OO0OOOOO0OOO0000O}元')#line:238
        else :#line:239
            print (OO0OOO0OOO000OO00 .text )#line:240
            return False #line:241
    def readinfo (O0OOO0O00OOO00OO0 ):#line:242
        OO00O0O00OO0OOOO0 ='https://ltai.litianwm.com/v1/task_center/read'#line:243
        O0O00OO0O000O0O0O =requests .get (OO00O0O00OO0OOOO0 ,headers =O0OOO0O00OOO00OO0 .headers )#line:244
        if 'success'in O0O00OO0O000O0O0O .text :#line:245
            O00OO0O0OOO0O0000 =O0O00OO0O000O0O0O .json ()#line:246
            O0OOO0O0O0O0O0O0O =O00OO0O0OOO0O0000 ['data']['rounds_num']#line:247
            O0O00O00O0O0OOOO0 =O00OO0O0OOO0O0000 ['data']['income']#line:248
            print (O0OOO0O00OOO00OO0 .name ,f'今日已阅读{O0OOO0O0O0O0O0O0O}轮，阅读收入{O0O00O00O0O0OOOO0}元')#line:249
        else :#line:250
            print (O0O00OO0O000O0O0O .text )#line:251
            return False #line:252
    def get_read_qrcode (OOOO0OO0OO0OOOO0O ):#line:253
        try :#line:254
            O0O000O00O0OOOOO0 =f'https://ltai.litianwm.com/v1/selfread.wechat_read/get_read_qrcode?jpurl={OOOO0OO0OO0OOOO0O.hostUrl[0]}'#line:255
            OOOOO00OOO0OO0OOO =requests .get (O0O000O00O0OOOOO0 ,headers =OOOO0OO0OO0OOOO0O .headers )#line:256
            if 'success'in OOOOO00OOO0OO0OOO .text :#line:257
                OO000OO0O00OO0O0O =OOOOO00OOO0OO0OOO .json ()#line:258
                OOO00OOO0OO00O00O =OO000OO0O00OO0O0O ['data']#line:259
                O0O0OOOO0OO0O0000 =re .search ("data:image/(?P<ext>.*?);base64,(?P<data>.*)",OOO00OOO0OO00O00O ,re .DOTALL )#line:260
                if O0O0OOOO0OO0O0000 :#line:261
                    OOOO0OO0OOO0OOOOO =O0O0OOOO0OO0O0000 .groupdict ().get ("data")#line:262
                    O0O000O00O0OOOOO0 ='http://175.24.153.42:8881/qcro001'#line:263
                    OOO00O000OOOOO0OO ={'data':OOOO0OO0OOO0OOOOO }#line:264
                    OOOOO00OOO0OO0OOO =requests .post (O0O000O00O0OOOOO0 ,json =OOO00O000OOOOO0OO )#line:265
                    if OOOOO00OOO0OO0OOO .text =='':#line:266
                        print ('获取阅读二维码失败0')#line:267
                        return False #line:268
                    OO000OO0O00OO0O0O =OOOOO00OOO0OO0OOO .json ()#line:269
                    O0000OO00OOO0OOO0 =OO000OO0O00OO0O0O .get ('msg')#line:270
                    if O0000OO00OOO0OOO0 ==None :#line:271
                        print ('获取阅读二维码失败1')#line:272
                        return False #line:273
                else :#line:274
                    print ('获取阅读二维码失败0')#line:275
                    return False #line:276
                OOO000OO0OO0O000O =urlparse (O0000OO00OOO0OOO0 )#line:277
                OO00O0O0OOO00000O =OOO000OO0OO0O000O .netloc #line:278
                OOO000000OO0000O0 =parse_qs (OOO000OO0OO0O000O .query )#line:279
                OO0OO000OOO0O0OO0 =OOO000000OO0000O0 .get ('k')[0 ]#line:280
                OOOOO00O0OO0O00O0 =OOO000000OO0000O0 .get ('rd')[0 ]#line:281
                O0OOOO000OOOO0000 ={'Host':'ltai.litianwm.com','Connection':'keep-alive','User-Agent':OOOO0OO0OO0OOOO0O .User_Agent ,'Token':'undefined','Content-Type':'application/json','Accept':'*/*','Origin':f'http://{OO00O0O0OOO00000O}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':f'http://{OO00O0O0OOO00000O}/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9',}#line:296
                print ('获取到的二维码解析的信息',OO0OO000OOO0O0OO0 ,OOOOO00O0OO0O00O0 )#line:297
                return O0OOOO000OOOO0000 ,OO0OO000OOO0O0OO0 ,OOOOO00O0OO0O00O0 #line:298
            else :#line:299
                print ('获取阅读二维码失败')#line:300
                print (OOOOO00OOO0OO0OOO .text )#line:301
                return False #line:302
        except Exception as OO0OO0OO00OO00000 :#line:303
            print (OO0OO0OO00OO00000 )#line:304
            print ('获取阅读二维码失败')#line:305
            return False #line:306
    def getWxArticle (O0OO0O000O0OO0000 ):#line:308
        O00O0O0O0OOOOOOOO =O0OO0O000O0OO0000 .get_read_qrcode ()#line:309
        time .sleep (2 )#line:310
        if O00O0O0O0OOOOOOOO ==False :#line:311
            return False #line:312
        O0OO0O000O0OO0000 .key1 =O00O0O0O0OOOOOOOO [1 ]#line:313
        O0OO00OO0000OO0O0 =0 #line:314
        while True :#line:315
            time .sleep (0.5 )#line:316
            O0O0O0OO0OOOOOOO0 ={"key":O0OO0O000O0OO0000 .key1 ,"rd":O00O0O0O0OOOOOOOO [2 ]}#line:317
            OO0000O000000OOO0 ='https://ltai.litianwm.com/v1/selfread.wechat_read/getWxArticle'#line:318
            OOOO00000OOOOO0OO =requests .post (OO0000O000000OOO0 ,headers =O00O0O0O0OOOOOOOO [0 ],json =O0O0O0OO0OOOOOOO0 )#line:319
            print (O0OO0O000O0OO0000 .name ,'-'*50 )#line:320
            if 'success'in OOOO00000OOOOO0OO .text :#line:321
                OO0OO0O0OOOOOOO00 =OOOO00000OOOOO0OO .json ()['data']#line:322
                OO000000000O0OOOO =OO0OO0O0OOOOOOO00 .get ('url')#line:323
                if OO000000000O0OOOO ==None :#line:324
                    print (O0OO0O000O0OO0000 .name ,f'没有获取到阅读链接')#line:325
                    print (O0OO0O000O0OO0000 .name ,f'阅读结果，结束')#line:326
                    return True #line:327
                if 'http'in OO000000000O0OOOO :#line:328
                    O0OO00OO0000OO0O0 +=1 #line:329
                    print (O0OO0O000O0OO0000 .name ,f'阅读中{OO0OO0O0OOOOOOO00["self_num"]}/{OO0OO0O0OOOOOOO00["total_num"]}')#line:330
                    O0OO0O000O0OO0000 .key1 =OO0OO0O0OOOOOOO00 .get ('key')#line:331
                    OOOO0O00OO00OO0OO =OO0OO0O0OOOOOOO00 .get ('readType')#line:332
                    OOO0000O0O0O0OO0O =OO0OO0O0OOOOOOO00 .get ('readKey')#line:333
                    O00O0OOO0O000OO00 =getinfo (OO000000000O0OOOO )#line:334
                    if O0OO00OO0000OO0O0 in push_num :#line:335
                        OOOOOOOOO00O0O0OO =list (O00O0OOO0O000OO00 )#line:336
                        OOOOOOOOO00O0O0OO [4 ]='ischeck'#line:337
                        if O0OO0O000O0OO0000 .testCheck (OOOOOOOOO00O0O0OO ,OO000000000O0OOOO )==False :#line:338
                            return False #line:339
                    else :#line:340
                        if O0OO0O000O0OO0000 .testCheck (O00O0OOO0O000OO00 ,OO000000000O0OOOO )==False :#line:341
                            return False #line:342
                    if O0OO0O000O0OO0000 .count >=5 :#line:343
                        print (O0OO0O000O0OO0000 .name ,'过检测超过4次中止阅读')#line:344
                        return False #line:345
                    OOOO00O00OO0O00O0 =random .randint (10 ,15 )#line:346
                    print (O0OO0O000O0OO0000 .name ,f'本次模拟读{OOOO00O00OO0O00O0}秒')#line:347
                    time .sleep (OOOO00O00OO0O00O0 )#line:348
                    O0OO0O000O0OO0000 .key1 =O0OO0O000O0OO0000 .completeWxRead (O00O0O0O0OOOOOOOO [0 ],OOOO0O00OO00OO0OO ,OOO0000O0O0O0OO0O ,O0OO0O000O0OO0000 .key1 )#line:349
                    if O0OO0O000O0OO0000 .key1 ==False :#line:350
                        print ('阅读结果')#line:351
                        return False #line:352
                else :#line:353
                    print (OOOO00000OOOOO0OO .text )#line:354
                    print (O0OO0O000O0OO0000 .name ,'未知结果')#line:355
                    return False #line:356
            else :#line:357
                print (OOOO00000OOOOO0OO .text )#line:358
                return False #line:359
    def completeWxRead (OOOO0OO00OOOOO00O ,OOO0OOOO0000O0000 ,OO0OO000O0O0O0O0O ,OOOO0000O0OOOOOO0 ,OOOO0OOO0OO000OOO ):#line:360
        OOO0OO0O0O00O0OOO ='https://ltai.litianwm.com/v1/selfread.wechat_read/completeWxRead'#line:361
        OOO00O00OO0OO0OOO ={"cType":OO0OO000O0O0O0O0O ,"cKey":OOOO0000O0OOOOOO0 ,"key":OOOO0OOO0OO000OOO }#line:362
        OOO000O0O0000O0O0 =requests .post (OOO0OO0O0O00O0OOO ,headers =OOO0OOOO0000O0000 ,json =OOO00O00OO0OO0OOO )#line:363
        if 'success'in OOO000O0O0000O0O0 .text :#line:364
            OOO000000O00OO0OO =OOO000O0O0000O0O0 .json ()#line:365
            OOOO0OOO0OO000OOO =OOO000000O00OO0OO ['data']['key']#line:366
            return OOOO0OOO0OO000OOO #line:367
        else :#line:368
            print (OOO000O0O0000O0O0 .text )#line:369
            return False #line:370
    def testCheck (OO0O00000OOO0O000 ,OOO000OO0OOOOOO00 ,O0OO00O0OOO000OOO ):#line:371
        if OOO000OO0OOOOOO00 [4 ]==[]:#line:372
            print (OO0O00000OOO0O000 .name ,'这个链接没有获取到微信号id',O0OO00O0OOO000OOO )#line:373
            return True #line:374
        if OOO000OO0OOOOOO00 [5 ]==[]:#line:375
            print (OO0O00000OOO0O000 .name ,'这个链接没有获取到时间',O0OO00O0OOO000OOO )#line:376
            return True #line:377
        if (checkDict .get (OOO000OO0OOOOOO00 [4 ])!=None )or (int (time .time ())-int (OOO000OO0OOOOOO00 [5 ])>3600 *24 *14 ):#line:378
            OO0O00000OOO0O000 .count +=1 #line:379
            if OO0O00000OOO0O000 .setstatus ()==99 :#line:380
                print (OO0O00000OOO0O000 .name ,'过检测服务器异常，使用无回调方案，请在50s内阅读检测文章')#line:381
                push (f'百事通读过检测:{OO0O00000OOO0O000.name}',O0OO00O0OOO000OOO ,OOO000OO0OOOOOO00 [3 ],'yuanbao',OO0O00000OOO0O000 .uids ,OO0O00000OOO0O000 .key )#line:382
                time .sleep (50 )#line:383
                return True #line:384
            for O00OO0OOO00O0O0OO in range (60 ):#line:385
                if O00OO0OOO00O0O0OO %30 ==0 :#line:386
                    OO0O00000O0OO00OO =f'http://175.24.153.42:8882/lookwxarticle?key=KEY&type=TYPE&wxurl={O0OO00O0OOO000OOO}'#line:387
                    push (f'百事通阅读过检测:{OO0O00000OOO0O000.name}',OO0O00000O0OO00OO ,OOO000OO0OOOOOO00 [3 ],'yuanbao',OO0O00000OOO0O000 .uids ,OO0O00000OOO0O000 .key )#line:388
                O000OO0OO0O000OO0 =OO0O00000OOO0O000 .getstatus ()#line:389
                if O000OO0OO0O000OO0 =='0':#line:390
                    print (OO0O00000OOO0O000 .name ,'过检测文章已经阅读')#line:391
                    return True #line:392
                elif O000OO0OO0O000OO0 =='1':#line:393
                    print (OO0O00000OOO0O000 .name ,f'正在等待过检测文章阅读结果{O00OO0OOO00O0O0OO}秒。。。')#line:394
                    time .sleep (1 )#line:395
                else :#line:396
                    print (OO0O00000OOO0O000 .name ,O000OO0OO0O000OO0 )#line:397
                    print (OO0O00000OOO0O000 .name ,'服务器异常')#line:398
            print (OO0O00000OOO0O000 .name ,'过检测超时中止脚本防止黑号')#line:399
            return False #line:400
        else :#line:401
            return True #line:402
    def run (O0000OOOO0OO0O0OO ):#line:403
        if hashlib .md5 (oo0o .encode ()).hexdigest ()!='373dd4f26e6fd5b3a6fc3f1d1b0b67b9':O0000OOOO0OO0O0OO .setstatus ()#line:404
        O0000OOOO0OO0O0OO .amountValue ()#line:405
        O0000OOOO0OO0O0OO .readinfo ()#line:406
        O0000OOOO0OO0O0OO .getWxArticle ()#line:407
        time .sleep (2 )#line:408
        O0000OOOO0OO0O0OO .amountValue ()#line:409
def getEnv (O0OO0000O0OOO00O0 ):#line:410
    O000000O0000O00OO =os .getenv (O0OO0000O0OOO00O0 )#line:411
    if O000000O0000O00OO ==None :#line:412
        print (f'{O0OO0000O0OOO00O0}青龙变量里没有获取到')#line:413
        exit (0 )#line:414
    try :#line:415
        O000000O0000O00OO =json .loads (O000000O0000O00OO .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:416
        return O000000O0000O00OO #line:417
    except Exception as O0OOO00000O0O0OOO :#line:418
        print ('错误:',O0OOO00000O0O0OOO )#line:419
        print ('你填写的变量是:',O000000O0000O00OO )#line:420
        print ('请检查变量参数是否填写正确')#line:421
if __name__ =='__main__':#line:422
    push_config =getEnv ('push_config')#line:424
    klydconfig =getEnv ('bstyd')#line:425
    printf =push_config .get ('printf',0 )#line:426
    appToken =push_config ['appToken']#line:427
    threadingf =push_config .get ('threadingf',1 )#line:428
    getmsg ()#line:429
    if threadingf ==1 :#line:430
        tl =[]#line:431
        for indexs ,cg in enumerate (klydconfig ):#line:432
            print ('*'*50 )#line:433
            print (f'开始执行{cg["name"]}')#line:434
            api =WXYD (cg ,indexs )#line:435
            t =threading .Thread (target =api .run ,args =())#line:436
            tl .append (t )#line:437
            t .start ()#line:438
            threadingt =push_config .get ('threadingt',3 )#line:439
            time .sleep (threadingt )#line:440
        for t in tl :#line:441
            t .join ()#line:442
    elif threadingf ==0 :#line:443
        for indexs ,cg in enumerate (klydconfig ):#line:444
            print ('*'*50 )#line:445
            print (f'开始执行{cg["name"]}')#line:446
            api =WXYD (cg ,indexs )#line:447
            api .run ()#line:448
            print (f'{cg["name"]}执行完毕')#line:449
            time .sleep (3 )#line:450
    else :#line:451
        print ('请确定推送变量中threadingf参数是否正确')#line:452
    print ('全部账号执行完成')#line:453
    time .sleep (10 )#line:454
