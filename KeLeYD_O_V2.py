oo0o ='''
cron: 30 */30 8-22 * * *
new Env('可乐阅读');
活动入口：http://12318208252026.excqoef.cn/r?upuid=123182
使用方法：
1.入口,WX打开：http://12318208252026.excqoef.cn/r?upuid=123182
'''#line:7
'''
1.入口1,WX打开http://12318208252026.excqoef.cn/r?upuid=123182
入口2：http://12318208261109.eooyvuu.cn/r?upuid=123182
若链接微信无法打开，请复制到浏览器复制新链接打开
2.打开活动入口，抓包的任意接口cookie参数
3.青龙菜单项《配置文件》，添加本脚本环境变量
填写变量参数时为方便填写可以随意换行
单账户：export klydconfig="[{'name':'备注名','udtauth12': 'xxxx','key':'xxxxxxx','uids':'xxxxxxx'}]"
多账户：export klydconfig="[
{'name':'备注名','udtauth12': 'xxxx','key':'xxxxx','uids':'xxxxxxx'},
{'name':'备注名','udtauth12': 'xxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','udtauth12': 'xxx7Rxxxxx','key':'xxxxxxx','uids':'xxxxxxx'}
]"
参数说明：
name:备注名随意填写
cookie:打开活动入口，抓包的任意接口headers中的udtauth12参数
key：每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送应用后，会在推送管理后台(https://wxpusher.zjiecode.com/admin/main)的'用户管理-->用户列表'中显示
用户在推送页面点击’我的-->我的UID‘也可以获取
User-Agent:抓包任意接口在headers中看到
4.青龙菜单项《配置文件》，添加本脚wxpusher环境变量(不需要重复添加)
export push_config="{'printf':0,'threadingf':1,'threadingt':3,'appToken':'xxxx'}"
参数说明：
printf:0是不打印调试日志，1是打印调试日志
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
threadingt:并行运行时每个账号的间隔时间默认3s
appToken 这个是填wxpusher的appToken,wxpusher如何使用可以百度
5.脚本运行时，检测到需要手动阅读的文章，将会推送到你的微信（需要填写好推送参数），你需要手动点击推送，阅读文章，这时脚本会继续运行，否则60秒后将检查超时，停止脚本。
定时运行每半个小时一次
'''#line:39
import requests #line:40
import re #line:41
import random #line:42
import os #line:43
import threading #line:44
import json #line:45
import hashlib #line:46
import time #line:47
from urllib .parse import urlparse ,parse_qs #line:48
checkDict ={'ischeck':['检测标注','检测标注请勿修改'],'MzkwNTY1MzYxOQ==':['无无有歌','gh_7d594718e309'],}#line:52
push_num =[-1 ]#line:53
def getmsg ():#line:54
    global checkDict #line:55
    OO000O00O0000O00O ='v1.0'#line:56
    try :#line:57
        OOOO00O00O00OOOO0 ='http://175.24.153.42:8881/getmsg'#line:58
        OOOO00O0O0000OO00 ={'type':'zhyd'}#line:59
        O0OOO0000000O00OO =requests .get (OOOO00O00O00OOOO0 ,params =OOOO00O0O0000OO00 ,timeout =2 )#line:60
        O0OO0O000000OO0OO =O0OOO0000000O00OO .json ()#line:61
        OOOOO00OOOO00O000 =O0OO0O000000OO0OO .get ('version')#line:62
        OOOO000OOOO000OOO =O0OO0O000000OO0OO .get ('gdict')#line:63
        O00O0O000OOOOO0OO =O0OO0O000000OO0OO .get ('gmmsg')#line:64
        print ('系统公告:',O00O0O000OOOOO0OO )#line:65
        print (f'最新版本{OOOOO00OOOO00O000},当前版本{OO000O00O0000O00O}')#line:66
        if OO000O00O0000O00O !=OOOOO00OOOO00O000 :#line:67
            print ('版本不一致，可能要更新脚本了')#line:68
        print (f'系统的公众号字典{len(OOOO000OOOO000OOO)}个:{OOOO000OOOO000OOO}')#line:69
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:70
        checkDict ={}#line:71
        for OO000OO000000OO0O in OOOO000OOOO000OOO :#line:72
            checkDict .update ({OO000OO000000OO0O :['','']})#line:73
    except Exception as OOOOO0OOOOOO0O00O :#line:74
        print (OOOOO0OOOOOO0O00O )#line:75
        print ('公告服务器异常')#line:76
