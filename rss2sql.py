#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, requests
from pyPodcastParser.Podcast import Podcast


headers = {'User-Agent': 'curl/7.64.0 (x86_64-pc-linux-gnu) +https://govorenefekt.com/bot GEfektBot/1.0'}


def parser(feedurl):
    response = requests.get(feedurl, headers=headers)
    pod = Podcast(response.content)
    title = pod.title or "няма данни"
    fname = title.replace(" ","_")
    description = pod.description or "няма данни"
    link = pod.link or "няма данни"
    category = ','.join(pod.itunes_categories) or "няма данни"
    with open(fname.lower() + '.sql', 'w') as f:
        print("INSERT INTO pods (title, description, website,rssfeed,category)\nVALUES(\""  + 
        title + "\",\n\"" +
        description + "\",\n\"" + 
        link + "\",\n\"" + 
        feedurl +  "\",\n\"" +
        category + "\");",
        file = f)


def main():
    feedurl = sys.argv[1]
    parser(feedurl)


if __name__ == '__main__':
    main()	
