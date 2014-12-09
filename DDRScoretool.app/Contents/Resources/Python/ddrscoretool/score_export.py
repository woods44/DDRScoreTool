#!/usr/bin/python 
#-*- coding:utf-8 -*-

import csv
import sqlite3
import codecs
import sys

class ScoreExport:
    def __init__(self):
        self.music_data = sqlite3.connect('music_info.db')
        self.music_data.text_factory = str
        self.cursor = self.music_data.cursor()
      
        
    def all_music_info(self):
        sql = 'select * from music order by id'
        result = self.cursor.execute(sql)
        print "---------------------export---------------------------"
        for row in result:
            print "id:"+str(row[0])
            print "name:"+str(row[1])
        sql = 'select music.name,score.diff,score.score from music,score  where music.id == score.id order by score.score desc;'
        result = self.cursor.execute(sql)
        print "---------------------export---------------------------"
        for row in result:
            if not row[2] == 0:
                if row[1] == 0:
                    print "name:"+str(row[0])+"-Beginner score:"+str(row[2])
                elif row[1] == 1:
                    print "name:"+str(row[0])+"-Basic score:"+str(row[2])
                elif row[1] == 2:
                    print "name:"+str(row[0])+"-Defficult score:"+str(row[2])
                elif row[1] == 3:
                    print "name:"+str(row[0])+"-Expert score:"+str(row[2])
                elif row[1] == 4:
                    print "name:"+str(row[0])+"-Challenge score:"+str(row[2])
            
        
