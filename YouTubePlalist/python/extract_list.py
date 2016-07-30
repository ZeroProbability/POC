#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import requests
import re

def main():
    r  = requests.get("https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb")
    soup = BeautifulSoup(r.text, "lxml")
    html_table = soup.find(id="pl-video-table")
    for link in html_table.find_all("a"):
        link_text = link.get('href')
        if link_text.startswith('/watch?v='):
            match_obj = re.search('.*?v=(.*?)&', link_text)
            if match_obj:
                yt_id = match_obj.groups()[0]
                print 'http://www.youtube.com/watch?v={}'.format(yt_id)

if __name__ == '__main__':
    main()
