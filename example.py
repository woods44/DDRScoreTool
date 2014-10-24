#!/usr/bin/python
# -*- conding=utf-8 -*-

import play_data
import login
import urllib2

if __name__ == "__main__":
    print("start")
    login = login.Login()
    opener = login.login_konami()
    data = play_data.Play_data()
    data.play_data_html(opener)
