#!/usr/bin/python
# -*- conding=utf-8 -*-

import cookielib
import urllib2
import urllib

class Login:
    
    def __init__(self):
        """addres for login """
        self.login_url = "https://p.eagate.573.jp/game/ddr/ac/p/login.html"
        self.post_params = {"KID":"***","pass":"***","OTP":""}


    """Try to login konami site"""
    def login_konami(self):
       cookie_jar = cookielib.MozillaCookieJar("cookies.txt")
       opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
       request = opener.open(self.login_url,urllib.urlencode(self.post_params))
       return opener
