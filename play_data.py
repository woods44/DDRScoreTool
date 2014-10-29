#!/usr/bin/python
#-*- coding:utf-8 -*-
import re
import urllib
import urllib2


class Play_data:
    """コンストラクタ """
    def __init__(self):
        return None
    
    """曲名とindexIDの抽出"""
    def get_music_info(self,html_data):
        music_id = []
        music_name = []
        html_tags = []
        music_info = []
        a_music_pat = re.compile('index=[0-9]*?"[\s]?class="music_info.*?</a>')
        a_music_id_pat = re.compile('index=([0-9]*?)"')
        a_music_name_pat = re.compile('cboxelement">(.*?)</a>')
        html_tags = a_music_pat.findall(html_data)
        for index in html_tags:
            a_name = a_music_name_pat.search(index)
            a_music_id = a_music_id_pat.search(index)
            if not a_name is None and not a_music_id is None:
                a_temporary = a_name.group(1)
                music_name.append(a_temporary)
                a_temporary = a_music_id.group(1)
                music_id.append(a_temporary)
        music_info = zip(music_id,music_name)
        return music_info

    """プレイデータ部分を取得する。 """
    def get_play_data(self,html_data):
        music_id = []
        music_diff = []
        music_score = []
        html_tags = []
        a_music_pat = re.compile('index=[0-9]*?&diff=.*?</div></td>')
        a_music_id_pat = re.compile('index=([0-9]*?)&')
        a_music_diff_pat = re.compile('diff=([0-9]*?)"')
        a_music_score_pat = re.compile('display:.*?">([0-9]*?)</div></td>')
        html_tags = a_music_pat.findall(html_data)
        for index in html_tags:
            a_music_id = a_music_id_pat.search(index)
            a_music_diff = a_music_diff_pat.search(index)
            a_music_score = a_music_score_pat.search(index)
            if not a_music_id is None and not a_music_diff is None and not a_music_score_pat is None:
                a_temporary = a_music_id.group(1)
                music_id.append(a_temporary)
                a_temporary = a_music_diff.group(1)
                music_diff.append(a_temporary)
                a_temporary = a_music_score.group(1)
                music_score.append(a_temporary)
        
        return zip(music_id,music_diff,music_score)

    """詳細なプレイデータのページの取得 """
    def get_detail_page(self,index,diff):
        a_url = 'http://p.eagate.573.jp/game/ddr/ac/p/playdata/music_detail.html?index='+str(index)+'&diff='+str(diff)
        return a_url

    """詳細なプレイデータの取得 """
    def get_detail_data(self,):
        return None
