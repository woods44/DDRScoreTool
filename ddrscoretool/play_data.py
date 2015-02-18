#!/usr/bin/python
#-*- coding:shift_jis -*-
import re
import urllib
import urllib2
import html_get


class Play_data:
    """�R���X�g���N�^ """
    def __init__(self):
        self._detail_html = ""
        return None
    
    """�Ȗ���indexID�̒��o"""
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

    """�v���C�f�[�^�������擾����B """
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

    """�ڍׂȃv���C�f�[�^�̃y�[�W�̎擾 """
    def get_detail_page(self,music_id,diff,opener):
        """[�v���C��,�N���A��,�ō��R���{,�t���R���{,�ŏI�v���C����,�S���r,�S��X�R�A,�S��l��,���x��]"""
        data_music = []
        html_getter = html_get.Html_get(music_id)
        a_url = 'http://p.eagate.573.jp/game/ddr/ac/p/playdata/music_detail.html?index='+str(music_id)+'&diff='+str(diff)
        a_html = html_getter.url_html_get(opener,a_url)
        print "id:"+str(music_id)+" diff:"+str(diff)
        a_play_count = self.play_count(a_html)
        if a_play_count == 0:
            return "NoPlay"
        a_level = self.play_level(a_html)
        a_clear = self.clear_count(a_html)
        a_max_combo = self.max_combo(a_html)
        top_who = self.top(a_html)
        top_score = self.top_score(a_html)
        data_music = [a_play_count,a_clear,a_max_combo,top_score,top_who,a_level]
        return data_music
        

    """���x��"""
    def play_level(self,a_html):
        print "Search level"
        a_high_score_pat = re.compile('<th>�ō��_���X���x��</th><td>(E|D|C|B|A*)</td>')
        level = a_high_score_pat.search(a_html)
        if not level is None:
            return level.group(1)
        return "NoPlay"
        
    """�v���C�� """
    def play_count(self,a_html):
        print "Count Play"
        a_play_count_pat = re.compile('[^�A]��</th><td>([0-9]*)</td>')
        count = a_play_count_pat.search(a_html)
        print count
        if not count is None:
            return count.group(1)
        return 0

    """�N���A��"""
    def clear_count(self,a_html):
        print "Count Clear"
        a_clear_pat = re.compile('�A��</th><td>([0-9]*)</td>')
        count = a_clear_pat.search(a_html)
        if not count is None:
            return count.group(1)
        return 0

    """�ő�R���{��"""
    def max_combo(self,a_html):
        print("Max Combo");
        a_max_combo_pat = re.compile('�ő�R���{��</th><td>([0-9]*)</td>')
        combo = a_max_combo_pat.search(a_html)
        if not combo is None:
            return combo.group(1)
        return 0

    """�S���g�b�v"""
    def top(self,a_html):
        print("World Record")
        a_pat = re.compile('�S���g�b�v</p>(.*)<span style="float:right;">([0-9]*)</span>')
        a_who = a_pat.search(a_html)
        if not a_who is None:
            return a_who.group(1)
        return 0

    """�S���g�b�v�X�R�A"""
    def top_score(self,a_html):
        a_pat = re.compile('�S���g�b�v</p>.*<span style="float:right;">([0-9]*)</span>')
        a_score = a_pat.search(a_html)
        if not a_score is None:
            return a_score.group(1)
        return 0