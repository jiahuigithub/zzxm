/**
 * cron "0 9,19 * * *" YueCheng.js
 * export YueCheng="账号1&密码1&支付宝姓名1&支付宝账号1 账号2&密码2&支付宝姓名2&支付宝账号2"
 * export OCR_SERVER="ocr服务"
 */
const $ = new Env('今日越城')
const YueCheng = ($.isNode() ? process.env.YueCheng : $.getdata("YueCheng")) || '';
const OCR_SERVER = ($.isNode() ? process.env.OCR_SERVER : $.getdata("OCR_SERVER")) || 'https://ddddocr.xzxxn7.live';
window = {};
let Utils = undefined;
let signature_key = ''
let notice = ''
let sessionId = ''
let tenantId = '31'
let accountId = ''
let clientId = '48'
let signatureSalt = "FR*r!isE5W"
let phone_number = ''
let password = ''
let realname = ''
let aliPay = ''
let ua = ''
let commonUa = ''
let deviceId = ''
let jinhuaAppId = 'K8tbWP2J0x3uCITGYEhL'
let jinhuaKey = '35c782a2'
let jinhuaToken = ''
let activityCookie = ''
let activityId = ''
let consumerId = ''
!(async () => {
    await main();
})().catch((e) => {$.log(e)}).finally(() => {$.done({});});