def push (OO00000O00OOOO0O0 ,O00OOOO00O0OO0000 ,O00O0OO000OO0O0OO ,OOO0O0OO00000O00O ,OOO0000000OOO0O0O ,OO0O000O0O0OOO000 ):#line:77
    OOOOOO00000O0OO00 ='''
<body onload="window.location.href='LINK'">
<p>TEXT</p><br>
<p><a href="http://175.24.153.42:8882/lookstatus?key=KEY&type=TYPE">查看状态</a></p><br>
</body>
    '''#line:83
    O0O0O0O0OOOO00000 =OOOOOO00000O0OO00 .replace ('TITTLE',OO00000O00OOOO0O0 ).replace ('LINK',O00OOOO00O0OO0000 ).replace ('TEXT',O00O0OO000OO0O0OO ).replace ('TYPE',OOO0O0OO00000O00O ).replace ('KEY',OO0O000O0O0OOO000 )#line:85
    OOOO0OOO000O000O0 ={"appToken":appToken ,"content":O0O0O0O0OOOO00000 ,"summary":OO00000O00OOOO0O0 ,"contentType":2 ,"uids":[OOO0000000OOO0O0O ]}#line:92
    OO0OO0O0O00O00OO0 ='http://wxpusher.zjiecode.com/api/send/message'#line:93
    try :#line:94
        O0OO00OOOO0OO0000 =requests .post (url =OO0OO0O0O00O00OO0 ,json =OOOO0OOO000O000O0 ).text #line:95
        print ('推送结果：',O0OO00OOOO0OO0000 )#line:96
        return True #line:97
    except Exception as O0OO000O0000OOOO0 :#line:98
        print ('推送失败！')#line:99
        print ('推送结果：',O0OO000O0000OOOO0 )#line:100
        return False #line:101
