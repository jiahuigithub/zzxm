#1. 微信小程序搜索兴攀农场官方进入后微信授权登陆
#2.然后直接打开抓包工具再进入小程序浇水点几下抓p.xpfarm.cn下的Authorization值
#3.提交格式：Authorization全部值为你抓的参数值便可。示列：b0c1c4e1f0f3e4cc376da49deb2130xx
import requests
import os
import time
import random
import concurrent.futures
response = requests.get("https://mkjt.jdmk.xyz/mkjt.txt")
response.encoding = 'utf-8'
txt = response.text
print(txt)


def Advertisingwilldrop(token):  # 广告水滴
    url = "https://p.xpfarm.cn/treemp/tree.Tasks/completeTask"
    headers = {
        "Host": "p.xpfarm.cn",
        "Connection": "keep-alive",
        "Content-Length": "13",
        "authorization": token,
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "contenttype": "[object Undefined]",
        "Referer": "https://servicewechat.com/wx27e219ff3142b7c8/59/page-frame.html"
    }
    data = {"task_id": 1}
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    message = response_data['message']
    print(f"广告观看结果→{message}")
    time.sleep(random.randint(30, 40))
def Advertisementwaterdropcollection(token):  # 广告水滴领取
    url = "https://p.xpfarm.cn/treemp/tree.Tasks/receiveTaskReward"
    headers = {
        "Host": "p.xpfarm.cn",
        "Connection": "keep-alive",
        "Content-Length": "13",
        "authorization": token,
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "contenttype": "[object Undefined]",
        "Referer": "https://servicewechat.com/wx27e219ff3142b7c8/59/page-frame.html"
    }
    data = {"task_id": 1}
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    message = response_data['message']
    print(f"广告水滴领取结果→{message}")
    time.sleep(random.randint(30, 40))
def Advertisementfertilizer(token):  # 广告肥料
    url = "https://p.xpfarm.cn/treemp/tree.Tasks/completeTask"
    headers = {
        "Host": "p.xpfarm.cn",
        "Connection": "keep-alive",
        "Content-Length": "13",
        "authorization": token,
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "contenttype": "[object Undefined]",
        "Referer": "https://servicewechat.com/wx27e219ff3142b7c8/59/page-frame.html"
    }
    data = {"task_id": 2}
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    message = response_data['message']
    print(f"广告肥料观看结果→{message}")
    time.sleep(random.randint(30, 40))
def Advertisementfertilizercollection(token):  # 广告肥料领取
    url = "https://p.xpfarm.cn/treemp/tree.Tasks/receiveTaskReward"
    headers = {
        "Host": "p.xpfarm.cn",
        "Connection": "keep-alive",
        "Content-Length": "13",
        "authorization": token,
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "contenttype": "[object Undefined]",
        "Referer": "https://servicewechat.com/wx27e219ff3142b7c8/59/page-frame.html"
    }
    data = {"task_id": 2}
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    message = response_data['message']
    print(f"广告肥料领取结果→{message}")
    time.sleep(random.randint(30, 40))
def ShareWaterDrops(token):  # 分享水滴
    url = "https://p.xpfarm.cn/treemp/tree.Tasks/completeTask"
    headers = {
        "Host": "p.xpfarm.cn",
        "Connection": "keep-alive",
        "Content-Length": "13",
        "authorization": token,
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "contenttype": "[object Undefined]",
        "Referer": "https://servicewechat.com/wx27e219ff3142b7c8/59/page-frame.html"
    }
    data = {"task_id": 5}
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    message = response_data['message']
    print(f"分享水滴结果→{message}")
    time.sleep(random.randint(30, 40))
def Sharewaterdropstoget(token):  # 分享水滴领取
    url = "https://p.xpfarm.cn/treemp/tree.Tasks/receiveTaskReward"
    headers = {
        "Host": "p.xpfarm.cn",
        "Connection": "keep-alive",
        "Content-Length": "13",
        "authorization": token,
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "contenttype": "[object Undefined]",
        "Referer": "https://servicewechat.com/wx27e219ff3142b7c8/59/page-frame.html"
    }
    data = {"task_id": 5}
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    message = response_data['message']
    print(f"分享水滴领取结果→{message}")
    time.sleep(random.randint(30, 40))
def Sharethefertilizer(token):  # 分享肥料
    url = "https://p.xpfarm.cn/treemp/tree.Tasks/completeTask"
    headers = {
        "Host": "p.xpfarm.cn",
        "Connection": "keep-alive",
        "Content-Length": "13",
        "authorization": token,
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "contenttype": "[object Undefined]",
        "Referer": "https://servicewechat.com/wx27e219ff3142b7c8/59/page-frame.html"
    }
    data = {"task_id": 13}
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    message = response_data['message']
    print(f"分享肥料结果→{message}")
    time.sleep(random.randint(30, 40))
def Sharefertilizercollection(token):  # 分享肥料领取
    url = "https://p.xpfarm.cn/treemp/tree.Tasks/receiveTaskReward"
    headers = {
        "Host": "p.xpfarm.cn",
        "Connection": "keep-alive",
        "Content-Length": "13",
        "authorization": token,
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "contenttype": "[object Undefined]",
        "Referer": "https://servicewechat.com/wx27e219ff3142b7c8/59/page-frame.html"
    }
    data = {"task_id": 13}
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    message = response_data['message']
    print(f"分享肥料领取结果→{message}")
    time.sleep(random.randint(30, 40))
def addWater(token):
    url = "https://p.xpfarm.cn/treemp/tree.Tasks/addWater"
    headers = {
        "Host": "p.xpfarm.cn",
        "Connection": "keep-alive",
        "Content-Length": "2",
        "authorization": token,
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip, compress, br, deflate",
        "contenttype": "[object Undefined]",
        "Referer": "https://servicewechat.com/wx27e219ff3142b7c8/59/page-frame.html"
    }
    data = {}
    for i in range(7):
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        message = response_data['message']
        print(f"浇水结果→{message}")
        delay = random.randint(30, 40)
        time.sleep(delay)
def Fertilization(token):
    url = "https://p.xpfarm.cn/treemp/tree.Tasks/addFertilizer"
    headers = {
        "Host": "p.xpfarm.cn",
        "Connection": "keep-alive",
        "Content-Length": "2",
        "authorization": token,
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/2307 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip, compress, br, deflate",
        "contenttype": "[object Undefined]",
        "Referer": "https://servicewechat.com/wx27e219ff3142b7c8/59/page-frame.html"
    }
    data = {"type":0}
    for i in range(2):
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        message = response_data['message']
        print(f"施肥结果→{message}")
        delay = random.randint(30, 40)
        time.sleep(delay)
def execute_tasks(token):
    Advertisingwilldrop(token)
    Advertisementwaterdropcollection(token)
    Advertisementfertilizer(token)
    Advertisementfertilizercollection(token)
    ShareWaterDrops(token)
    Sharewaterdropstoget(token)
    Sharethefertilizer(token)
    Sharefertilizercollection(token)
    addWater(token)
    Fertilization(token)
if __name__ == "__main__":
    token = os.environ.get('xpnc')
    if not token:
        print("请设置xpnc环境变量在运行")
    else:
        token_list = token.split('@')
        num = len(token_list)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for num, token in enumerate(token_list, start=1):
                print(f"=====👑MK兴攀农场小程序👑=====")
                print(f"=====开始执行第{num}个用户的任务=====")
                print("=====开始执行获取水滴和肥料等任务=====")
        
                executor.submit(execute_tasks, token)
