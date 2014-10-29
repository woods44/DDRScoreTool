#!/usr/bin/python
#-*- coding:utf-8 -*-
import sqlite3


class Data_base:
    """コンストラクタ"""
    def __init__(self):
        self.music_data = sqlite3.connect("music_info.db")
        self.music_data.text_factory = str
        print("Create music infomation data base")
        sql = "create table music(id integer primary key,name String);"
        self.music_data.execute(sql)
        print("Create music infomation table")
        sql = "create table score(id integer,diff integer,score integer);"
        self.music_data.execute(sql)
        print("Create music score table")


        return None

    """データベースに曲とidを保存する """
    def add_music(self,music_datas):
        sql = "insert into music values (?,?)"
        for (id,name) in music_datas:
            self.music_data.execute(sql,(id,str(name)))
        self.music_data.commit()
        return None

    """idと難易度別のスコアを保存する"""
    def add_score(self,music_scores):
        sql = "insert into score values (?,?,?)"
        for (id,diff,score) in music_scores:
            self.music_data.execute(sql,(id,diff,score))
        self.music_data.commit()
        return None
