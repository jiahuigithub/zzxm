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

6.优化提现功能，新增支付宝提现共功能

启用支付宝提现，请在青龙菜单项《配置文件》，添加kltx环境变量

export kltx01="{'name':'李四','phone':'18888888888','limit_tx':50}"

参数说明：

name：支付宝用户姓名

phone：支付宝用户手机号

limit_tx：提现标准，单位为分，不能小于30分。自行参考设置。(仅对支付宝提现生效)

'''#line:46

import requests #line:47

import re #line:48

import random #line:49

import os #line:50

import threading #line:51

import json #line:52

import hashlib #line:53

import time #line:54

from urllib .parse import urlparse ,parse_qs ,quote #line:55

checkDict ={'ischeck':['检测标注','检测标注请勿修改'],'MzkwNTY1MzYxOQ==':['无无有歌','gh_7d594718e309'],}#line:59

push_num =[-1 ]#line:60

def getmsg ():#line:61

    global checkDict #line:62

    O000O00O00OOO0OO0 ='v1.1'#line:63

    try :#line:64

        OOOOO0O0OO000O00O ='http://175.24.153.42:8881/getmsg'#line:65

        O0O000000O0O00OOO ={'type':'zhyd'}#line:66

        OOOO00O0OOOOOOOOO =requests .get (OOOOO0O0OO000O00O ,params =O0O000000O0O00OOO ,timeout =2 )#line:67

        O000O0OO0OO0OOOOO =OOOO00O0OOOOOOOOO .json ()#line:68

        OOOO0O00000O0O0O0 =O000O0OO0OO0OOOOO .get ('version')#line:69

        O0OOOOOO00OO000O0 =O000O0OO0OO0OOOOO .get ('gdict')#line:70

        O0O00O0OO0000O000 =O000O0OO0OO0OOOOO .get ('gmmsg')#line:71

        print ('系统公告:',O0O00O0OO0000O000 )#line:72

        print (f'最新版本{OOOO0O00000O0O0O0},当前版本{O000O00O00OOO0OO0}')#line:73

        if O000O00O00OOO0OO0 !=OOOO0O00000O0O0O0 :#line:74

            print ('版本不一致，可能要更新脚本了')#line:75

        print (f'系统的公众号字典{len(O0OOOOOO00OO000O0)}个:{O0OOOOOO00OO000O0}')#line:76

        print (f'本脚本公众号字典{len(checkDict.values())}个:{list(checkDict.keys())}')#line:77

        checkDict ={}#line:78

        for O0O00OO0000O000O0 in O0OOOOOO00OO000O0 :#line:79

            checkDict .update ({O0O00OO0000O000O0 :['','']})#line:80

    except Exception as OOOO0OO0O0OOO0O00 :#line:81

        print (OOOO0OO0O0OOO0O00 )#line:82

        print ('公告服务器异常')#line:83

def push (OOO00O0O0OO0O0O0O ,OOO000OOO00OOOO0O ,OOOO0OOOO0OOO0OOO ,OOOO0O000000OO0O0 ,OOOO000OOOOOOOOOO ,OO0O0O000O0O0O0O0 ):#line:84

    O000OO0OOOOO0O0OO ='''

<body onload="window.location.href='LINK'">

<p>TEXT</p><br>

<p><a href="http://175.24.153.42:8882/lookstatus?key=KEY&type=TYPE">查看状态</a></p><br>