def getinfo (O0O0OO00O0OO00OO0 ):#line:102
    try :#line:103
        OOO0O0OOO0O0OO00O ={'Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090b19) XWEB/9193 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language':'zh-CN,zh;q=0.9','Cookie':'rewardsn=; wxtokenkey=777; devicetype=Windows11x64; version=73020b18; lang=zh_CN;',}#line:110
        OOOOOOO000O0O0O0O =requests .get (O0O0OO00O0OO00OO0 ,headers =OOO0O0OOO0O0OO00O )#line:111
        O0O0OO0OOOO0OOOO0 =re .sub ('\s','',OOOOOOO000O0O0O0O .text )#line:112
        O00OOO00000OO0OOO =re .findall ('varbiz="(.*?)"\|\|',O0O0OO0OOOO0OOOO0 )#line:113
        if O00OOO00000OO0OOO !=[]:#line:114
            O00OOO00000OO0OOO =O00OOO00000OO0OOO [0 ]#line:115
        if O00OOO00000OO0OOO ==''or O00OOO00000OO0OOO ==[]:#line:116
            if '__biz'in O0O0OO00O0OO00OO0 :#line:117
                O00OOO00000OO0OOO =re .findall ('__biz=(.*?)&',O0O0OO00O0OO00OO0 )#line:118
                if O00OOO00000OO0OOO !=[]:#line:119
                    O00OOO00000OO0OOO =O00OOO00000OO0OOO [0 ]#line:120
        OO000OO0000OO0OOO =re .findall ('varnickname=htmlDecode\("(.*?)"\);',O0O0OO0OOOO0OOOO0 )#line:121
        if OO000OO0000OO0OOO !=[]:#line:122
            OO000OO0000OO0OOO =OO000OO0000OO0OOO [0 ]#line:123
        OOO00OO00OOOOOO0O =re .findall ('varuser_name="(.*?)";',O0O0OO0OOOO0OOOO0 )#line:124
        if OOO00OO00OOOOOO0O !=[]:#line:125
            OOO00OO00OOOOOO0O =OOO00OO00OOOOOO0O [0 ]#line:126
        O0OO0O0000000O0OO =re .findall ("varmsg_title='(.*?)'\.html\(",O0O0OO0OOOO0OOOO0 )#line:127
        if O0OO0O0000000O0OO !=[]:#line:128
            O0OO0O0000000O0OO =O0OO0O0000000O0OO [0 ]#line:129
        OO0OO0O0O0OOOOO0O =re .findall ("varoriCreateTime='(.*?)';",O0O0OO0OOOO0OOOO0 )#line:130
        if OO0OO0O0O0OOOOO0O !=[]:#line:131
            OO0OO0O0O0OOOOO0O =OO0OO0O0O0OOOOO0O [0 ]#line:132
        O0O0OO000OOOO00OO =re .findall ("varcreateTime='(.*?)';",O0O0OO0OOOO0OOOO0 )#line:133
        if O0O0OO000OOOO00OO !=[]:#line:134
            O0O0OO000OOOO00OO =O0O0OO000OOOO00OO [0 ]#line:135
            O0O0OO000OOOO00OO =O0O0OO000OOOO00OO [:-5 ]+' '+O0O0OO000OOOO00OO [-5 :]#line:136
        O0O0O00OO0O000OOO =f'公众号唯一标识：{O00OOO00000OO0OOO}|文章:{O0OO0O0000000O0OO}|作者:{OO000OO0000OO0OOO}|账号:{OOO00OO00OOOOOO0O}|文章时间戳:{OO0OO0O0O0OOOOO0O}|文章时间:{O0O0OO000OOOO00OO}'#line:137
        print (O0O0O00OO0O000OOO )#line:138
        return OO000OO0000OO0OOO ,OOO00OO00OOOOOO0O ,O0OO0O0000000O0OO ,O0O0O00OO0O000OOO ,O00OOO00000OO0OOO ,OO0OO0O0O0OOOOO0O ,O0O0OO000OOOO00OO #line:139
    except Exception as O0O00OO0O0O000O00 :#line:140
        print (O0O00OO0O0O000O00 )#line:141
        print ('异常')#line:142
        return False #line:143
