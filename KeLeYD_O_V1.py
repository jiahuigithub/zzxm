oo0o ='''
cron: 30 */30 8-22 * * *
new Env('可乐阅读');
活动入口：http://12318208252026.excqoef.cn/r?upuid=123182
使用方法：
1.入口,WX打开：http://12318208252026.excqoef.cn/r?upuid=123182
'''#line:7
'''
1.入口,WX打开http://12318208252026.excqoef.cn/r?upuid=123182
若链接微信无法打开，请复制到浏览器复制新链接打开
2.打开活动入口，抓包的任意接口cookie参数
3.青龙菜单项《配置文件》，添加本脚本环境变量
填写变量参数时为方便填写可以随意换行
单账户：export klydconfig="[{'name':'备注名','udtauth12': 'xxxxxx','key':'xxxxxxx','uids':'xxxxxxx'}]"
多账户：export klydconfig="[
{'name':'备注名','udtauth12': 'xxxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','udtauth12': 'xxxxx','key':'xxxxxxx','uids':'xxxxxxx'},
{'name':'备注名','udtauth12': 'xxxxx','key':'xxxxxxx','uids':'xxxxxxx'}
]"
参数说明：
name:备注名随意填写
cookie:打开活动入口，抓包的任意接口headers中的udtauth12参数
key：每个账号的推送标准，每个账号全阅读只需要一个key,多个账号需要多个key,key永不过期。
为了防止恶意调用key接口，限制每个ip每天只能获取一个key。手机开飞行模式10s左右可以变更ip重新获取key
通过浏览器打开链接获取:http://175.24.153.42:8882/getkey
uids:wxpusher的参数，当一个微信关注了一个wxpusher的推送应用后，会在推送管理后台(https://wxpusher.zjiecode.com/admin/main)的'用户管理-->用户列表'中显示
用户在推送页面点击’我的-->我的UID‘也可以获取
4.青龙环境变量菜单，添加本脚wxpusher环境变量(不需要重复添加)
export push_config="{'printf':0,'threadingf':1,'threadingt':3,'appToken':'xxxx'}"
参数说明：
printf:0是不打印调试日志，1是打印调试日志
threadingf:并行运行账号参数 1并行执行，0顺序执行，并行执行优点，能够并行跑所以账号，加快完成时间，缺点日志打印混乱。
threadingt:并行运行时每个账号的间隔时间默认3s
appToken 这个是填wxpusher的appToken,wxpusher如何使用可以百度
5.定时运行每半个小时一次
'''#line:42
import requests #line:43
import re #line:44
import random #line:45
import os #line:46
import threading #line:47
import json #line:48
import hashlib #line:49
import time #line:50
from urllib .parse import urlparse ,parse_qs #line:51
checkDict ={'ischeck':['检测标注','检测标注请勿修改'],'MzkwNTY1MzYxOQ==':['无无有歌','gh_7d594718e309'],}#line:55
push_num =[-1 ]#line:56
def getmsg ():#line:57
    global checkDict #line:58
    O0OOO0O0OOO00O000 ='v1.6f'#line:59
    try :#line:60
        OOOOO0O0OOOO0O000 ='http://175.24.153.42:8881/getmsg'#line:61
        OOOO00O0OOOOOOO0O ={'type':'zhyd'}#line:62
        O0O0OO000OO0OOO0O =requests .get (OOOOO0O0OOOO0O000 ,params =OOOO00O0OOOOOOO0O ,timeout =2 )#line:63
        OO0OOOO00OOOOOO00 =O0O0OO000OO0OOO0O .json ()#line:64
        O0OOO000OO00OOOO0 =OO0OOOO00OOOOOO00 .get ('version')#line:65
        OOO0O0OOO0O0OOOOO =OO0OOOO00OOOOOO00 .get ('gdict')#line:66
        OOO0OOO0O000O0000 =OO0OOOO00OOOOOO00 .get ('gmmsg')#line:67
        print ('系统公告:',OOO0OOO0O000O0000 )#line:68
        print (f'最新版本{O0OOO000OO00OOOO0},当前版本{O0OOO0O0OOO00O000}')#line:69
        print (f'系统的公众号字典{len(OOO0O0OOO0O0OOOOO)}个:{OOO0O0OOO0O0OOOOO}')#line:70
        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:71
        checkDict ={}#line:72
        for O00O0OOOO0OOOOOOO in OOO0O0OOO0O0OOOOO :#line:73
            checkDict .update ({O00O0OOOO0OOOOOOO :['','']})#line:74
    except Exception as OO00OOO00O000OOO0 :#line:75
        print (OO00OOO00O000OOO0 )#line:76
        print ('公告服务器异常')#line:77
