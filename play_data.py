#!/usr/bin/python
# -*- conding=utf-8 -*-

import cookielib
import urllib2
import urllib

class Play_data:
    def __init__(self):
        self.play_data_url = "http://p.eagate.573.jp/game/ddr/ac/p/playdata/music_data_single.html"

    def play_data_html(self,opener):
        request = opener.open(self.play_data_url)
        files = open('out.html','w')
        files.write(request.read())
        files.close()
        
