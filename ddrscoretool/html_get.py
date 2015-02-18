#!/usr/bin/python
# -*- coding=utf-8 -*-

import cookielib
import urllib2
import urllib

class Html_get:
    """コンストラクタ"""
    def __init__(self,index):
        self.play_data_url = "http://p.eagate.573.jp/game/ddr/ac/p/playdata/music_data_single.html?offset="+str(index)

    """HTMLファイルのテキストを取得する """
    def html_get(self,opener,a_page_number):
        a_request = opener.open(self.play_data_url)
        a_html = a_request.read()
        print("end to load html No."+str(a_page_number)+" file.")
        return a_html

    def url_html_get(self,opener,a_url):
        a_request = opener.open(a_url)
        a_html = a_request.read()
       # print('end to load'+str(a_url)+'html file.')
        return a_html