async function main() {
    console.log('作者：@xzxxn777\n频道：https://t.me/xzxxn777\n群组：https://t.me/xzxxn7777\n自用机场推荐：https://xn--diqv0fut7b.com\n')
    if (!YueCheng) {
        console.log("先去boxjs填写账号密码")
        await sendMsg('先去boxjs填写账号密码');
        return
    }
    Utils = await loadUtils();
    let arr = YueCheng.split(" ");
    for (const item of arr) {
        console.log("随机生成UA")
        let randomUA = generateRandomUA();
        ua = randomUA.ua;
        commonUa = randomUA.commonUa;
        deviceId = randomUA.uuid;
        console.log(ua)
        console.log(commonUa)
        phone_number = item.split("&")[0]
        password = item.split("&")[1]
        realname = item.split("&")[2]
        aliPay = item.split("&")[3] || phone_number
        console.log(`用户：${phone_number}开始任务`)
        console.log("获取sessionId")
        let initSession = await commonPost('/api/account/init');
        sessionId = initSession.data.session.id;
        console.log(sessionId)
        console.log("获取signature_key")
        let init = await initGet(`/web/init?client_id=${clientId}`)
        signature_key = init.data.client.signature_key;
        console.log(signature_key)
        console.log("获取code")
        let credential_auth = await passportPost('/web/oauth/credential_auth')
        if (!credential_auth.data) {
            console.log(credential_auth.message)
            continue
        }
        let code = credential_auth.data.authorization_code.code;
        console.log(code)
        console.log("登录")
        let login = await commonPost('/api/zbtxz/login',`check_token=&code=${code}&token=&type=-1&union_id=`)
        console.log('登录成功')
        accountId = login.data.session.account_id;
        sessionId = login.data.session.id;
        console.log("————————————")
        console.log('阅读抽奖')
        console.log("获取id")
        let articleList = await commonGet('/api/minus1floor/config')
        let url = articleList.data.article_list[2].column_news_list[2].url;
        let urlStr = url.split('?')[1];
        let result = {};
        let paramsArr = urlStr.split('&')
        for(let i = 0,len = paramsArr.length;i < len;i++){
            let arr = paramsArr[i].split('=')
            result[arr[0]] = arr[1];
        }
        let id = result.id;
        console.log(id)
        console.log("获取key和token")
        let jinhuaLogin = await jinhuaPost('/api/member/login',{"debug":0,"userId":""})
        jinhuaKey = jinhuaLogin.data.key;
        jinhuaToken = "Bearer " + jinhuaLogin.data.token;
        console.log(jinhuaKey)
        console.log(jinhuaToken)
        console.log("获取抽奖id")
        let jinhuaDetail = await jinhuaGet(`/api/study/detail?id=${id}`,{"id":id})
        let lotteryId = jinhuaDetail.data.lottery.lottery_id;
        console.log(lotteryId)
        console.log("开始阅读")
        for (const item of jinhuaDetail.data.levels) {
            let level = await jinhuaGet(`/api/study/level?id=${item.id}`,{"id":item.id})
            console.log(level.data.level.name)
            if (level.data.level.task_num == level.data.completedTasks.length) {
                console.log(`已完成`)
                continue
            }
            for (const task of level.data.tasks) {
                let detail = await commonGet(`/api/article/detail?id=${task.content_id}`)
                console.log(`文章：${detail.data.article.list_title}`)
                let read = await commonGet(`/api/article/read_time?channel_article_id=${task.content_id}&read_time=5938`)
                console.log(`阅读：${read.message}`)
                let complete = await jinhuaPost(`/api/study/task/complete`,{"id":task.id})
                console.log(`完成任务：${complete.message}`)
            }
        }
        let lotteryCount = await jinhuaPost(`/api/lotterybigwheel/_ac_lottery_count`,{"id":lotteryId,"module":"study"})
        console.log(`拥有${lotteryCount.data.count}次抽奖`)
        for (let i = 0; i < lotteryCount.data.count; i++) {
            let lottery = await jinhuaPost(`/api/lotterybigwheel/_ac_lottery`,{"id":lotteryId,"app_id":jinhuaAppId,"module":"study","optionHash":""})
            if (lottery.code == 10000) {
                console.log(lottery.message)
                let captcha =  await jinhuaPost(`/api/captcha/get`,{"activity_id":lotteryId,"module":"bigWheel"})
                let jigsawImageUrl = captcha.data.jigsawImageUrl;
                let originalImageUrl = captcha.data.originalImageUrl;
                console.log(`滑块：${jigsawImageUrl}`)
                console.log(`背景：${originalImageUrl}`)
                let captchaToken = captcha.data.token;
                let secretKey = captcha.data.secretKey;
                console.log(`秘钥：${secretKey}`)
                let getXpos = await slidePost({'slidingImage': jigsawImageUrl, 'backImage': originalImageUrl})
                if (!getXpos) {
                    console.log("ddddocr服务异常")
                    await sendMsg('ddddocr服务异常');
                    continue;
                }
                console.log(getXpos)
                let point = aesEncrypt(JSON.stringify({x: getXpos.result, y: 5}), secretKey)
                let check = await jinhuaPost(`/api/captcha/check`,{"activity_id":lotteryId,"module":"bigWheel","cap_token":captchaToken,"point":point})
                console.log("验证滑块：" + check.message)
                if (check.message == '操作成功') {
                    lottery = await jinhuaPost(`/api/lotterybigwheel/_ac_lottery`,{"id":lotteryId,"app_id":jinhuaAppId,"module":"study","optionHash":""})
                    if (lottery.data.code) {
                        console.log(`抽奖获得：${lottery.data.title}`)
                        notice += `用户：${phone_number} 抽奖获得：${lottery.data.title}\n`
                    } else {
                        console.log(`抽奖获得：${lottery.data.tip_title}`)
                        notice += `用户：${phone_number} 抽奖获得：${lottery.data.tip_title}\n`
                    }
                }
            } else {
                if (lottery.data.code) {
                    console.log(`抽奖获得：${lottery.data.title}`)
                    notice += `用户：${phone_number} 抽奖获得：${lottery.data.title}\n`
                } else {
                    console.log(`抽奖获得：${lottery.data.tip_title}`)
                    notice += `用户：${phone_number} 抽奖获得：${lottery.data.tip_title}\n`
                }
            }
        }
        console.log("————————————")
        console.log('动动手指赢红包')
        url = articleList.data.article_list[2].column_news_list[1].url;
        urlStr = url.split('?')[1];
        result = {};
        paramsArr = urlStr.split('&')
        for(let i = 0,len = paramsArr.length;i < len;i++){
            let arr = paramsArr[i].split('=')
            result[arr[0]] = arr[1];
        }
        let getDetail = await commonGet(`/api/article/detail?id=${result.id}`)
        let newsList = await commonGet(`/api/article/subject_group_list?group_id=${getDetail.data.article.subject_groups[0].group_id}`)
        for (const news of newsList.data.article_list) {
            if (!isToday(news.published_at)) {
                break
            }
            console.log(`文章：${news.list_title}`)
            let detail = await commonGet(`/api/article/detail?id=${news.id}`)
            let content = detail.data.article.content;
            const match = content.match(/id%3D(\d+)%26dbnewopen/);
            if (match) {
                activityId = match[1];
                console.log(`activityId：${activityId}`)
            } else {
                console.log("未匹配到activityId");
                continue
            }
            console.log("阅读登录")
            let activityLogin = await activityGet(`/customActivity/zjtm/autoLogin?_=${Date.now()}&sessionId=${sessionId}&accountId=${accountId}&redirectUrl=https://95337.activity-42.m.duiba.com.cn/hdtool/index?id=${activityId}&dbnewopen`)
            let location = activityLogin.data;
            activityCookie = ''
            activityCookie = await activityCookieGet(location);
            console.log("获取抽奖key")
            let key = await keyGet(`https://95337.activity-42.m.duiba.com.cn/hdtool/index?id=${activityId}&dbnewopen&from=login&spm=95337.1.1.1`)
            let getTokenNew = await activityPost(`/hdtool/ctoken/getTokenNew`,`timestamp=${Date.now()}&activityId=${activityId}&activityType=hdtool&consumerId=${consumerId}`)
            eval(getTokenNew.token);
            let token = window[key];
            let lottery = await activityPost(`/hdtool/dy/doJoin?dpm=95337.3.1.0&activityId=${activityId}&_=${Date.now()}`,`actId=${activityId}&oaId=${activityId}&activityType=hdtool&consumerId=${consumerId}&token=${token}`)
            if (lottery.success) {
                if (!lottery.orderId) {
                    console.log(lottery.message)
                    continue
                }
                let orderId = lottery.orderId;
                let result = 0;
                while (result == 0) {
                    let getOrderStatus = await activityPost(`/hdtool/getOrderStatus?_=${Date.now()}`,`orderId=${orderId}&adslotId=`)
                    result = getOrderStatus.result;
                    if (result == 0) {
                        console.log(getOrderStatus.message)
                    } else {
                        if (getOrderStatus.lottery.type == 'thanks') {
                            console.log(`谢谢参与`)
                        }
                        if (getOrderStatus.lottery.type == 'alipay') {
                            console.log(`抽奖获得支付宝红包：${getOrderStatus.lottery.title}`)
                            notice += `用户：${phone_number} 抽奖获得支付宝红包：${getOrderStatus.lottery.title}\n`
                            let url = getOrderStatus.lottery.link;
                            let urlStr = url.split('?')[1];
                            let result = {};
                            let paramsArr = urlStr.split('&')
                            for(let i = 0,len = paramsArr.length;i < len;i++){
                                let arr = paramsArr[i].split('=')
                                result[arr[0]] = arr[1];
                            }
                            let recordId = result.recordId;
                            if (realname && aliPay) {
                                console.log("获取兑换key")
                                key = await keyGet(`https://95337.activity-42.m.duiba.com.cn/activity/takePrizeNew?recordId=${recordId}&dbnewopen`)
                                let getToken = await activityPost(`/ctoken/getToken.do`)
                                eval(getToken.token);
                                let token = window[key];
                                let award = await activityPost(`/activity/doTakePrize`,`alipay=${aliPay}&realname=${encodeURI(realname)}&recordId=${recordId}&token=${token}`)
                                console.log(award.message)
                            } else {
                                console.log(`请设置支付宝姓名和账号`)
                            }
                        }
                    }
                }
            } else {
                console.log(lottery.message)
            }
            await $.wait(2000)
        }
        // console.log("————————————")
        // console.log("开始任务")
        // let readFinish = true;
        // let likeFinish = true;
        // let shareFinish = true;
        // let taskList = await commonGet('/api/user_center/task?type=1&current=1&size=20')
        // for (let task of taskList.data.list) {
        //     console.log(`任务：${task.name}`)
        //     if (task.completed == 1) {
        //         console.log(`任务已完成`)
        //         continue;
        //     }
        //     console.log(`任务进度：${task.finish_times}/${task.frequency}`)
        //     if (task.name == '新闻资讯阅读') {
        //         readFinish = false;
        //     }
        //     if (task.name == '新闻资讯点赞') {
        //         likeFinish = false;
        //     }
        //     if (task.name == '分享资讯给好友') {
        //         shareFinish = false;
        //     }
        // }
        // if (!readFinish || !likeFinish || !shareFinish) {
        //     let articleList = await commonGet('/api/article/channel_list?channel_id=5dbf7fdfb1985007455762fd&isDiFangHao=false&is_new=true&list_count=0&size=20')
        //     for (const article of articleList.data.article_list) {
        //         let articleId = article.id;
        //         if (!readFinish) {
        //             let read = await commonGet(`/api/article/read_time?channel_article_id=${articleId}&is_end=true&read_time=3051`)
        //             if (read.data.score_notify) {
        //                 console.log(`阅读获得：${read.data?.score_notify?.integral}积分`)
        //             } else {
        //                 console.log(`文章已经阅读过了`)
        //             }
        //         }
        //         if (!likeFinish) {
        //             let like = await commonPost(`/api/favorite/like`,`action=true&id=${articleId}`)
        //             if (like.data) {
        //                 console.log(`点赞获得：${like.data?.score_notify?.integral}积分`)
        //             } else {
        //                 console.log(`文章已经点赞过了`)
        //             }
        //         }
        //         if (!shareFinish) {
        //             let share = await commonPost(`/api/user_mumber/doTask`,`memberType=3&member_type=3&target_id==${articleId}`)
        //             if (share.data.score_notify) {
        //                 console.log(`分享获得：${share.data?.score_notify?.integral}积分`)
        //             } else {
        //                 console.log(`文章已经分享过了`)
        //             }
        //         }
        //     }
        // }
        // console.log("————————————")
        // console.log("查询积分")
        // let detail = await commonGet('/api/user_mumber/account_detail')
        // console.log(`拥有积分：${detail.data.rst.total_integral}\n`)
        // notice += `用户：${phone_number} 积分：${detail.data.rst.total_integral}\n`
    }
    if (notice) {
        await sendMsg(notice);
    }
}