def push (O00O00O0OO00OO0OO ,O0O0O0O000O0O0OO0 ,O00OO0O000OOOOO0O ,OO0OO0O0OOOOO0OO0 ,O0O0OOOOOO0O00O0O ,O0O0OOO00O00O0O0O ):#line:78
    O0OO0OO0OOO000O0O ='''
<body onload="window.location.href='LINK'">
<p>TEXT</p><br>
<p><a href="http://175.24.153.42:8882/lookstatus?key=KEY&type=TYPE">查看状态</a></p><br>
</body>
    '''#line:84
    O0O000O0OO0OO0OOO =O0OO0OO0OOO000O0O .replace ('TITTLE',O00O00O0OO00OO0OO ).replace ('LINK',O0O0O0O000O0O0OO0 ).replace ('TEXT',O00OO0O000OOOOO0O ).replace ('TYPE',OO0OO0O0OOOOO0OO0 ).replace ('KEY',O0O0OOO00O00O0O0O )#line:86
    OOO00O000O00O0O00 ={"appToken":appToken ,"content":O0O000O0OO0OO0OOO ,"summary":O00O00O0OO00OO0OO ,"contentType":2 ,"uids":[O0O0OOOOOO0O00O0O ]}#line:93
    OO00O000O00O000OO ='http://wxpusher.zjiecode.com/api/send/message'#line:94
    try :#line:95
        O000O00O00O00O0OO =requests .post (url =OO00O000O00O000OO ,json =OOO00O000O00O0O00 ).text #line:96
        print ('推送结果：',O000O00O00O00O0OO )#line:97
        return True #line:98
    except Exception as OOOOO0OOOOOO00OO0 :#line:99
        print ('推送失败！')#line:100
        print ('推送结果：',OOOOO0OOOOOO00OO0 )#line:101
        return False #line:102
def getinfo (OOOO00O0O0O00OO00 ):#line:103
    try :#line:104
        O0OO0OOO00OOOO0O0 ={'Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090b19) XWEB/9193 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language':'zh-CN,zh;q=0.9','Cookie':'rewardsn=; wxtokenkey=777; devicetype=Windows11x64; version=73020b18; lang=zh_CN;',}#line:111
        OOO00OO0O000OOO00 =requests .get (OOOO00O0O0O00OO00 ,headers =O0OO0OOO00OOOO0O0 )#line:112
        O0OO00O0000O00O00 =re .sub ('\s','',OOO00OO0O000OOO00 .text )#line:113
        O0OOOO00000OOOOO0 =re .findall ('varbiz="(.*?)"\|\|',O0OO00O0000O00O00 )#line:114
        if O0OOOO00000OOOOO0 !=[]:#line:115
            O0OOOO00000OOOOO0 =O0OOOO00000OOOOO0 [0 ]#line:116
        if O0OOOO00000OOOOO0 ==''or O0OOOO00000OOOOO0 ==[]:#line:117
            if '__biz'in OOOO00O0O0O00OO00 :#line:118
                O0OOOO00000OOOOO0 =re .findall ('__biz=(.*?)&',OOOO00O0O0O00OO00 )#line:119
                if O0OOOO00000OOOOO0 !=[]:#line:120
                    O0OOOO00000OOOOO0 =O0OOOO00000OOOOO0 [0 ]#line:121
        O000O00OOOO0O00O0 =re .findall ('varnickname=htmlDecode\("(.*?)"\);',O0OO00O0000O00O00 )#line:122
        if O000O00OOOO0O00O0 !=[]:#line:123
            O000O00OOOO0O00O0 =O000O00OOOO0O00O0 [0 ]#line:124
        O00O0O0OO00OOOOOO =re .findall ('varuser_name="(.*?)";',O0OO00O0000O00O00 )#line:125
        if O00O0O0OO00OOOOOO !=[]:#line:126
            O00O0O0OO00OOOOOO =O00O0O0OO00OOOOOO [0 ]#line:127
        O0OO0OOOO0O00OOO0 =re .findall ("varmsg_title='(.*?)'\.html\(",O0OO00O0000O00O00 )#line:128
        if O0OO0OOOO0O00OOO0 !=[]:#line:129
            O0OO0OOOO0O00OOO0 =O0OO0OOOO0O00OOO0 [0 ]#line:130
        O0O0000OOOOO0OOO0 =re .findall ("varoriCreateTime='(.*?)';",O0OO00O0000O00O00 )#line:131
        if O0O0000OOOOO0OOO0 !=[]:#line:132
            O0O0000OOOOO0OOO0 =O0O0000OOOOO0OOO0 [0 ]#line:133
        OO0O0000O0O0OOOOO =re .findall ("varcreateTime='(.*?)';",O0OO00O0000O00O00 )#line:134
        if OO0O0000O0O0OOOOO !=[]:#line:135
            OO0O0000O0O0OOOOO =OO0O0000O0O0OOOOO [0 ]#line:136
            OO0O0000O0O0OOOOO =OO0O0000O0O0OOOOO [:-5 ]+' '+OO0O0000O0O0OOOOO [-5 :]#line:137
        OOOO0O00OOOOO00OO =f'公众号唯一标识：{O0OOOO00000OOOOO0}|文章:{O0OO0OOOO0O00OOO0}|作者:{O000O00OOOO0O00O0}|账号:{O00O0O0OO00OOOOOO}|文章时间戳:{O0O0000OOOOO0OOO0}|文章时间:{OO0O0000O0O0OOOOO}'#line:138
        print (OOOO0O00OOOOO00OO )#line:139
        return O000O00OOOO0O00O0 ,O00O0O0OO00OOOOOO ,O0OO0OOOO0O00OOO0 ,OOOO0O00OOOOO00OO ,O0OOOO00000OOOOO0 ,O0O0000OOOOO0OOO0 ,OO0O0000O0O0OOOOO #line:140
    except Exception as O00O000O00OOO00O0 :#line:141
        print (O00O000O00OOO00O0 )#line:142
        print ('异常')#line:143
        return False #line:144