class WXYD :#line:144
    def __init__ (O00O00O0OO0O0OO00 ,OOOO0O0OO00OO0O00 ):#line:145
        O00O00O0OO0O0OO00 .name =OOOO0O0OO00OO0O00 ['name']#line:146
        O00O00O0OO0O0OO00 .key =OOOO0O0OO00OO0O00 ['key']#line:147
        O00O00O0OO0O0OO00 .uids =OOOO0O0OO00OO0O00 ['uids']#line:148
        O00O00O0OO0O0OO00 .count =0 #line:149
        O00O00O0OO0O0OO00 .User_Agent ='Mozilla/5.0 (Linux; Android 13; M2104K10AC Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110017 MMWEBSDK/20231002 MMWEBID/2545 MicroMessenger/8.0.43.2480(0x28112BE1) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64'#line:150
        OO0O0O0OOOOOO0OOO =O00O00O0OO0O0OO00 .get_host ()#line:151
        O00O00O0OO0O0OO00 .host =OO0O0O0OOOOOO0OOO [0 ]#line:152
        O00O00O0OO0O0OO00 .t =OO0O0O0OOOOOO0OOO [1 ]#line:153
        O00O00O0OO0O0OO00 .headers ={'Host':'m.zzyi4cf7z8.cn','Connection':'keep-alive','Accept':'application/json, text/plain, */*','X-Requested-With':'XMLHttpRequest','udtauth12':OOOO0O0OO00OO0O00 ['udtauth12'],'User-Agent':O00O00O0OO0O0OO00 .User_Agent ,'Origin':f'http://{O00O00O0OO0O0OO00.host}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':f'http://{O00O00O0OO0O0OO00.host}/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9',}#line:168
    def printjson (O0O0OOO000OOO00OO ,O0O00O0O0O00O0000 ):#line:169
        if printf ==0 :#line:170
            return False #line:171
        print (O0O0OOO000OOO00OO .name ,O0O00O0O0O00O0000 )#line:172
    def setstatus (OOOO0OO0O00O00O00 ):#line:173
        try :#line:174
            OOO0O00O000OOOOOO ='http://175.24.153.42:8882/setstatus'#line:175
            OOO00O0O00OOO0000 ={'key':OOOO0OO0O00O00O00 .key ,'type':'zhyd','val':'1','ven':oo0o }#line:176
            O00O0O00O0O0OO00O =requests .get (OOO0O00O000OOOOOO ,params =OOO00O0O00OOO0000 ,timeout =5 )#line:177
            print (OOOO0OO0O00O00O00 .name ,O00O0O00O0O0OO00O .text )#line:178
            if '无效'in O00O0O00O0O0OO00O .text :#line:179
                exit (0 )#line:180
        except Exception as O00000O000O0OOOOO :#line:181
            print (OOOO0OO0O00O00O00 .name ,'设置状态异常')#line:182
            print (OOOO0OO0O00O00O00 .name ,O00000O000O0OOOOO )#line:183
            return 99 #line:184
    def getstatus (O0000O0O0O0OO0000 ):#line:185
        try :#line:186
            OOO00OOO000O0O000 ='http://175.24.153.42:8882/getstatus'#line:187
            OOO00OOO000OOOOOO ={'key':O0000O0O0O0OO0000 .key ,'type':'zhyd'}#line:188
            O00O00O0O0OO0OOOO =requests .get (OOO00OOO000O0O000 ,params =OOO00OOO000OOOOOO ,timeout =3 )#line:189
            return O00O00O0O0OO0OOOO .text #line:190
        except Exception as OOO00OO00O0O00OOO :#line:191
            print (O0000O0O0O0OO0000 .name ,'查询状态异常',OOO00OO00O0O00OOO )#line:192
            return False #line:193
    def get_host (OOO0000O0O0OOOOO0 ):#line:194
        try :#line:195
            OOOOOOO0OO00OO0O0 ='http://12318208252026.excqoef.cn/r?upuid=123182'#line:196
            O000OOOO0O0O0OO0O ={'Host':'12318208252026.excqoef.cn','Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':OOO0000O0O0OOOOO0 .User_Agent ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9',}#line:205
            OO0O0O0O000O00000 =requests .get (OOOOOOO0OO00OO0O0 ,headers =O000OOOO0O0O0OO0O ,allow_redirects =False )#line:206
            if OO0O0O0O000O00000 .headers .get ('Location')!=None :#line:207
                O000OO0O0O0OOOO0O =urlparse (OO0O0O0O000O00000 .headers .get ('Location'))#line:208
                OOOO00OO00000OO0O =O000OO0O0O0OOOO0O .netloc #line:209
                OO000OOO0000O00O0 =re .findall (r't=(\d+)',OO0O0O0O000O00000 .headers .get ('Location'))[0 ]#line:210
                return OOOO00OO00000OO0O ,OO000OOO0000O00O0 #line:211
            else :#line:212
                print ('获取host失败0')#line:213
                return 'klluodi-04.obs.cn-jxnc1.ctyun.cn'#line:214
        except Exception as O0O00O000OOO0O000 :#line:215
            print ('获取host失败1',O0O00O000OOO0O000 )#line:216
            return 'klluodi-04.obs.cn-jxnc1.ctyun.cn'#line:217
    def tuijian (O00000O0OOO0OO0OO ):#line:218
        OO0O0O0O0O00O0OOO =f'https://m.zzyi4cf7z8.cn/tuijian?url=upuid%3D123182%26t%3D{O00000O0OOO0OO0OO.t}&upuid=123182'#line:219
        O00O0OOO00OO00O0O =requests .get (OO0O0O0O0O00O0OOO ,headers =O00000O0OOO0OO0OO .headers )#line:220
        try :#line:221
            O0000O0OOOO0OOO0O =O00O0OOO00OO00O0O .json ()#line:222
            if O0000O0OOOO0OOO0O .get ('code')==0 :#line:223
                O0OOO0OOO0OOOO0OO =O0000O0OOOO0OOO0O ['data']['user']['username']#line:224
                O000O00000O0OO0OO =float (O0000O0OOOO0OOO0O ['data']['user']['score'])/100 #line:225
                O00OOO00O0OOO000O =O0000O0OOOO0OOO0O ['data']['infoView'].get ('msg')#line:226
                OO00O0O00O0O0OOO0 =O0000O0OOOO0OOO0O ['data']['infoView']['num']#line:227
                O00OO0OOO000O0000 =O0000O0OOOO0OOO0O ['data']['infoView']['rest']#line:228
                if O00OO0OOO000O0000 ==0 :#line:229
                    print ('当前状态，可能是不可阅读')#line:230
                    print (O00000O0OOO0OO0OO .name ,f'{O0OOO0OOO0OOOO0OO}:当前剩余{O000O00000O0OO0OO}元,今日已经阅读：{OO00O0O00O0O0OOO0}篇,提示信息：{O00OOO00O0OOO000O}')#line:231
                    return False #line:232
                print (O00000O0OOO0OO0OO .name ,f'{O0OOO0OOO0OOOO0OO}:当前剩余{O000O00000O0OO0OO}元,今日已经阅读：{OO00O0O00O0O0OOO0}篇,提示信息：{O00OOO00O0OOO000O}')#line:233
                return True #line:234
            else :#line:235
                print (O00000O0OOO0OO0OO .name ,O0000O0OOOO0OOO0O )#line:236
                print (O00000O0OOO0OO0OO .name ,'账号异常0,ck可能失效')#line:237
                return False #line:238
        except Exception as O0OOO00OO0OOO00O0 :#line:239
            print (O00000O0OOO0OO0OO .name ,O0OOO00OO0OOO00O0 )#line:240
            print (O00000O0OOO0OO0OO .name ,'账号异常1，ck可能失效')#line:241
            return False #line:242
    def get_read_url (O000O0OO0OOO0OO0O ):#line:243
        OOOOO00O0O000OOOO ='https://m.zzyi4cf7z8.cn/new/bbbbb'#line:244
        OO0O0OO0OOO0O00OO =requests .get (OOOOO00O0O000OOOO ,headers =O000O0OO0OOO0OO0O .headers )#line:245
        O0OOO0000000000OO =OO0O0OO0OOO0O00OO .json ()#line:246
        OOO0000OOOO0OO00O =O0OOO0000000000OO .get ('jump')#line:247
        OOOO00OO00O00OOOO =parse_qs (urlparse (OOO0000OOOO0OO00O ).query )#line:248
        OOO0OO0OO0O00O0OO =urlparse (OOO0000OOOO0OO00O ).netloc #line:249
        OO0OO0000OO0OO000 =OOOO00OO00O00OOOO .get ('iu')[0 ]#line:250
        OOOO0O00OO0OO0000 ={'Host':O000O0OO0OOO0OO0O .host ,'Connection':'keep-alive','User-Agent':O000O0OO0OOO0OO0O .User_Agent ,'X-Requested-With':'XMLHttpRequest','Accept':'*/*','Origin':f'http://{OOO0OO0OO0O00O0OO}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':f'http://{OOO0OO0OO0O00O0OO}/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9',}#line:264
        return OO0OO0000OO0OO000 ,OOO0OO0OO0O00O0OO ,OOOO0O00OO0OO0000 #line:265
    def do_read (O0O0OO000O0000000 ):#line:267
        OO0O0O0OO0O00000O =O0O0OO000O0000000 .get_read_url ()#line:268
        O0O0OO000O0000000 .jkey =''#line:269
        O0OO0OO0O0O0000O0 =0 #line:270
        while True :#line:271
            OO000O000O0O00OOO =f'iu={OO0O0O0OO0O00000O[0]}&r={round(random.uniform(0, 1), 17)}&{O0O0OO000O0000000.jkey}'#line:273
            O00OO000O0O00OOO0 ='https://m.zzyi4cf7z8.cn/dodoaa/mmaa?'+OO000O000O0O00OOO #line:274
            O0O0OO000O0000000 .printjson (O00OO000O0O00OOO0 )#line:275
            OO0OOO0O0OO0O00OO =requests .get (O00OO000O0O00OOO0 ,headers =OO0O0O0OO0O00000O [2 ])#line:276
            print (O0O0OO000O0000000 .name ,'-'*50 )#line:277
            O0O0OO000OOO0O000 =OO0OOO0O0OO0O00OO .json ()#line:278
            if O0O0OO000OOO0O000 .get ('msg'):#line:279
                print (O0O0OO000O0000000 .name ,'弹出msg',O0O0OO000OOO0O000 .get ('msg'))#line:280
            if O0O0OO000OOO0O000 .get ('success_msg'):#line:281
                print (O0O0OO000O0000000 .name ,'成功msg',O0O0OO000OOO0O000 .get ('msg'))#line:282
            O0OO0000O0000OO0O =O0O0OO000OOO0O000 .get ('url')#line:283
            O0O0OO000O0000000 .printjson (O0OO0000O0000OO0O )#line:284
            if O0OO0000O0000OO0O =='close':#line:285
                print (O0O0OO000O0000000 .name ,f'阅读结果结束')#line:286
                return True #line:287
            if 'http'in O0OO0000O0000OO0O :#line:288
                O0OO0OO0O0O0000O0 +=1 #line:289
                print (O0O0OO000O0000000 .name ,f'上一篇阅读结果：{O0O0OO000OOO0O000.get("success_msg","第一篇开始阅读或者异常")}')#line:290
                O0OOO0O0OOO0O000O =O0O0OO000OOO0O000 .get ('jkey')#line:291
                O0O0OO000O0000000 .jkey =f'&jkey={O0OOO0O0OOO0O000O}'#line:292
                OOOO000000000OOO0 =getinfo (O0OO0000O0000OO0O )#line:293
                if O0OO0OO0O0O0000O0 in push_num :#line:294
                    OOO00O00OO0000OO0 =list (OOOO000000000OOO0 )#line:295
                    OOO00O00OO0000OO0 [4 ]='ischeck'#line:296
                    if O0O0OO000O0000000 .testCheck (OOO00O00OO0000OO0 ,O0OO0000O0000OO0O )==False :#line:297
                        return False #line:298
                else :#line:299
                    if O0O0OO000O0000000 .testCheck (OOOO000000000OOO0 ,O0OO0000O0000OO0O )==False :#line:300
                        return False #line:301
                if O0O0OO000O0000000 .count >=5 :#line:302
                    print (O0O0OO000O0000000 .name ,'过检测超过4次中止阅读')#line:303
                    return False #line:304
                OO0000O0O000O0O00 =random .randint (6 ,9 )#line:305
                print (O0O0OO000O0000000 .name ,f'本次模拟读{OO0000O0O000O0O00}秒')#line:306
                time .sleep (OO0000O0O000O0O00 )#line:307
            else :#line:308
                print (O0O0OO000O0000000 .name ,'未知结果')#line:309
                print (O0O0OO000O0000000 .name ,O0O0OO000OOO0O000 )#line:310
                break #line:311
    def testCheck (OO00O0O0OOOO0O00O ,O0OO00OO00OOO000O ,O000OO0OOOO0000O0 ):#line:312
        if O0OO00OO00OOO000O [4 ]==[]:#line:313
            print (OO00O0O0OOOO0O00O .name ,'这个链接没有获取到微信号id',O000OO0OOOO0000O0 )#line:314
            return True #line:315
        if O0OO00OO00OOO000O [5 ]==[]:#line:316
            print (OO00O0O0OOOO0O00O .name ,'这个链接没有获取到时间',O000OO0OOOO0000O0 )#line:317
            return True #line:318
        if (checkDict .get (O0OO00OO00OOO000O [4 ])!=None )or (int (time .time ())-int (O0OO00OO00OOO000O [5 ])>3600 *24 *14 ):#line:319
            OO00O0O0OOOO0O00O .count +=1 #line:320
            if OO00O0O0OOOO0O00O .setstatus ()==99 :#line:321
                print (OO00O0O0OOOO0O00O .name ,'过检测服务器异常，使用无回调方案，请在50s内阅读检测文章')#line:322
                push (f'可乐阅读过检测:{OO00O0O0OOOO0O00O.name}',O000OO0OOOO0000O0 ,O0OO00OO00OOO000O [3 ],'zhyd',OO00O0O0OOOO0O00O .uids ,OO00O0O0OOOO0O00O .key )#line:323
                time .sleep (50 )#line:324
                return True #line:325
            for O0OOO0OO0000OO0OO in range (60 ):#line:326
                if O0OOO0OO0000OO0OO %30 ==0 :#line:327
                    OOOOO000OOOOOOO00 =f'http://175.24.153.42:8882/lookwxarticle?key=KEY&type=TYPE&wxurl={O000OO0OOOO0000O0}'#line:328
                    push (f'可乐阅读过检测:{OO00O0O0OOOO0O00O.name}',OOOOO000OOOOOOO00 ,O0OO00OO00OOO000O [3 ],'zhyd',OO00O0O0OOOO0O00O .uids ,OO00O0O0OOOO0O00O .key )#line:329
                OOOOOO0O0OOO0O0O0 =OO00O0O0OOOO0O00O .getstatus ()#line:330
                if OOOOOO0O0OOO0O0O0 =='0':#line:331
                    print (OO00O0O0OOOO0O00O .name ,'过检测文章已经阅读')#line:332
                    return True #line:333
                elif OOOOOO0O0OOO0O0O0 =='1':#line:334
                    print (OO00O0O0OOOO0O00O .name ,f'正在等待过检测文章阅读结果{O0OOO0OO0000OO0OO}秒。。。')#line:335
                    time .sleep (1 )#line:336
                else :#line:337
                    print (OO00O0O0OOOO0O00O .name ,OOOOOO0O0OOO0O0O0 )#line:338
                    print (OO00O0O0OOOO0O00O .name ,'服务器异常')#line:339
            print (OO00O0O0OOOO0O00O .name ,'过检测超时中止脚本防止黑号')#line:340
            return False #line:341
        else :#line:342
            return True #line:343
    def withdrawal (OO0O00O00OOO0OOOO ):#line:344
        OO0O00000O0O0O000 ='https://m.zzyi4cf7z8.cn/withdrawal'#line:345
        O0OOOOO0OO0OOOOOO =requests .get (OO0O00000O0O0O000 ,headers =OO0O00O00OOO0OOOO .headers )#line:346
        O0OOOO000O0000OO0 =O0OOOOO0OO0OOOOOO .json ()#line:347
        time .sleep (3 )#line:348
        if O0OOOO000O0000OO0 .get ('code')==0 :#line:349
            OO00O0000OOO000O0 =int (float (O0OOOO000O0000OO0 ['data']['user']['score']))#line:350
            if OO00O0000OOO000O0 <30 :#line:351
                print ('没有达到提现标标准')#line:352
                return False #line:353
            O000OO0000OO0O000 =OO0O00O00OOO0OOOO .headers .copy ()#line:354
            O000OO0000OO0O000 .update ({'Content-Type':'application/x-www-form-urlencoded'})#line:355
            OO0O00000O0O0O000 ='https://m.zzyi4cf7z8.cn/withdrawal/doWithdraw'#line:356
            OO0O0OOOO0OO0O0OO =f'amount={OO00O0000OOO000O0}&type=wx'#line:357
            O0OOOOO0OO0OOOOOO =requests .post (OO0O00000O0O0O000 ,headers =O000OO0000OO0O000 ,data =OO0O0OOOO0OO0O0OO )#line:358
            print (OO0O00O00OOO0OOOO .name ,'提现结果',O0OOOOO0OO0OOOOOO .text )#line:359
        else :#line:360
            print ('提现异常')#line:361
            print (OO0O00O00OOO0OOOO .name ,O0OOOO000O0000OO0 )#line:362
    def run (O0O00OO00O00O0OOO ):#line:363
        if hashlib .md5 (oo0o .encode ()).hexdigest ()!='e08ca2eddd87fc6ddceba5e5491202bd':O0O00OO00O00O0OOO .setstatus ()#line:364
        if O0O00OO00O00O0OOO .tuijian ():#line:365
            time .sleep (2 )#line:366
            O0O00OO00O00O0OOO .get_read_url ()#line:367
            O0O00OO00O00O0OOO .do_read ()#line:368
            time .sleep (2 )#line:369
            O0O00OO00O00O0OOO .withdrawal ()#line:370
def getEnv (O00O000OOO0O0000O ):#line:371
    OOO0OO00OOOOO0OOO =os .getenv (O00O000OOO0O0000O )#line:372
    if OOO0OO00OOOOO0OOO ==None :#line:373
        print (f'{O00O000OOO0O0000O}青龙变量里没有获取到，使用本地参数')#line:374
        return False #line:375
    try :#line:376
        OOO0OO00OOOOO0OOO =json .loads (OOO0OO00OOOOO0OOO .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:377
        return OOO0OO00OOOOO0OOO #line:378
    except Exception as O0OOO0O000O00000O :#line:379
        print ('错误:',O0OOO0O000O00000O )#line:380
        print ('你填写的变量是:',OOO0OO00OOOOO0OOO )#line:381
        print ('请检查变量参数是否填写正确')#line:382
        print (f'{O00O000OOO0O0000O}使用本地参数')#line:383
if __name__ =='__main__':#line:384
    push_config = getEnv('push_config')
    klydconfig = getEnv('klydconfig')
    printf = push_config.get('printf',0)  # 打印调试日志0不打印，1打印，若运行异常请打开调试
    appToken = push_config['appToken']
    threadingf = push_config.get('threadingf',1)
    getmsg()
    if threadingf == 1:
        tl=[]
        for cg in klydconfig:
            print('*' * 50)
            print(f'开始执行{cg["name"]}')
            api = WXYD(cg)
            t = threading.Thread(target=api.run, args=())
            tl.append(t)
            t.start()
            threadingt=push_config.get('threadingt',3)
            time.sleep(threadingt)
        for t in tl:
            t.join()
    elif threadingf == 0:
        for cg in klydconfig:
            print('*' * 50)
            print(f'开始执行{cg["name"]}')
            api = WXYD(cg)
            api.run()
            print(f'{cg["name"]}执行完毕')
            time.sleep(3)
    else:
        print('请确定推送变量中threadingf参数是否正确')
    print('全部账号执行完成')
    time.sleep(10)
