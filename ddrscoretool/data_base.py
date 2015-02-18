#!/usr/bin/python
#-*- coding:utf-8 -*-
import sqlite3


class Data_base:
    """コンストラクタ"""
    def __init__(self):
        self.music_data = sqlite3.connect("music_info.db")
        self.music_data.text_factory = str
        try:
            print("Create music information data base")
            sql = "create table music(id integer primary key,name String);"
            self.music_data.execute(sql)
        except sqlite3.Error,e:
            print "An error sql",e.args[0]
        try:
            print("Create music information table")
            sql = "create table score(id integer,diff integer,score integer);"
            self.music_data.execute(sql)
        except sqlite3.Error,e:
            print "An error sql",e.args[0]
        print("Create music score table")
        try:
            print("Create music information data base")
            sql = "create table level(id integer,diff integer,level String);"
            self.music_data.execute(sql)
        except sqlite3.Error,e:
            print "An error sql",e.args[0]

        try:
            print("Create music information data base")
            sql = "create table top(id integer,diff integer,name String,score integer);"
            self.music_data.execute(sql)
        except sqlite3.Error,e:
            print "An error sql",e.args[0]


        return None

    """データベースに曲とidを保存する """
    def add_music(self,music_datas):
        sql = "insert into music values (?,?)"
        for (id,name) in music_datas:
            try:
                self.music_data.execute(sql,(id,str(name)))
            except sqlite3.Error,e:
                print "An error sql",e.args[0]
        self.music_data.commit()
        return None

    """idと難易度別のスコアを保存する"""
    def add_score(self,music_scores):
        sql = "insert into score values (?,?,?)"
        for (id,diff,score) in music_scores:
            try:
                self.music_data.execute(sql,(id,diff,score))
            except sqlite3.Error,e:
                print "Error",e.args[0]
        self.music_data.commit()
        return None

    """ダンスレベルを登録する"""
    def add_level(self,index,diff,level):
        sql = "insert into level values(?,?,?)"
        try:
            self.music_data.execute(sql,(index,diff,level))
        except sqlite3.Error,e:
            print "Error",e.args[0]
        self.music_data.commit()
        return None

    """全国を登録"""
    def add_top(self,index,diff,name,score):
        sql = "insert into top values(?,?,?,?)"
        try:
            self.music_data.execute(sql,(index,diff,name,score))
        except sqlite3.Error,e:
            print "Error",e.args[0]
        self.music_data.commit()
        return None