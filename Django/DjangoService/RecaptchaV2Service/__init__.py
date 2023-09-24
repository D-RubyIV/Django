import requests, time


class Recaptchav2Service:
    
    def __init__(self, YOUR_APIKEY, SITE_KEY, PAGE_URL) -> None:
        self.YOUR_APIKEY = YOUR_APIKEY
        self.SITE_KEY = SITE_KEY
        self.PAGE_URL = PAGE_URL

    def solve(self):
        url = f"http://api.multibot.in/in.php?key={self.YOUR_APIKEY}&method=userrecaptcha&sitekey={self.SITE_KEY}&pageurl={self.PAGE_URL}"
        result = requests.get(url)
        print(result.text)
        captchaCode = result.text.split("|")[-1]
        return captchaCode

    def getTokenCaptcha(self):
        captchaCode = self.solve()
        url = f'http://api.multibot.in/res.php?key={self.YOUR_APIKEY}&id={captchaCode}'
        stt = 0
        time.sleep(5)  
        while(True):
            response = requests.get(url)
            token_response_raw = response.text
            if 'OK' in token_response_raw:
                token_response = token_response_raw.split('|')[-1]
                print(token_response)
                return token_response
            elif 'CAPCHA_NOT_READY' in token_response_raw:
                print(f"{stt}|{token_response_raw}")
                stt += 1
                time.sleep(5)
            else:
                print(token_response_raw)
                return token_response_raw

Recaptchav2Service("eWC32frEcolg7Y9UtHBKJXAI6whxVs","6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-","https://google.com/recaptcha/api2/demo").getTokenCaptcha()