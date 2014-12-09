#!/usr/bin/python -S
# -*- coding:utf-8 -*-

import html_get
import play_data
import data_base
import login
import urllib2
import time
import sys
import codecs
import score_export



"""作成したクラス群を実行する """

class Example(object):
    def main(self):
        music_score_data = [[[]]]
        music_data = [[]]
        arguments = sys.argv
        a_id = str(arguments[1])
        a_pass = str(arguments[2])
        login_get = login.Login(a_id,a_pass)
        opener = login_get.login()
        getter_data = play_data.Play_data()
        play_data_base = data_base.Data_base()
        for index in range(0,1):
            time.sleep(5)
            html_getter = html_get.Html_get(index)
            html_data = html_getter.html_get(opener,index)
            music_data  = getter_data.get_music_info(html_data)
            music_score_data = getter_data.get_play_data(html_data)
            if not index == 0:
                del music_data[0]
                del music_score_data[0]
            play_data_base.add_music(music_data)
            play_data_base.add_score(music_score_data)
        for (id,name) in music_data:
            for diff in range(0,5):
                time.sleep(1)
                detail_data = getter_data.get_detail_page(id,diff,opener)
                if detail_data == "NoPlay":
                    continue
                print "id:"+str(id)+" diff:"+str(diff)+" detail:"+str(detail_data[1])
                play_data_base.add_level(id,diff,detail_data[1])
               
               
        score = score_export.ScoreExport()
        score.all_music_info()
        
        
