# 中青提现
# json文件格式如下：[{"ua": "ua", "body": {"access": "wifi", "app_version": "2.8.2"}}]#抓提现包里面的body处理成字典后放入，json不支持注释，运行前删除json文件中的注释
import json
import requests
import time
response = requests.get("https://mkjt.jdmk.xyz/mkjt.txt")
response.encoding = 'utf-8'
txt = response.text
print(txt)

def read_json_file():
    with open('zq.json','r') as f:
        json_data = json.load(f)
    return json_data

def write_json_file(json_data):
    with open('zq.json','w') as f:
        f.write(json.dumps(json_data))

def get_withdraw(ua,body) :
    withdraw_headers = {'Accept-Language': 'zh-CN', 'user-agent': ua, 'Referer': 'https://quickapp.cn/com.youth.kandianquickapp/170/page-frame.html', 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'Content-Length': '485', 'Host': 'user.youth.cn', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'}
    url = "https://user.youth.cn/FastApi/Alipay/withdraw.json"
    res = requests.post(url,data=body,headers=withdraw_headers).json()
    print(res)
    if res['error_code'] == '0' :
        print('提现0.3成功')
    elif res['error_code'] == 200009 :
        print('每日任务未完成')
    elif res['error_code'] == 200006 :
        print('今日已提现')
    elif res['error_code'] == 200010 :
        body['money'] = '1'
        res = requests.post(url,data=body,headers=withdraw_headers).json()
        if res['error_code'] == 0 :
            print('提现1成功')
        else :
            print('未知错误', res['items']['text'])
    else :
        print('未知错误', res['items']['text'])

def daily_task(ua,body):
    headers = {'Accept-Language': 'zh-CN', 'user-agent': ua, 'Referer': 'https://quickapp.cn/com.youth.kandianquickapp/170/page-frame.html', 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'Content-Length': '517', 'Host': 'user.youth.cn', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'}
    url = 'https://user.youth.cn/FastApi/article/shareEnd.json'
    s_body = body.copy()
    s_body['stype'] = 'WEIXIN'
    s_body['custom'] = 'native'
    s_body['article_id'] = '52279272' #获取文章id待写
    s_body['device_platform'] = 'android'
    del s_body['type'],s_body['add_desktop'],s_body['money'],s_body['is_login']
    res = requests.post(url,data=s_body,headers=headers).json()
    if res['error_code'] == '0' :
        print('转发成功，5s后尝试提现')
        return True
    else :
        print('未知错误', res['message'])
        return False


datas = read_json_file()
i = 0
print(f'共{len(datas)}个账号')
for data in datas :
    try :
        i += 1
        print(f'开始运行第{i}个账号')
        if daily_task(data['ua'],data['body']) :
            time.sleep(5)
            get_withdraw(data['ua'],data['body'])
        else :
            print('每日任务尝试完成失败，跳过提现')
        print('30s后下一个账号')
        time.sleep(30)
    except Exception as e:
        print('错误：',e)
        print('10s后尝试下一账号')
        time.sleep(10)