class WXYD :#line:145
    def __init__ (O00OOOO0OO0OO000O ,OO0O00OOOO00000OO ):#line:146
        O00OOOO0OO0OO000O .name =OO0O00OOOO00000OO ['name']#line:147
        O00OOOO0OO0OO000O .key =OO0O00OOOO00000OO ['key']#line:148
        O00OOOO0OO0OO000O .uids =OO0O00OOOO00000OO ['uids']#line:149
        O00OOOO0OO0OO000O .count =0 #line:150
        O00OOOO0OO0OO000O .User_Agent ='Mozilla/5.0 (Linux; Android 13; M2104K10AC Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110017 MMWEBSDK/20231002 MMWEBID/2545 MicroMessenger/8.0.43.2480(0x28112BE1) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64'#line:151
        OO00O00OO000OOO0O =O00OOOO0OO0OO000O .get_host ()#line:152
        O00OOOO0OO0OO000O .host =OO00O00OO000OOO0O [0 ]#line:153
        O00OOOO0OO0OO000O .t =OO00O00OO000OOO0O [1 ]#line:154
        O00OOOO0OO0OO000O .headers ={'Host':'m.zzyi4cf7z8.cn','Connection':'keep-alive','Accept':'application/json, text/plain, */*','X-Requested-With':'XMLHttpRequest','udtauth12':OO0O00OOOO00000OO ['udtauth12'],'User-Agent':O00OOOO0OO0OO000O .User_Agent ,'Origin':f'http://{O00OOOO0OO0OO000O.host}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':f'http://{O00OOOO0OO0OO000O.host}/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9',}#line:169
    def printjson (O0OO000OO0O0O0OOO ,OOO0OOO000000OOOO ):#line:170
        if printf ==0 :#line:171
            return False #line:172
        print (O0OO000OO0O0O0OOO .name ,OOO0OOO000000OOOO )#line:173
    def setstatus (OO00OOO00O0O0O00O ):#line:174
        try :#line:175
            O0O0000OO00OO0OOO ='http://175.24.153.42:8882/setstatus'#line:176
            O0O0O00OO0O0OO0OO ={'key':OO00OOO00O0O0O00O .key ,'type':'zhyd','val':'1','ven':oo0o }#line:177
            OOO0O0OO0O0OO00OO =requests .get (O0O0000OO00OO0OOO ,params =O0O0O00OO0O0OO0OO ,timeout =5 )#line:178
            print (OO00OOO00O0O0O00O .name ,OOO0O0OO0O0OO00OO .text )#line:179
            if '无效'in OOO0O0OO0O0OO00OO .text :#line:180
                exit (0 )#line:181
        except Exception as OOO0OO00OO0O0O0OO :#line:182
            print (OO00OOO00O0O0O00O .name ,'设置状态异常')#line:183
            print (OO00OOO00O0O0O00O .name ,OOO0OO00OO0O0O0OO )#line:184
            return 99 #line:185
    def getstatus (OO0OOOO00OO00OO0O ):#line:186
        try :#line:187
            OO00O0O00OOOOOO00 ='http://175.24.153.42:8882/getstatus'#line:188
            O0OO0O00OO0O000O0 ={'key':OO0OOOO00OO00OO0O .key ,'type':'zhyd'}#line:189
            O00OO0O0OOO000OOO =requests .get (OO00O0O00OOOOOO00 ,params =O0OO0O00OO0O000O0 ,timeout =3 )#line:190
            return O00OO0O0OOO000OOO .text #line:191
        except Exception as OOOO0O0OO00OO00OO :#line:192
            print (OO0OOOO00OO00OO0O .name ,'查询状态异常',OOOO0O0OO00OO00OO )#line:193
            return False #line:194
    def get_host (OO00000OOOOOO00O0 ):#line:195
        try :#line:196
            O0O0000O000OO0OO0 ='http://12318208252026.excqoef.cn/r?upuid=123182'#line:197
            O00000OOO000O00OO ={'Host':'12318208252026.excqoef.cn','Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':OO00000OOOOOO00O0 .User_Agent ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9',}#line:206
            OO0O000OO0O000OOO =requests .get (O0O0000O000OO0OO0 ,headers =O00000OOO000O00OO ,allow_redirects =False )#line:207
            if OO0O000OO0O000OOO .headers .get ('Location')!=None :#line:208
                OOOOOOOO0O0O0O0OO =urlparse (OO0O000OO0O000OOO .headers .get ('Location'))#line:209
                OO00O00O0OO0OO00O =OOOOOOOO0O0O0O0OO .netloc #line:210
                O0OOOOOO0O000OOO0 =re .findall (r't=(\d+)',OO0O000OO0O000OOO .headers .get ('Location'))[0 ]#line:211
                return OO00O00O0OO0OO00O ,O0OOOOOO0O000OOO0 #line:212
            else :#line:213
                print ('获取host失败0')#line:214
                return 'klluodi-04.obs.cn-jxnc1.ctyun.cn'#line:215
        except Exception as OOOO0OO0OOO000O00 :#line:216
            print ('获取host失败1',OOOO0OO0OOO000O00 )#line:217
            return 'klluodi-04.obs.cn-jxnc1.ctyun.cn'#line:218
    def tuijian (OOOOO0OO0O0OO0OO0 ):#line:219
        OOO00O00O0O0OOO0O =f'https://m.zzyi4cf7z8.cn/tuijian?url=upuid%3D123182%26t%3D{OOOOO0OO0O0OO0OO0.t}&upuid=123182'#line:220
        OOO00O0000O0O000O =requests .get (OOO00O00O0O0OOO0O ,headers =OOOOO0OO0O0OO0OO0 .headers )#line:221
        try :#line:222
            OOO000000OO000000 =OOO00O0000O0O000O .json ()#line:223
            if OOO000000OO000000 .get ('code')==0 :#line:224
                O000O000OO000OOO0 =OOO000000OO000000 ['data']['user']['username']#line:225
                O00OOOO0O00OO0000 =float (OOO000000OO000000 ['data']['user']['score'])/100 #line:226
                OOO0OO0O0O00O0O00 =OOO000000OO000000 ['data']['infoView'].get ('msg')#line:227
                O00OO0O00OOO0O000 =OOO000000OO000000 ['data']['infoView']['num']#line:228
                OOO0O000O00OOO00O =OOO000000OO000000 ['data']['infoView']['rest']#line:229
                if OOO0O000O00OOO00O ==0 :#line:230
                    print ('当前状态，可能是不可阅读')#line:231
                    print (OOOOO0OO0O0OO0OO0 .name ,f'{O000O000OO000OOO0}:当前剩余{O00OOOO0O00OO0000}元,今日已经阅读：{O00OO0O00OOO0O000}篇,提示信息：{OOO0OO0O0O00O0O00}')#line:232
                    return False #line:233
                print (OOOOO0OO0O0OO0OO0 .name ,f'{O000O000OO000OOO0}:当前剩余{O00OOOO0O00OO0000}元,今日已经阅读：{O00OO0O00OOO0O000}篇,提示信息：{OOO0OO0O0O00O0O00}')#line:234
                return True #line:235
            else :#line:236
                print (OOOOO0OO0O0OO0OO0 .name ,OOO000000OO000000 )#line:237
                print (OOOOO0OO0O0OO0OO0 .name ,'账号异常0,ck可能失效')#line:238
                return False #line:239
        except Exception as O00OO0O000O0OO0O0 :#line:240
            print (OOOOO0OO0O0OO0OO0 .name ,O00OO0O000O0OO0O0 )#line:241
            print (OOOOO0OO0O0OO0OO0 .name ,'账号异常1，ck可能失效')#line:242
            return False #line:243
    def get_read_url (OOOOOO00OOO000O00 ):#line:244
        O0O00O00OOO0000OO ='https://m.zzyi4cf7z8.cn/new/bbbbb'#line:245
        O0O0000000O0O00OO =requests .get (O0O00O00OOO0000OO ,headers =OOOOOO00OOO000O00 .headers )#line:246
        OO000O0000OOOOO00 =O0O0000000O0O00OO .json ()#line:247
        O0OOOO00O0000O0OO =OO000O0000OOOOO00 .get ('jump')#line:248
        OOOO0OO00O0O0OO00 =parse_qs (urlparse (O0OOOO00O0000O0OO ).query )#line:249
        O0O0O00O0OO0OOOO0 =urlparse (O0OOOO00O0000O0OO ).netloc #line:250
        OOO00OO0OOOO0OOOO =OOOO0OO00O0O0OO00 .get ('iu')[0 ]#line:251
        O0OO0OO0O0OOO000O ={'Host':OOOOOO00OOO000O00 .host ,'Connection':'keep-alive','User-Agent':OOOOOO00OOO000O00 .User_Agent ,'X-Requested-With':'XMLHttpRequest','Accept':'*/*','Origin':f'http://{O0O0O00O0OO0OOOO0}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':f'http://{O0O0O00O0OO0OOOO0}/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9',}#line:265
        return OOO00OO0OOOO0OOOO ,O0O0O00O0OO0OOOO0 ,O0OO0OO0O0OOO000O #line:266
    def do_read (O0OO0O0OOOOOOO000 ):#line:268
        O0OO00OOO00O0O00O =O0OO0O0OOOOOOO000 .get_read_url ()#line:269
        O0OO0O0OOOOOOO000 .jkey =''#line:270
        O00O00OO0O00O0O00 =0 #line:271
        while True :#line:272
            OOOO00O0000OOOOO0 =f'iu={O0OO00OOO00O0O00O[0]}&r={round(random.uniform(0, 1), 17)}&{O0OO0O0OOOOOOO000.jkey}'#line:274
            OO000OOOOOOO0OO00 ='https://m.zzyi4cf7z8.cn/dodoaa/mmaa?'+OOOO00O0000OOOOO0 #line:275
            O0OO0O0OOOOOOO000 .printjson (OO000OOOOOOO0OO00 )#line:276
            OO000OOOO0OO0OOO0 =requests .get (OO000OOOOOOO0OO00 ,headers =O0OO00OOO00O0O00O [2 ])#line:277
            print (O0OO0O0OOOOOOO000 .name ,'-'*50 )#line:278
            OOO0O0OO0OO0OO0OO =OO000OOOO0OO0OOO0 .json ()#line:279
            if OOO0O0OO0OO0OO0OO .get ('msg'):#line:280
                print (O0OO0O0OOOOOOO000 .name ,'弹出msg',OOO0O0OO0OO0OO0OO .get ('msg'))#line:281
            if OOO0O0OO0OO0OO0OO .get ('success_msg'):#line:282
                print (O0OO0O0OOOOOOO000 .name ,'成功msg',OOO0O0OO0OO0OO0OO .get ('msg'))#line:283
            OOOO00000O0OO0O00 =OOO0O0OO0OO0OO0OO .get ('url')#line:284
            O0OO0O0OOOOOOO000 .printjson (OOOO00000O0OO0O00 )#line:285
            if OOOO00000O0OO0O00 =='close':#line:286
                print (O0OO0O0OOOOOOO000 .name ,f'阅读结果结束')#line:287
                return True #line:288
            if 'http'in OOOO00000O0OO0O00 :#line:289
                O00O00OO0O00O0O00 +=1 #line:290
                print (O0OO0O0OOOOOOO000 .name ,f'上一篇阅读结果：{OOO0O0OO0OO0OO0OO.get("success_msg","第一篇开始阅读或者异常")}')#line:291
                O00OOOO0OOO00OO00 =OOO0O0OO0OO0OO0OO .get ('jkey')#line:292
                O0OO0O0OOOOOOO000 .jkey =f'&jkey={O00OOOO0OOO00OO00}'#line:293
                O00O0O000000OOOOO =getinfo (OOOO00000O0OO0O00 )#line:294
                if O00O00OO0O00O0O00 in push_num :#line:295
                    O00O0O0O00O0O00OO =list (O00O0O000000OOOOO )#line:296
                    O00O0O0O00O0O00OO [4 ]='ischeck'#line:297
                    if O0OO0O0OOOOOOO000 .testCheck (O00O0O0O00O0O00OO ,OOOO00000O0OO0O00 )==False :#line:298
                        return False #line:299
                else :#line:300
                    if O0OO0O0OOOOOOO000 .testCheck (O00O0O000000OOOOO ,OOOO00000O0OO0O00 )==False :#line:301
                        return False #line:302
                if O0OO0O0OOOOOOO000 .count >=5 :#line:303
                    print (O0OO0O0OOOOOOO000 .name ,'过检测超过4次中止阅读')#line:304
                    return False #line:305
                OO00O00O0OOOO00O0 =random .randint (6 ,9 )#line:306
                print (O0OO0O0OOOOOOO000 .name ,f'本次模拟读{OO00O00O0OOOO00O0}秒')#line:307
                time .sleep (OO00O00O0OOOO00O0 )#line:308
            else :#line:309
                print (O0OO0O0OOOOOOO000 .name ,'未知结果')#line:310
                print (O0OO0O0OOOOOOO000 .name ,OOO0O0OO0OO0OO0OO )#line:311
                break #line:312
    def testCheck (O0O0O0O0000OOO0OO ,OOOO0000O00O00OOO ,OO00O00O00O0O0OO0 ):#line:313
        if OOOO0000O00O00OOO [4 ]==[]:#line:314
            print (O0O0O0O0000OOO0OO .name ,'这个链接没有获取到微信号id',OO00O00O00O0O0OO0 )#line:315
            return True #line:316
        if (checkDict .get (OOOO0000O00O00OOO [4 ])!=None )or (int (time .time ())-int (OOOO0000O00O00OOO [5 ])>3600 *24 *14 ):#line:317
            O0O0O0O0000OOO0OO .count +=1 #line:318
            if O0O0O0O0000OOO0OO .setstatus ()==99 :#line:319
                print (O0O0O0O0000OOO0OO .name ,'过检测服务器异常，使用无回调方案，请在50s内阅读检测文章')#line:320
                push (f'可乐阅读过检测:{O0O0O0O0000OOO0OO.name}',OO00O00O00O0O0OO0 ,OOOO0000O00O00OOO [3 ],'zhyd',O0O0O0O0000OOO0OO .uids ,O0O0O0O0000OOO0OO .key )#line:321
                time .sleep (50 )#line:322
                return True #line:323
            for OOOOOO000OOO000O0 in range (60 ):#line:324
                if OOOOOO000OOO000O0 %30 ==0 :#line:325
                    O0O00OO00O000OO00 =f'http://175.24.153.42:8882/lookwxarticle?key=KEY&type=TYPE&wxurl={OO00O00O00O0O0OO0}'#line:326
                    push (f'可乐阅读过检测:{O0O0O0O0000OOO0OO.name}',O0O00OO00O000OO00 ,OOOO0000O00O00OOO [3 ],'zhyd',O0O0O0O0000OOO0OO .uids ,O0O0O0O0000OOO0OO .key )#line:327
                OOOOO0OO00OO000OO =O0O0O0O0000OOO0OO .getstatus ()#line:328
                if OOOOO0OO00OO000OO =='0':#line:329
                    print (O0O0O0O0000OOO0OO .name ,'过检测文章已经阅读')#line:330
                    return True #line:331
                elif OOOOO0OO00OO000OO =='1':#line:332
                    print (O0O0O0O0000OOO0OO .name ,f'正在等待过检测文章阅读结果{OOOOOO000OOO000O0}秒。。。')#line:333
                    time .sleep (1 )#line:334
                else :#line:335
                    print (O0O0O0O0000OOO0OO .name ,OOOOO0OO00OO000OO )#line:336
                    print (O0O0O0O0000OOO0OO .name ,'服务器异常')#line:337
            print (O0O0O0O0000OOO0OO .name ,'过检测超时中止脚本防止黑号')#line:338
            return False #line:339
        else :#line:340
            return True #line:341
    def withdrawal (O000000OO0OO0OOO0 ):#line:342
        O00O0O00O0OOOO0OO ='https://m.zzyi4cf7z8.cn/withdrawal'#line:343
        OO0O00O0OO0O00O0O =requests .get (O00O0O00O0OOOO0OO ,headers =O000000OO0OO0OOO0 .headers )#line:344
        O0OOO0OOOOO0O0OOO =OO0O00O0OO0O00O0O .json ()#line:345
        time .sleep (3 )#line:346
        if O0OOO0OOOOO0O0OOO .get ('code')==0 :#line:347
            O00OOOOO0O0000OOO =int (float (O0OOO0OOOOO0O0OOO ['data']['user']['score']))#line:348
            if O00OOOOO0O0000OOO <30 :#line:349
                print ('没有达到提现标标准')#line:350
                return False #line:351
            O0OO00OO00OO000OO =O000000OO0OO0OOO0 .headers .copy ()#line:352
            O0OO00OO00OO000OO .update ({'Content-Type':'application/x-www-form-urlencoded'})#line:353
            O00O0O00O0OOOO0OO ='https://m.zzyi4cf7z8.cn/withdrawal/doWithdraw'#line:354
            O0O0OO000OO00OO0O =f'amount={O00OOOOO0O0000OOO}&type=wx'#line:355
            OO0O00O0OO0O00O0O =requests .post (O00O0O00O0OOOO0OO ,headers =O0OO00OO00OO000OO ,data =O0O0OO000OO00OO0O )#line:356
            print (O000000OO0OO0OOO0 .name ,'提现结果',OO0O00O0OO0O00O0O .text )#line:357
        else :#line:358
            print ('提现异常')#line:359
            print (O000000OO0OO0OOO0 .name ,O0OOO0OOOOO0O0OOO )#line:360
    def run (O0000OO00000000OO ):#line:361
        if hashlib .md5 (oo0o .encode ()).hexdigest ()!='e08ca2eddd87fc6ddceba5e5491202bd':O0000OO00000000OO .setstatus ()#line:362
        if O0000OO00000000OO .tuijian ():#line:363
            time .sleep (2 )#line:364
            O0000OO00000000OO .get_read_url ()#line:365
            O0000OO00000000OO .do_read ()#line:366
            time .sleep (2 )#line:367
            O0000OO00000000OO .withdrawal ()#line:368
def getEnv (O0000O0OO0000OOOO ):#line:369
    O0O00OOOO0O00OOOO =os .getenv (O0000O0OO0000OOOO )#line:370
    if O0O00OOOO0O00OOOO ==None :#line:371
        print (f'{O0000O0OO0000OOOO}青龙变量里没有获取到，使用本地参数')#line:372
        return False #line:373
    try :#line:374
        O0O00OOOO0O00OOOO =json .loads (O0O00OOOO0O00OOOO .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:375
        return O0O00OOOO0O00OOOO #line:376
    except Exception as OO000OOO0O0O00O00 :#line:377
        print ('错误:',OO000OOO0O0O00O00 )#line:378
        print ('你填写的变量是:',O0O00OOOO0O00OOOO )#line:379
        print ('请检查变量参数是否填写正确')#line:380
        print (f'{O0000O0OO0000OOOO}使用本地参数')#line:381
if __name__ =='__main__':#line:382
    push_config = getEnv('push_config')
    klydconfig = getEnv('klydconfig')
    printf = push_config.get('printf',0)  # 打印调试日志0不打印，1打印，若运行异常请打开调试
    appToken = push_config['appToken']  # 这个是填wxpusher的appToken
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
