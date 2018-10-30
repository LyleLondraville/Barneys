import requests, time, json

def c() :

    ## 2captcha key - 90183367e53b95cb465c6fba6f9b6cdf

    P = False

    sesh = requests.Session()

    postData={
             "key":'90183367e53b95cb465c6fba6f9b6cdf',
             "method":"userrecaptcha",
             "googlekey":'6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz',
             "proxy":'45.76.16.191:3128',
             "proxytype":"HTTP",
             "pageurl":'https://www.supremenewyork.com/checkout',
             "json":'1'
             }

    captchaPost = sesh.post('http://2captcha.com/in.php', data = postData)

    JSONdict = json.loads(captchaPost.text)

    if JSONdict['status'] == 1 :
        P = True

    else :
        while P == False :
            captchaPost = sesh.post('http://2captcha.com/in.php', data = postData)
            JSONdict = json.loads(captchaPost.text)

            if JSONdict['status'] == 1 :
                P = True
            else :
                pass

    getData={
           "key":'90183367e53b95cb465c6fba6f9b6cdf',
           "action":"get",
           "json":'1',
           "id":JSONdict['request'],
           }

    captchaGet=sesh.get("http://2captcha.com/res.php", params = getData)

    while 'CAPCHA_NOT_READY' in captchaGet.text :
        print 'Waiting for captcha'
        time.sleep(1)
        captchaGet = sesh.get("http://2captcha.com/res.php", params = getData)

    JSONDict2 = json.loads(captchaGet.text)

    return str(JSONDict2['request'])


print c()