async function initGet(url) {
    return new Promise(resolve => {
        const options = {
            url: `https://passport.tmuyun.com${url}`,
            headers : {
                'Connection': 'Keep-Alive',
                'Cache-Control': 'no-cache',
                'X-REQUEST-ID': generateUUID(),
                'Accept-Encoding': 'gzip',
                'user-agent': ua,
            }
        }
        $.get(options, async (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    resolve(JSON.parse(data));
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

async function passportPost(url) {
    let params = getBody();
    return new Promise(resolve => {
        const options = {
            url: `https://passport.tmuyun.com${url}`,
            headers : {
                'Connection': 'Keep-Alive',
                'X-REQUEST-ID': params.uuid,
                'X-SIGNATURE': params.signature,
                'Cache-Control': 'no-cache',
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'Accept-Encoding': 'gzip',
                'user-agent': ua,
            },
            body: params.body
        }
        $.post(options, async (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    resolve(JSON.parse(data));
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

async function commonGet(url) {
    let params = getParams(url);
    return new Promise(resolve => {
        const options = {
            url: `https://vapp.tmuyun.com${url}`,
            headers : {
                'Connection': 'Keep-Alive',
                'X-TIMESTAMP': params.time,
                'X-SESSION-ID': sessionId,
                'X-REQUEST-ID': params.uuid,
                'X-SIGNATURE': params.signature,
                'X-TENANT-ID': tenantId,
                'X-ACCOUNT-ID': accountId,
                'Cache-Control': 'no-cache',
                'Accept-Encoding': 'gzip',
                'user-agent': commonUa,
            }
        }
        $.get(options, async (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    await $.wait(2000)
                    resolve(JSON.parse(data));
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

async function commonPost(url,body) {
    let params = getParams(url);
    return new Promise(resolve => {
        const options = {
            url: `https://vapp.tmuyun.com${url}`,
            headers : {
                'Connection': 'Keep-Alive',
                'X-TIMESTAMP': params.time,
                'X-SESSION-ID': sessionId,
                'X-REQUEST-ID': params.uuid,
                'X-SIGNATURE': params.signature,
                'X-TENANT-ID': tenantId,
                'X-ACCOUNT-ID': accountId,
                'Cache-Control': 'no-cache',
                'Accept-Encoding': 'gzip',
                'user-agent': commonUa,
            },
            body: body
        }
        $.post(options, async (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    await $.wait(2000)
                    resolve(JSON.parse(data));
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

async function jinhuaPost(url,body) {
    let params = getJinhuaParams(body);
    return new Promise(resolve => {
        const options = {
            url: `https://op-api.cloud.jinhua.com.cn${url}`,
            headers : {
                'access-type': 'app',
                'access-module': 'study',
                'access-device-id': deviceId,
                'access-auth-id': accountId,
                'access-api-signature': params.signature,
                'access-nonce-str': params.uuid,
                'authorization': jinhuaToken,
                'access-app-id': jinhuaAppId,
                'access-timestamp': params.time,
                'access-api-token': sessionId,
                'accept': 'application/json, text/plain, */*',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; 21091116AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36;xsb_yuecheng;xsb_yuecheng;1.7.0;native_app;6.12.0',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://op-h5.cloud.jinhua.com.cn',
                'x-requested-with': 'com.zjonline.zhuji',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://op-h5.cloud.jinhua.com.cn/',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            },
            body: JSON.stringify(body)
        }
        $.post(options, async (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    await $.wait(2000)
                    resolve(JSON.parse(data));
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

async function jinhuaGet(url,body) {
    let params = getJinhuaParams(body);
    return new Promise(resolve => {
        const options = {
            url: `https://op-api.cloud.jinhua.com.cn${url}`,
            headers : {
                'access-type': 'app',
                'access-module': 'study',
                'access-device-id': deviceId,
                'access-auth-id': accountId,
                'access-api-signature': params.signature,
                'access-nonce-str': params.uuid,
                'authorization': jinhuaToken,
                'access-app-id': jinhuaAppId,
                'access-timestamp': params.time,
                'access-api-token': sessionId,
                'accept': 'application/json, text/plain, */*',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; 21091116AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36;xsb_yuecheng;xsb_yuecheng;1.7.0;native_app;6.12.0',
                'origin': 'https://op-h5.cloud.jinhua.com.cn',
                'x-requested-with': 'com.zjonline.zhuji',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://op-h5.cloud.jinhua.com.cn/',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            }
        }
        $.get(options, async (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    await $.wait(2000)
                    resolve(JSON.parse(data));
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

async function activityGet(url) {
    return new Promise(resolve => {
        const options = {
            url: `https://95337.activity-42.m.duiba.com.cn${url}`,
            headers : {
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; 21091116AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36;xsb_yuecheng;xsb_yuecheng;1.7.0;native_app;6.12.0',
                'x-requested-with': 'com.zjonline.yuecheng',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            }
        }
        $.get(options, async (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    await $.wait(2000)
                    resolve(JSON.parse(data));
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

async function activityPost(url,body) {
    return new Promise(resolve => {
        const options = {
            url: `https://95337.activity-42.m.duiba.com.cn${url}`,
            headers : {
                'accept': 'application/json',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; 21091116AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36;xsb_yuecheng;xsb_yuecheng;1.7.0;native_app;6.12.0',
                'x-requested-with': 'XMLHttpRequest',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://95337.activity-42.m.duiba.com.cn',
                'cookie': activityCookie,
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': `https://95337.activity-42.m.duiba.com.cn/hdtool/index?id=${activityId}&dbnewopen&from=login&spm=95337.1.1.1`,
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            },
            body: body
        }
        $.post(options, async (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    await $.wait(2000)
                    resolve(JSON.parse(data));
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

async function activityCookieGet(url) {
    return new Promise(resolve => {
        const options = {
            url: `https:${url}`,
            headers : {
                'accept': '*/*',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; 21091116AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36;xsb_yuecheng;xsb_yuecheng;1.7.0;native_app;6.12.0',
                'x-requested-with': 'com.zjonline.yuecheng',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            },
            followRedirect: false
        }
        $.get(options, async (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    await $.wait(2000)
                    if ($.isNode()) {
                        let cookieArr = resp.headers['set-cookie'] || resp.headers['Set-Cookie'];
                        for (let i = 0; i < cookieArr.length; i++) {
                            activityCookie += cookieArr[i].split(';')[0] + ';'
                        }
                    } else {
                        activityCookie = resp.headers['set-cookie'] || resp.headers['Set-Cookie'];
                        activityCookie = formatCookies(activityCookie);
                    }
                    resolve(activityCookie);
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

async function keyGet(url) {
    return new Promise(resolve => {
        const options = {
            url: url,
            headers: {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; 21091116AC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36;xsb_yuecheng;xsb_yuecheng;1.7.0;native_app;6.12.0',
                'x-requested-with': 'com.zjonline.yuecheng',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://95337.activity-42.m.duiba.com.cn/',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'cookie': activityCookie
            }
        }
        $.get(options, async (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    await $.wait(2000)
                    let code = /<script type\b[^>]*>\s*var([\s\S]*?)<\/script>/.exec(data)[1];
                    eval(code)
                    let key = /var\s+key\s+=\s+'([^']+)';/.exec(getDuibaToken.toString())[1];
                    console.log(key)
                    console.log('获取consumerId')
                    const regex = /consumerId:'(\d+)'/;
                    const match = data.match(regex);
                    if (match) {
                        consumerId = match[1];
                    } else {
                        consumerId = '4135312778'
                    }
                    console.log(consumerId)
                    resolve(key);
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

async function slidePost(body) {
    return new Promise(resolve => {
        const options = {
            url: `${OCR_SERVER}/capcode`,
            headers: {
                'Content-Type': 'application/json',
            },
            body:JSON.stringify(body)
        }
        $.post(options, (err, resp, data) => {
            try {
                if (err) {
                    console.log(`${JSON.stringify(err)}`)
                    console.log(`${$.name} API请求失败，请检查网路重试`)
                } else {
                    resolve(JSON.parse(data));
                }
            } catch (e) {
                $.logErr(e, resp)
            } finally {
                resolve();
            }
        })
    })
}

function formatCookies(cookieString) {
    const cookies = cookieString.split(', ');
    const formattedCookies = cookies.map(cookie => {
        const keyValue = cookie.split(';')[0];
        return keyValue.trim();
    });
    return formattedCookies.join(';');
}

function aesEncrypt(e, r) {
    CryptoJS = Utils.createCryptoJS();
    var n = CryptoJS.enc.Utf8.parse(r)
        , o = CryptoJS.enc.Utf8.parse(e)
        , s = CryptoJS.AES.encrypt(o, n, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return s.toString()
}

function getBody() {
    const key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD6XO7e9YeAOs+cFqwa7ETJ+WXizPqQeXv68i5vqw9pFREsrqiBTRcg7wB0RIp3rJkDpaeVJLsZqYm5TW7FWx/iOiXFc+zCPvaKZric2dXCw27EvlH5rq+zwIPDAJHGAfnn1nmQH7wR3PCatEIb8pz5GFlTHMlluw4ZYmnOwg+thwIDAQAB';
    const encryptor = new (Utils.loadJSEncrypt());
    encryptor.setPublicKey(key);
    password = encryptor.encrypt(password);
    let uuid = generateUUID();
    let body = `client_id=${clientId}&password=${password}&phone_number=${phone_number}`;
    const str = `post%%/web/oauth/credential_auth?${body}%%${uuid}%%`;
    body = `client_id=${clientId}&password=${encodeURIComponent(password)}&phone_number=${phone_number}`;
    CryptoJS = Utils.createCryptoJS();
    const hash = CryptoJS.HmacSHA256(str, signature_key);
    let signature = CryptoJS.enc.Hex.stringify(hash);
    return {"uuid":uuid,"signature":signature,"body":body};
}

function getJinhuaParams(params) {
    let uuid = generateUUID();
    let time = Date.now();
    let config = {
        app_id: jinhuaAppId,
        device_id: deviceId,
        nonce_str: uuid,
        source_type: 'app',
        timestamp: time,
        auth_id: accountId,
        token: sessionId
    };
    Object.entries(params).forEach(([key, value]) => {
        config[key] = value;
    });
    let sortedKeys = Object.keys(config).sort();
    let result = sortedKeys.map(key => `${key}=${config[key]}`).join('&&');
    result = result + '&&' + jinhuaKey;
    CryptoJS = Utils.createCryptoJS();
    let signature = CryptoJS.SHA256(result).toString();
    return {"uuid":uuid,"time":time,"signature":signature};
}

function getParams(url) {
    let uuid = generateUUID();
    let time = Date.now();
    if (url.indexOf('?') > 0) {
        url = url.substring(0, url.indexOf('?'));
    }
    CryptoJS = Utils.createCryptoJS();
    let signature = CryptoJS.SHA256(`${url}&&${sessionId}&&${uuid}&&${time}&&${signatureSalt}&&${tenantId}`).toString();
    return {"uuid":uuid,"time":time,"signature":signature};
}

function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        const r = (Math.random() * 16) | 0;
        const v = c === 'x' ? r : (r & 0x3) | 0x8;
        return v.toString(16);
    });
}

function getRandomElement(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

function generateRandomUA() {
    const version = "1.7.0";
    const uuid = generateUUID();
    const deviceIds = [
        "M1903F2A",
        "M2001J2E",
        "M2001J2C",
        "M2001J1E",
        "M2001J1C",
        "M2002J9E",
        "M2011K2C",
        "M2102K1C",
        "M2101K9C",
        "2107119DC",
        "2201123C",
        "2112123AC",
        "2201122C",
        "2211133C",
        "2210132C",
        "2304FPN6DC",
        "23127PN0CC",
        "24031PN0DC",
        "23090RA98C",
        "2312DRA50C",
        "2312CRAD3C",
        "2312DRAABC",
        "22101316UCP",
        "22101316C"
    ];
    const deviceId = getRandomElement(deviceIds);
    const device = "Xiaomi " + deviceId;
    const os = "Android";
    const osVersion = "11";
    const osType = "Release";
    const appVersion = "6.12.0";

    let ua = `${os.toUpperCase()};${osVersion};${clientId};${version};1.0;null;${deviceId}`
    let commonUa = `${version};${uuid};${device};${os};${osVersion};${osType};${appVersion}`
    return {"ua": ua, "commonUa": commonUa,"uuid":uuid};
}

function isToday(dateString) {
    const inputDate = new Date(dateString);
    const today = new Date();

    return inputDate.getFullYear() === today.getFullYear() &&
        inputDate.getMonth() === today.getMonth() &&
        inputDate.getDate() === today.getDate();
}

async function loadUtils() {
    let code = $.getdata('Utils_Code') || '';
    if (code && Object.keys(code).length) {
        console.log(`✅ ${$.name}: 缓存中存在Utils代码, 跳过下载`)
        eval(code)
        return creatUtils();
    }
    console.log(`🚀 ${$.name}: 开始下载Utils代码`)
    return new Promise(async (resolve) => {
        $.getScript(
            'https://mirror.ghproxy.com/https://raw.githubusercontent.com/xzxxn777/Surge/main/Utils/Utils.js'
        ).then((fn) => {
            $.setdata(fn, "Utils_Code")
            eval(fn)
            console.log(`✅ Utils加载成功, 请继续`)
            resolve(creatUtils())
        })
    })
}

async function sendMsg(message) {
    if ($.isNode()) {
        let notify = ''
        try {
            notify = require('./sendNotify');
        } catch (e) {
            notify = require("../sendNotify");
        }
        await notify.sendNotify($.name, message);
    } else {
        $.msg($.name, '', message)
    }
}

// prettier-ignore
function Env(t,e){class s{constructor(t){this.env=t}send(t,e="GET"){t="string"==typeof t?{url:t}:t;let s=this.get;return"POST"===e&&(s=this.post),new Promise(((e,i)=>{s.call(this,t,((t,s,o)=>{t?i(t):e(s)}))}))}get(t){return this.send.call(this.env,t)}post(t){return this.send.call(this.env,t,"POST")}}return new class{constructor(t,e){this.logLevels={debug:0,info:1,warn:2,error:3},this.logLevelPrefixs={debug:"[DEBUG] ",info:"[INFO] ",warn:"[WARN] ",error:"[ERROR] "},this.logLevel="info",this.name=t,this.http=new s(this),this.data=null,this.dataFile="box.dat",this.logs=[],this.isMute=!1,this.isNeedRewrite=!1,this.logSeparator="\n",this.encoding="utf-8",this.startTime=(new Date).getTime(),Object.assign(this,e),this.log("",`🔔${this.name}, 开始!`)}getEnv(){return"undefined"!=typeof $environment&&$environment["surge-version"]?"Surge":"undefined"!=typeof $environment&&$environment["stash-version"]?"Stash":"undefined"!=typeof module&&module.exports?"Node.js":"undefined"!=typeof $task?"Quantumult X":"undefined"!=typeof $loon?"Loon":"undefined"!=typeof $rocket?"Shadowrocket":void 0}isNode(){return"Node.js"===this.getEnv()}isQuanX(){return"Quantumult X"===this.getEnv()}isSurge(){return"Surge"===this.getEnv()}isLoon(){return"Loon"===this.getEnv()}isShadowrocket(){return"Shadowrocket"===this.getEnv()}isStash(){return"Stash"===this.getEnv()}toObj(t,e=null){try{return JSON.parse(t)}catch{return e}}toStr(t,e=null,...s){try{return JSON.stringify(t,...s)}catch{return e}}getjson(t,e){let s=e;if(this.getdata(t))try{s=JSON.parse(this.getdata(t))}catch{}return s}setjson(t,e){try{return this.setdata(JSON.stringify(t),e)}catch{return!1}}getScript(t){return new Promise((e=>{this.get({url:t},((t,s,i)=>e(i)))}))}runScript(t,e){return new Promise((s=>{let i=this.getdata("@chavy_boxjs_userCfgs.httpapi");i=i?i.replace(/\n/g,"").trim():i;let o=this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout");o=o?1*o:20,o=e&&e.timeout?e.timeout:o;const[r,a]=i.split("@"),n={url:`http://${a}/v1/scripting/evaluate`,body:{script_text:t,mock_type:"cron",timeout:o},headers:{"X-Key":r,Accept:"*/*"},timeout:o};this.post(n,((t,e,i)=>s(i)))})).catch((t=>this.logErr(t)))}loaddata(){if(!this.isNode())return{};{this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e);if(!s&&!i)return{};{const i=s?t:e;try{return JSON.parse(this.fs.readFileSync(i))}catch(t){return{}}}}}writedata(){if(this.isNode()){this.fs=this.fs?this.fs:require("fs"),this.path=this.path?this.path:require("path");const t=this.path.resolve(this.dataFile),e=this.path.resolve(process.cwd(),this.dataFile),s=this.fs.existsSync(t),i=!s&&this.fs.existsSync(e),o=JSON.stringify(this.data);s?this.fs.writeFileSync(t,o):i?this.fs.writeFileSync(e,o):this.fs.writeFileSync(t,o)}}lodash_get(t,e,s){const i=e.replace(/\[(\d+)\]/g,".$1").split(".");let o=t;for(const t of i)if(o=Object(o)[t],void 0===o)return s;return o}lodash_set(t,e,s){return Object(t)!==t||(Array.isArray(e)||(e=e.toString().match(/[^.[\]]+/g)||[]),e.slice(0,-1).reduce(((t,s,i)=>Object(t[s])===t[s]?t[s]:t[s]=Math.abs(e[i+1])>>0==+e[i+1]?[]:{}),t)[e[e.length-1]]=s),t}getdata(t){let e=this.getval(t);if(/^@/.test(t)){const[,s,i]=/^@(.*?)\.(.*?)$/.exec(t),o=s?this.getval(s):"";if(o)try{const t=JSON.parse(o);e=t?this.lodash_get(t,i,""):e}catch(t){e=""}}return e}setdata(t,e){let s=!1;if(/^@/.test(e)){const[,i,o]=/^@(.*?)\.(.*?)$/.exec(e),r=this.getval(i),a=i?"null"===r?null:r||"{}":"{}";try{const e=JSON.parse(a);this.lodash_set(e,o,t),s=this.setval(JSON.stringify(e),i)}catch(e){const r={};this.lodash_set(r,o,t),s=this.setval(JSON.stringify(r),i)}}else s=this.setval(t,e);return s}getval(t){switch(this.getEnv()){case"Surge":case"Loon":case"Stash":case"Shadowrocket":return $persistentStore.read(t);case"Quantumult X":return $prefs.valueForKey(t);case"Node.js":return this.data=this.loaddata(),this.data[t];default:return this.data&&this.data[t]||null}}setval(t,e){switch(this.getEnv()){case"Surge":case"Loon":case"Stash":case"Shadowrocket":return $persistentStore.write(t,e);case"Quantumult X":return $prefs.setValueForKey(t,e);case"Node.js":return this.data=this.loaddata(),this.data[e]=t,this.writedata(),!0;default:return this.data&&this.data[e]||null}}initGotEnv(t){this.got=this.got?this.got:require("got"),this.cktough=this.cktough?this.cktough:require("tough-cookie"),this.ckjar=this.ckjar?this.ckjar:new this.cktough.CookieJar,t&&(t.headers=t.headers?t.headers:{},t&&(t.headers=t.headers?t.headers:{},void 0===t.headers.cookie&&void 0===t.headers.Cookie&&void 0===t.cookieJar&&(t.cookieJar=this.ckjar)))}get(t,e=(()=>{})){switch(t.headers&&(delete t.headers["Content-Type"],delete t.headers["Content-Length"],delete t.headers["content-type"],delete t.headers["content-length"]),t.params&&(t.url+="?"+this.queryStr(t.params)),void 0===t.followRedirect||t.followRedirect||((this.isSurge()||this.isLoon())&&(t["auto-redirect"]=!1),this.isQuanX()&&(t.opts?t.opts.redirection=!1:t.opts={redirection:!1})),this.getEnv()){case"Surge":case"Loon":case"Stash":case"Shadowrocket":default:this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient.get(t,((t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status?s.status:s.statusCode,s.status=s.statusCode),e(t,s,i)}));break;case"Quantumult X":this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then((t=>{const{statusCode:s,statusCode:i,headers:o,body:r,bodyBytes:a}=t;e(null,{status:s,statusCode:i,headers:o,body:r,bodyBytes:a},r,a)}),(t=>e(t&&t.error||"UndefinedError")));break;case"Node.js":let s=require("iconv-lite");this.initGotEnv(t),this.got(t).on("redirect",((t,e)=>{try{if(t.headers["set-cookie"]){const s=t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString();s&&this.ckjar.setCookieSync(s,null),e.cookieJar=this.ckjar}}catch(t){this.logErr(t)}})).then((t=>{const{statusCode:i,statusCode:o,headers:r,rawBody:a}=t,n=s.decode(a,this.encoding);e(null,{status:i,statusCode:o,headers:r,rawBody:a,body:n},n)}),(t=>{const{message:i,response:o}=t;e(i,o,o&&s.decode(o.rawBody,this.encoding))}));break}}post(t,e=(()=>{})){const s=t.method?t.method.toLocaleLowerCase():"post";switch(t.body&&t.headers&&!t.headers["Content-Type"]&&!t.headers["content-type"]&&(t.headers["content-type"]="application/x-www-form-urlencoded"),t.headers&&(delete t.headers["Content-Length"],delete t.headers["content-length"]),void 0===t.followRedirect||t.followRedirect||((this.isSurge()||this.isLoon())&&(t["auto-redirect"]=!1),this.isQuanX()&&(t.opts?t.opts.redirection=!1:t.opts={redirection:!1})),this.getEnv()){case"Surge":case"Loon":case"Stash":case"Shadowrocket":default:this.isSurge()&&this.isNeedRewrite&&(t.headers=t.headers||{},Object.assign(t.headers,{"X-Surge-Skip-Scripting":!1})),$httpClient[s](t,((t,s,i)=>{!t&&s&&(s.body=i,s.statusCode=s.status?s.status:s.statusCode,s.status=s.statusCode),e(t,s,i)}));break;case"Quantumult X":t.method=s,this.isNeedRewrite&&(t.opts=t.opts||{},Object.assign(t.opts,{hints:!1})),$task.fetch(t).then((t=>{const{statusCode:s,statusCode:i,headers:o,body:r,bodyBytes:a}=t;e(null,{status:s,statusCode:i,headers:o,body:r,bodyBytes:a},r,a)}),(t=>e(t&&t.error||"UndefinedError")));break;case"Node.js":let i=require("iconv-lite");this.initGotEnv(t);const{url:o,...r}=t;this.got[s](o,r).then((t=>{const{statusCode:s,statusCode:o,headers:r,rawBody:a}=t,n=i.decode(a,this.encoding);e(null,{status:s,statusCode:o,headers:r,rawBody:a,body:n},n)}),(t=>{const{message:s,response:o}=t;e(s,o,o&&i.decode(o.rawBody,this.encoding))}));break}}time(t,e=null){const s=e?new Date(e):new Date;let i={"M+":s.getMonth()+1,"d+":s.getDate(),"H+":s.getHours(),"m+":s.getMinutes(),"s+":s.getSeconds(),"q+":Math.floor((s.getMonth()+3)/3),S:s.getMilliseconds()};/(y+)/.test(t)&&(t=t.replace(RegExp.$1,(s.getFullYear()+"").substr(4-RegExp.$1.length)));for(let e in i)new RegExp("("+e+")").test(t)&&(t=t.replace(RegExp.$1,1==RegExp.$1.length?i[e]:("00"+i[e]).substr((""+i[e]).length)));return t}queryStr(t){let e="";for(const s in t){let i=t[s];null!=i&&""!==i&&("object"==typeof i&&(i=JSON.stringify(i)),e+=`${s}=${i}&`)}return e=e.substring(0,e.length-1),e}msg(e=t,s="",i="",o={}){const r=t=>{const{$open:e,$copy:s,$media:i,$mediaMime:o}=t;switch(typeof t){case void 0:return t;case"string":switch(this.getEnv()){case"Surge":case"Stash":default:return{url:t};case"Loon":case"Shadowrocket":return t;case"Quantumult X":return{"open-url":t};case"Node.js":return}case"object":switch(this.getEnv()){case"Surge":case"Stash":case"Shadowrocket":default:{const r={};let a=t.openUrl||t.url||t["open-url"]||e;a&&Object.assign(r,{action:"open-url",url:a});let n=t["update-pasteboard"]||t.updatePasteboard||s;if(n&&Object.assign(r,{action:"clipboard",text:n}),i){let t,e,s;if(i.startsWith("http"))t=i;else if(i.startsWith("data:")){const[t]=i.split(";"),[,o]=i.split(",");e=o,s=t.replace("data:","")}else{e=i,s=(t=>{const e={JVBERi0:"application/pdf",R0lGODdh:"image/gif",R0lGODlh:"image/gif",iVBORw0KGgo:"image/png","/9j/":"image/jpg"};for(var s in e)if(0===t.indexOf(s))return e[s];return null})(i)}Object.assign(r,{"media-url":t,"media-base64":e,"media-base64-mime":o??s})}return Object.assign(r,{"auto-dismiss":t["auto-dismiss"],sound:t.sound}),r}case"Loon":{const s={};let o=t.openUrl||t.url||t["open-url"]||e;o&&Object.assign(s,{openUrl:o});let r=t.mediaUrl||t["media-url"];return i?.startsWith("http")&&(r=i),r&&Object.assign(s,{mediaUrl:r}),console.log(JSON.stringify(s)),s}case"Quantumult X":{const o={};let r=t["open-url"]||t.url||t.openUrl||e;r&&Object.assign(o,{"open-url":r});let a=t["media-url"]||t.mediaUrl;i?.startsWith("http")&&(a=i),a&&Object.assign(o,{"media-url":a});let n=t["update-pasteboard"]||t.updatePasteboard||s;return n&&Object.assign(o,{"update-pasteboard":n}),console.log(JSON.stringify(o)),o}case"Node.js":return}default:return}};if(!this.isMute)switch(this.getEnv()){case"Surge":case"Loon":case"Stash":case"Shadowrocket":default:$notification.post(e,s,i,r(o));break;case"Quantumult X":$notify(e,s,i,r(o));break;case"Node.js":break}if(!this.isMuteLog){let t=["","==============📣系统通知📣=============="];t.push(e),s&&t.push(s),i&&t.push(i),console.log(t.join("\n")),this.logs=this.logs.concat(t)}}debug(...t){this.logLevels[this.logLevel]<=this.logLevels.debug&&(t.length>0&&(this.logs=[...this.logs,...t]),console.log(`${this.logLevelPrefixs.debug}${t.map((t=>t??String(t))).join(this.logSeparator)}`))}info(...t){this.logLevels[this.logLevel]<=this.logLevels.info&&(t.length>0&&(this.logs=[...this.logs,...t]),console.log(`${this.logLevelPrefixs.info}${t.map((t=>t??String(t))).join(this.logSeparator)}`))}warn(...t){this.logLevels[this.logLevel]<=this.logLevels.warn&&(t.length>0&&(this.logs=[...this.logs,...t]),console.log(`${this.logLevelPrefixs.warn}${t.map((t=>t??String(t))).join(this.logSeparator)}`))}error(...t){this.logLevels[this.logLevel]<=this.logLevels.error&&(t.length>0&&(this.logs=[...this.logs,...t]),console.log(`${this.logLevelPrefixs.error}${t.map((t=>t??String(t))).join(this.logSeparator)}`))}log(...t){t.length>0&&(this.logs=[...this.logs,...t]),console.log(t.map((t=>t??String(t))).join(this.logSeparator))}logErr(t,e){switch(this.getEnv()){case"Surge":case"Loon":case"Stash":case"Shadowrocket":case"Quantumult X":default:this.log("",`❗️${this.name}, 错误!`,e,t);break;case"Node.js":this.log("",`❗️${this.name}, 错误!`,e,void 0!==t.message?t.message:t,t.stack);break}}wait(t){return new Promise((e=>setTimeout(e,t)))}done(t={}){const e=((new Date).getTime()-this.startTime)/1e3;switch(this.log("",`🔔${this.name}, 结束! 🕛 ${e} 秒`),this.log(),this.getEnv()){case"Surge":case"Loon":case"Stash":case"Shadowrocket":case"Quantumult X":default:$done(t);break;case"Node.js":process.exit(1)}}}(t,e)}