</body>

    '''#line:90

    OOO0OOO0O0OOOO0O0 =O000OO0OOOOO0O0OO .replace ('TITTLE',OOO00O0O0OO0O0O0O ).replace ('LINK',OOO000OOO00OOOO0O ).replace ('TEXT',OOOO0OOOO0OOO0OOO ).replace ('TYPE',OOOO0O000000OO0O0 ).replace ('KEY',OO0O0O000O0O0O0O0 )#line:92

    OO000OOOOO0O00000 ={"appToken":appToken ,"content":OOO0OOO0O0OOOO0O0 ,"summary":OOO00O0O0OO0O0O0O ,"contentType":2 ,"uids":[OOOO000OOOOOOOOOO ]}#line:99

    OOOO0OOO00O0O0000 ='http://wxpusher.zjiecode.com/api/send/message'#line:100

    try :#line:101

        OOO000O0OOOOOO0O0 =requests .post (url =OOOO0OOO00O0O0000 ,json =OO000OOOOO0O00000 ).text #line:102

        print ('推送结果：',OOO000O0OOOOOO0O0 )#line:103

        return True #line:104

    except Exception as O0OO00OOOOO000O0O :#line:105

        print ('推送失败！')#line:106

        print ('推送结果：',O0OO00OOOOO000O0O )#line:107

        return False #line:108

def getinfo (OO000000O0O00O0O0 ):#line:109

    try :#line:110

        OOOOO0O0OOOOOOOOO ={'Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090b19) XWEB/9193 Flue','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language':'zh-CN,zh;q=0.9','Cookie':'rewardsn=; wxtokenkey=777; devicetype=Windows11x64; version=73020b18; lang=zh_CN;',}#line:117

        OOO0O0OOOO00OOO00 =requests .get (OO000000O0O00O0O0 ,headers =OOOOO0O0OOOOOOOOO )#line:118

        O0O000O0000000OOO =re .sub ('\s','',OOO0O0OOOO00OOO00 .text )#line:119

        OO0OOO0OO00000000 =re .findall ('varbiz="(.*?)"\|\|',O0O000O0000000OOO )#line:120

        if OO0OOO0OO00000000 !=[]:#line:121

            OO0OOO0OO00000000 =OO0OOO0OO00000000 [0 ]#line:122

        if OO0OOO0OO00000000 ==''or OO0OOO0OO00000000 ==[]:#line:123

            if '__biz'in OO000000O0O00O0O0 :#line:124

                OO0OOO0OO00000000 =re .findall ('__biz=(.*?)&',OO000000O0O00O0O0 )#line:125

                if OO0OOO0OO00000000 !=[]:#line:126

                    OO0OOO0OO00000000 =OO0OOO0OO00000000 [0 ]#line:127

        O00O0OO000000OOO0 =re .findall ('varnickname=htmlDecode\("(.*?)"\);',O0O000O0000000OOO )#line:128

        if O00O0OO000000OOO0 !=[]:#line:129

            O00O0OO000000OOO0 =O00O0OO000000OOO0 [0 ]#line:130

        O00OOOO00OO0OO00O =re .findall ('varuser_name="(.*?)";',O0O000O0000000OOO )#line:131

        if O00OOOO00OO0OO00O !=[]:#line:132

            O00OOOO00OO0OO00O =O00OOOO00OO0OO00O [0 ]#line:133

        OO0O0O0O0OO000O0O =re .findall ("varmsg_title='(.*?)'\.html\(",O0O000O0000000OOO )#line:134

        if OO0O0O0O0OO000O0O !=[]:#line:135

            OO0O0O0O0OO000O0O =OO0O0O0O0OO000O0O [0 ]#line:136

        OO0000000000OO0O0 =re .findall ("varoriCreateTime='(.*?)';",O0O000O0000000OOO )#line:137

        if OO0000000000OO0O0 !=[]:#line:138

            OO0000000000OO0O0 =OO0000000000OO0O0 [0 ]#line:139

        O0O00OOO0O0OOO0O0 =re .findall ("varcreateTime='(.*?)';",O0O000O0000000OOO )#line:140

        if O0O00OOO0O0OOO0O0 !=[]:#line:141

            O0O00OOO0O0OOO0O0 =O0O00OOO0O0OOO0O0 [0 ]#line:142

            O0O00OOO0O0OOO0O0 =O0O00OOO0O0OOO0O0 [:-5 ]+' '+O0O00OOO0O0OOO0O0 [-5 :]#line:143

        OO0OOO000000OO00O =f'公众号唯一标识：{OO0OOO0OO00000000}|文章:{OO0O0O0O0OO000O0O}|作者:{O00O0OO000000OOO0}|账号:{O00OOOO00OO0OO00O}|文章时间戳:{OO0000000000OO0O0}|文章时间:{O0O00OOO0O0OOO0O0}'#line:144

        print (OO0OOO000000OO00O )#line:145

        return O00O0OO000000OOO0 ,O00OOOO00OO0OO00O ,OO0O0O0O0OO000O0O ,OO0OOO000000OO00O ,OO0OOO0OO00000000 ,OO0000000000OO0O0 ,O0O00OOO0O0OOO0O0 #line:146

    except Exception as O0000OO0O0O0O0OOO :#line:147

        print (O0000OO0O0O0O0OOO )#line:148

        print ('异常')#line:149

        return False #line:150

class WXYD :#line:151

    def __init__ (OOOO0OOO0O0O000OO ,O0O0OO000O00OO000 ):#line:152

        OOOO0OOO0O0O000OO .name =O0O0OO000O00OO000 ['name']#line:153

        OOOO0OOO0O0O000OO .key =O0O0OO000O00OO000 ['key']#line:154

        OOOO0OOO0O0O000OO .uids =O0O0OO000O00OO000 ['uids']#line:155

        OOOO0OOO0O0O000OO .count =0 #line:156

        OOOO0OOO0O0O000OO .User_Agent ='Mozilla/5.0 (Linux; Android 13; M2104K10AC Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110017 MMWEBSDK/20231002 MMWEBID/2545 MicroMessenger/8.0.43.2480(0x28112BE1) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64'#line:157

        O0O00000OO0OOO00O =OOOO0OOO0O0O000OO .get_host ()#line:158

        OOOO0OOO0O0O000OO .host =O0O00000OO0OOO00O [0 ]#line:159

        OOOO0OOO0O0O000OO .t =O0O00000OO0OOO00O [1 ]#line:160

        OOOO0OOO0O0O000OO .headers ={'Host':'m.zzyi4cf7z8.cn','Connection':'keep-alive','Accept':'application/json, text/plain, */*','X-Requested-With':'XMLHttpRequest','udtauth12':O0O0OO000O00OO000 ['udtauth12'],'User-Agent':OOOO0OOO0O0O000OO .User_Agent ,'Origin':f'http://{OOOO0OOO0O0O000OO.host}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':f'http://{OOOO0OOO0O0O000OO.host}/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9',}#line:175

    def printjson (O0O000O0O00OOOOO0 ,OO0O00OO00O00O00O ):#line:176

        if printf ==0 :#line:177

            return False #line:178

        print (O0O000O0O00OOOOO0 .name ,OO0O00OO00O00O00O )#line:179

    def setstatus (O0OO0O0OOO00OO000 ):#line:180

        try :#line:181

            OO0O000OO00OO00O0 ='http://175.24.153.42:8882/setstatus'#line:182

            OO0O00O00OO00O000 ={'key':O0OO0O0OOO00OO000 .key ,'type':'zhyd','val':'1','ven':oo0o }#line:183

            O00O0OO000OO000OO =requests .get (OO0O000OO00OO00O0 ,params =OO0O00O00OO00O000 ,timeout =5 )#line:184

            print (O0OO0O0OOO00OO000 .name ,O00O0OO000OO000OO .text )#line:185

            if '无效'in O00O0OO000OO000OO .text :#line:186

                exit (0 )#line:187

        except Exception as OOO0000O0O0O0O0OO :#line:188

            print (O0OO0O0OOO00OO000 .name ,'设置状态异常')#line:189

            print (O0OO0O0OOO00OO000 .name ,OOO0000O0O0O0O0OO )#line:190

            return 99 #line:191

    def getstatus (O0OO0000OOO000O0O ):#line:192

        try :#line:193

            O00O00OOO000OO000 ='http://175.24.153.42:8882/getstatus'#line:194

            O000OOO0000OOO000 ={'key':O0OO0000OOO000O0O .key ,'type':'zhyd'}#line:195

            OOOOOOOOO00O000O0 =requests .get (O00O00OOO000OO000 ,params =O000OOO0000OOO000 ,timeout =3 )#line:196

            return OOOOOOOOO00O000O0 .text #line:197

        except Exception as O00OOO0O000O0OOO0 :#line:198

            print (O0OO0000OOO000O0O .name ,'查询状态异常',O00OOO0O000O0OOO0 )#line:199

            return False #line:200

    def get_host (O0OOO00OOOO0O0000 ):#line:201

        try :#line:202

            OOOOO00OOOO0000O0 ='http://12318208252026.excqoef.cn/r?upuid=123182'#line:203

            O00OO00O0O000O00O ={'Host':'12318208252026.excqoef.cn','Connection':'keep-alive','Upgrade-Insecure-Requests':'1','User-Agent':O0OOO00OOOO0O0000 .User_Agent ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9',}#line:212

            O0000OOOOO0OO0OOO =requests .get (OOOOO00OOOO0000O0 ,headers =O00OO00O0O000O00O ,allow_redirects =False )#line:213

            if O0000OOOOO0OO0OOO .headers .get ('Location')!=None :#line:214

                O0000O0000O0OOOO0 =urlparse (O0000OOOOO0OO0OOO .headers .get ('Location'))#line:215

                O000O0O000O000O00 =O0000O0000O0OOOO0 .netloc #line:216

                OOOOO0OOO00OO0000 =re .findall (r't=(\d+)',O0000OOOOO0OO0OOO .headers .get ('Location'))[0 ]#line:217

                return O000O0O000O000O00 ,OOOOO0OOO00OO0000 #line:218

            else :#line:219

                print ('获取host失败0')#line:220

                return 'klluodi-04.obs.cn-jxnc1.ctyun.cn'#line:221

        except Exception as O00O0OO00O0OOO0O0 :#line:222

            print ('获取host失败1',O00O0OO00O0OOO0O0 )#line:223

            return 'klluodi-04.obs.cn-jxnc1.ctyun.cn'#line:224

    def tuijian (OO0OOO0OOO0000O00 ):#line:225

        OO0OOOOO0OOO0OO0O =f'https://m.zzyi4cf7z8.cn/tuijian?url=upuid%3D123182%26t%3D{OO0OOO0OOO0000O00.t}&upuid=123182'#line:226

        OO00000O000OO0O00 =requests .get (OO0OOOOO0OOO0OO0O ,headers =OO0OOO0OOO0000O00 .headers )#line:227

        try :#line:228

            O0OOO0O0O00OOO000 =OO00000O000OO0O00 .json ()#line:229

            if O0OOO0O0O00OOO000 .get ('code')==0 :#line:230

                O000O000OO0OO0O0O =O0OOO0O0O00OOO000 ['data']['user']['username']#line:231

                OOOO00OOO0OOO0OOO =float (O0OOO0O0O00OOO000 ['data']['user']['score'])/100 #line:232

                OOOOO00OO0O0O000O =O0OOO0O0O00OOO000 ['data']['infoView'].get ('msg')#line:233

                O0O00OO0OOO0OOO0O =O0OOO0O0O00OOO000 ['data']['infoView']['num']#line:234

                O0OO00OO0000OOOO0 =O0OOO0O0O00OOO000 ['data']['infoView']['rest']#line:235

                if O0OO00OO0000OOOO0 ==0 :#line:236

                    print ('当前状态，可能是不可阅读')#line:237

                    print (OO0OOO0OOO0000O00 .name ,f'{O000O000OO0OO0O0O}:当前剩余{OOOO00OOO0OOO0OOO}元,今日已经阅读：{O0O00OO0OOO0OOO0O}篇,提示信息：{OOOOO00OO0O0O000O}')#line:238

                    return False #line:239

                print (OO0OOO0OOO0000O00 .name ,f'{O000O000OO0OO0O0O}:当前剩余{OOOO00OOO0OOO0OOO}元,今日已经阅读：{O0O00OO0OOO0OOO0O}篇,提示信息：{OOOOO00OO0O0O000O}')#line:240

                return True #line:241

            else :#line:242

                print (OO0OOO0OOO0000O00 .name ,O0OOO0O0O00OOO000 )#line:243

                print (OO0OOO0OOO0000O00 .name ,'账号异常0,ck可能失效')#line:244

                return False #line:245

        except Exception as OO000O0000OOOOOO0 :#line:246

            print (OO0OOO0OOO0000O00 .name ,OO000O0000OOOOOO0 )#line:247

            print (OO0OOO0OOO0000O00 .name ,'账号异常1，ck可能失效')#line:248

            return False #line:249

    def get_read_url (OO0000000OO0O00OO ):#line:250

        OOO00O00O00OOO00O ='https://m.zzyi4cf7z8.cn/new/bbbbb'#line:251

        OOO0O00000O0OO000 =requests .get (OOO00O00O00OOO00O ,headers =OO0000000OO0O00OO .headers )#line:252

        O0O000OO00OOO00O0 =OOO0O00000O0OO000 .json ()#line:253

        OO0OO000OO0O0000O =O0O000OO00OOO00O0 .get ('jump')#line:254

        OO0000O000O0O00O0 =parse_qs (urlparse (OO0OO000OO0O0000O ).query )#line:255

        OOO0OOOOOO0O0O00O =urlparse (OO0OO000OO0O0000O ).netloc #line:256

        O0O0O0OOO0OOO0OO0 =OO0000O000O0O00O0 .get ('iu')[0 ]#line:257

        OOOO00000OOO00000 ={'Host':OO0000000OO0O00OO .host ,'Connection':'keep-alive','User-Agent':OO0000000OO0O00OO .User_Agent ,'X-Requested-With':'XMLHttpRequest','Accept':'*/*','Origin':f'http://{OOO0OOOOOO0O0O00O}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':f'http://{OOO0OOOOOO0O0O00O}/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9',}#line:271

        return O0O0O0OOO0OOO0OO0 ,OOO0OOOOOO0O0O00O ,OOOO00000OOO00000 #line:272

    def do_read (OOO0O000O0OO0O00O ):#line:274

        OO00O0OO000O000OO =OOO0O000O0OO0O00O .get_read_url ()#line:275

        OOO0O000O0OO0O00O .jkey =''#line:276

        OO0000OO000OOOOOO =0 #line:277

        while True :#line:278

            OOOO00OOOO00OOO0O =f'iu={OO00O0OO000O000OO[0]}&r={round(random.uniform(0, 1), 17)}&{OOO0O000O0OO0O00O.jkey}'#line:280

            OO0O0O0O00OOO0O0O ='https://m.zzyi4cf7z8.cn/dodoaa/mmaa?'+OOOO00OOOO00OOO0O #line:281

            OOO0O000O0OO0O00O .printjson (OO0O0O0O00OOO0O0O )#line:282

            O000000O0O0OO0O0O =requests .get (OO0O0O0O00OOO0O0O ,headers =OO00O0OO000O000OO [2 ])#line:283

            print (OOO0O000O0OO0O00O .name ,'-'*50 )#line:284

            OO0OO0O0OO0000OOO =O000000O0O0OO0O0O .json ()#line:285

            if OO0OO0O0OO0000OOO .get ('msg'):#line:286

                print (OOO0O000O0OO0O00O .name ,'弹出msg',OO0OO0O0OO0000OOO .get ('msg'))#line:287

            if OO0OO0O0OO0000OOO .get ('success_msg'):#line:288

                print (OOO0O000O0OO0O00O .name ,'成功msg',OO0OO0O0OO0000OOO .get ('msg'))#line:289

            O0OO0000O00OO0OOO =OO0OO0O0OO0000OOO .get ('url')#line:290

            OOO0O000O0OO0O00O .printjson (O0OO0000O00OO0OOO )#line:291

            if O0OO0000O00OO0OOO =='close':#line:292

                print (OOO0O000O0OO0O00O .name ,f'阅读结果结束')#line:293

                return True #line:294

            if 'http'in O0OO0000O00OO0OOO :#line:295

                OO0000OO000OOOOOO +=1 #line:296

                print (OOO0O000O0OO0O00O .name ,f'上一篇阅读结果：{OO0OO0O0OO0000OOO.get("success_msg","第一篇开始阅读或者异常")}')#line:297

                O0000O0O00O00O00O =OO0OO0O0OO0000OOO .get ('jkey')#line:298

                OOO0O000O0OO0O00O .jkey =f'&jkey={O0000O0O00O00O00O}'#line:299

                OO0OOO00O00000O0O =getinfo (O0OO0000O00OO0OOO )#line:300

                if OO0000OO000OOOOOO in push_num :#line:301

                    O0O00OOOO0OO000OO =list (OO0OOO00O00000O0O )#line:302

                    O0O00OOOO0OO000OO [4 ]='ischeck'#line:303

                    if OOO0O000O0OO0O00O .testCheck (O0O00OOOO0OO000OO ,O0OO0000O00OO0OOO )==False :#line:304

                        return False #line:305

                else :#line:306

                    if OOO0O000O0OO0O00O .testCheck (OO0OOO00O00000O0O ,O0OO0000O00OO0OOO )==False :#line:307

                        return False #line:308

                if OOO0O000O0OO0O00O .count >=5 :#line:309

                    print (OOO0O000O0OO0O00O .name ,'过检测超过4次中止阅读')#line:310

                    return False #line:311

                OO00OO0OO0000O0OO =random .randint (6 ,9 )#line:312

                print (OOO0O000O0OO0O00O .name ,f'本次模拟读{OO00OO0OO0000O0OO}秒')#line:313

                time .sleep (OO00OO0OO0000O0OO )#line:314

            else :#line:315

                print (OOO0O000O0OO0O00O .name ,'未知结果')#line:316

                print (OOO0O000O0OO0O00O .name ,OO0OO0O0OO0000OOO )#line:317

                break #line:318

    def testCheck (O0O0O000000O0000O ,OO00O0O0O00OOOO00 ,OOOOOOOO00O0OO0O0 ):#line:319

        if OO00O0O0O00OOOO00 [4 ]==[]:#line:320

            print (O0O0O000000O0000O .name ,'这个链接没有获取到微信号id',OOOOOOOO00O0OO0O0 )#line:321

            return True #line:322

        if OO00O0O0O00OOOO00 [5 ]==[]:#line:323

            print (O0O0O000000O0000O .name ,'这个链接没有获取到时间',OOOOOOOO00O0OO0O0 )#line:324

            return True #line:325

        if (checkDict .get (OO00O0O0O00OOOO00 [4 ])!=None )or (int (time .time ())-int (OO00O0O0O00OOOO00 [5 ])>3600 *24 *14 ):#line:326

            O0O0O000000O0000O .count +=1 #line:327

            if O0O0O000000O0000O .setstatus ()==99 :#line:328

                print (O0O0O000000O0000O .name ,'过检测服务器异常，使用无回调方案，请在50s内阅读检测文章')#line:329

                push (f'可乐阅读过检测:{O0O0O000000O0000O.name}',OOOOOOOO00O0OO0O0 ,OO00O0O0O00OOOO00 [3 ],'zhyd',O0O0O000000O0000O .uids ,O0O0O000000O0000O .key )#line:330

                time .sleep (50 )#line:331

                return True #line:332

            for OO0OOO0O0OO0O0000 in range (60 ):#line:333

                if OO0OOO0O0OO0O0000 %30 ==0 :#line:334

                    O000O0OOO0O0O0O0O =f'http://175.24.153.42:8882/lookwxarticle?key=KEY&type=TYPE&wxurl={OOOOOOOO00O0OO0O0}'#line:335

                    push (f'可乐阅读过检测:{O0O0O000000O0000O.name}',O000O0OOO0O0O0O0O ,OO00O0O0O00OOOO00 [3 ],'zhyd',O0O0O000000O0000O .uids ,O0O0O000000O0000O .key )#line:336

                OOO00O00OOOOOOOO0 =O0O0O000000O0000O .getstatus ()#line:337

                if OOO00O00OOOOOOOO0 =='0':#line:338

                    print (O0O0O000000O0000O .name ,'过检测文章已经阅读')#line:339

                    return True #line:340

                elif OOO00O00OOOOOOOO0 =='1':#line:341

                    print (O0O0O000000O0000O .name ,f'正在等待过检测文章阅读结果{OO0OOO0O0OO0O0000}秒。。。')#line:342

                    time .sleep (1 )#line:343

                else :#line:344

                    print (O0O0O000000O0000O .name ,OOO00O00OOOOOOOO0 )#line:345

                    print (O0O0O000000O0000O .name ,'服务器异常')#line:346

            print (O0O0O000000O0000O .name ,'过检测超时中止脚本防止黑号')#line:347

            return False #line:348

        else :#line:349

            return True #line:350

    def withdrawal (OO0OOO0000000OOOO ):#line:351

        O0OO000000O00O0O0 ='https://m.zzyi4cf7z8.cn/withdrawal'#line:352

        OOO00O0O0O00OO000 =requests .get (O0OO000000O00O0O0 ,headers =OO0OOO0000000OOOO .headers )#line:353

        O0000OO0OOO00O0OO =OOO00O0O0O00OO000 .json ()#line:354

        time .sleep (3 )#line:355

        if O0000OO0OOO00O0OO .get ('code')==0 :#line:356

            OOO0000O0OOOOOO00 =int (float (O0000OO0OOO00O0OO ['data']['user']['score']))#line:357

            if OOO0000O0OOOOOO00 <30 :#line:358

                print ('没有达到提现标标准')#line:359

                return False #line:360

            if OOO0000O0OOOOOO00 >=2000 :#line:361

                OOO0000O0OOOOOO00 =2000 #line:362

            O0O0O000OOOO0O0O0 =OO0OOO0000000OOOO .headers .copy ()#line:363

            O0O0O000OOOO0O0O0 .update ({'Content-Type':'application/x-www-form-urlencoded'})#line:364

            OO0OO000O0O00OO0O =os .getenv ('kltx01')#line:365

            if OO0OO000O0O00OO0O ==None :#line:366

                OOOO0000O0OO00000 =f'amount={OOO0000O0OOOOOO00}&type=wx'#line:367

            else :#line:368

                OOOOOOOOOOOOO0O0O =json .loads (OO0OO000O0O00OO0O .replace ("'",'"'))#line:369

                if OOO0000O0OOOOOO00 <int (OOOOOOOOOOOOO0O0O .get ('limit_tx')):#line:370

                    print ('没有达到你设置的提现标标准')#line:371

                    return False #line:372

                OOOO0000O0OO00000 =f'amount={OOO0000O0OOOOOO00}&type=ali&u_ali_account={OOOOOOOOOOOOO0O0O.get("phone")}&u_ali_real_name={quote(OOOOOOOOOOOOO0O0O.get("name"))}'#line:373

            O0OO000000O00O0O0 ='https://m.zzyi4cf7z8.cn/withdrawal/doWithdraw'#line:374

            OOO00O0O0O00OO000 =requests .post (O0OO000000O00O0O0 ,headers =O0O0O000OOOO0O0O0 ,data =OOOO0000O0OO00000 )#line:375

            print (OO0OOO0000000OOOO .name ,'提现结果',OOO00O0O0O00OO000 .text )#line:376

        else :#line:377

            print ('提现异常')#line:378

            print (OO0OOO0000000OOOO .name ,O0000OO0OOO00O0OO )#line:379

    def run (O00OOOOO000O0O0OO ):#line:380

        if hashlib .md5 (oo0o .encode ()).hexdigest ()!='e08ca2eddd87fc6ddceba5e5491202bd':O00OOOOO000O0O0OO .setstatus ()#line:381

        if O00OOOOO000O0O0OO .tuijian ():#line:382

            time .sleep (2 )#line:383

            O00OOOOO000O0O0OO .get_read_url ()#line:384

            O00OOOOO000O0O0OO .do_read ()#line:385

            time .sleep (2 )#line:386

            O00OOOOO000O0O0OO .withdrawal ()#line:387

def getEnv (OO0OOOO000O000OOO ):#line:388

    O0O000000O0O00O0O =os .getenv (OO0OOOO000O000OOO )#line:389

    if O0O000000O0O00O0O ==None :#line:390

        print (f'{OO0OOOO000O000OOO}青龙变量里没有获取到，使用本地参数')#line:391

        return False #line:392

    try :#line:393

        O0O000000O0O00O0O =json .loads (O0O000000O0O00O0O .replace ("'",'"').replace ("\n","").replace (" ","").replace ("\t",""))#line:394

        return O0O000000O0O00O0O #line:395

    except Exception as O0OO00O0000OO0000 :#line:396

        print ('错误:',O0OO00O0000OO0000 )#line:397

        print ('你填写的变量是:',O0O000000O0O00O0O )#line:398

        print ('请检查变量参数是否填写正确')#line:399

        print (f'{OO0OOOO000O000OOO}使用本地参数')#line:400

if __name__ =='__main__':#line:401

    push_config =getEnv ('push_config')#line:407

    klydconfig =getEnv ('klydconfig')#line:408

    printf =push_config .get ('printf',0 )#line:409

    appToken =push_config ['appToken']#line:410

    threadingf =push_config .get ('threadingf',1 )#line:411

    getmsg ()#line:412

    if threadingf ==1 :#line:413

        tl =[]#line:414

        for cg in klydconfig :#line:415

            print ('*'*50 )#line:416

            print (f'开始执行{cg["name"]}')#line:417

            api =WXYD (cg )#line:418

            t =threading .Thread (target =api .run ,args =())#line:419

            tl .append (t )#line:420

            t .start ()#line:421

            threadingt =push_config .get ('threadingt',3 )#line:422

            time .sleep (threadingt )#line:423

        for t in tl :#line:424

            t .join ()#line:425

    elif threadingf ==0 :#line:426

        for cg in klydconfig :#line:427

            print ('*'*50 )#line:428

            print (f'开始执行{cg["name"]}')#line:429

            api =WXYD (cg )#line:430

            api .run ()#line:431

            print (f'{cg["name"]}执行完毕')#line:432

            time .sleep (3 )#line:433

    else :#line:434

        print ('请确定推送变量中threadingf参数是否正确')#line:435

    print ('全部账号执行完成')#line:436

    time .sleep (10 )#line:437

