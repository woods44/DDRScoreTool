#!/usr/bin/python
# -*- coding=utf-8 -*-
import cookielib
import urllib2
import urllib


class Login:
    """コンストラクタ """
    def __init__(self,a_id,a_pass):
        self.login_url = "https://p.eagate.573.jp/game/ddr/ac/p/login.html"
        self.post_params = {"KID":a_id,"pass":a_pass,"OTP":""}
        
        return None
    """ログイン後セッションを保存"""
    def login(self):
        cookie_jar = cookielib.MozillaCookieJar("cookies.txt")
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
        a_request = opener.open(self.login_url,urllib.urlencode(self.post_params))
        return opener
        
