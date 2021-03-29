import requests


class TestAddress:
    def setup(self):
        pass

    def test_get_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww67cc50e01d7bab5d&corpsecret=")
        print(r.json())
