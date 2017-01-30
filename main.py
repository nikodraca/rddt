#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup
import sys
import json
import time

reload(sys)
sys.setdefaultencoding('utf-8')


song_list = """ 
http://genius.com/Tyler-the-creator-smuckers-lyrics/
http://genius.com/Yg-twist-my-fingaz-lyrics
http://genius.com/Bryson-tiller-sorry-not-sorry-lyrics
http://genius.com/Rae-sremmurd-come-get-her-lyrics
http://genius.com/Young-thug-best-friend-lyrics
http://genius.com/Future-fuck-up-some-commas-lyrics
http://genius.com/King-los-war-lyrics
http://genius.com/Earl-sweatshirt-faucet-lyrics
http://genius.com/Ty-dolla-sign-blase-lyrics
http://genius.com/Vic-mensa-u-mad-lyrics
http://genius.com/Isaiah-rashad-nelly-lyrics
http://genius.com/Mick-jenkins-ps-and-qs-lyrics
http://genius.com/Freddie-gibbs-careless-lyrics
http://genius.com/Future-where-ya-at-lyrics
http://genius.com/Kanye-west-only-one-lyrics
http://genius.com/Travi-scott-90210-lyrics
http://genius.com/Meek-mill-lord-knows-lyrics
http://genius.com/Jay-rock-gumbo-lyrics
http://genius.com/Action-bronson-baby-blue-lyrics
http://genius.com/The-game-100-lyrics
http://genius.com/Pusha-t-untouchable-lyrics
http://genius.com/Lupe-fiasco-prisoner-1-and-2-lyrics
http://genius.com/A-ap-rocky-l-d-lyrics
http://genius.com/Mac-miller-100-grandkids-lyrics
http://genius.com/Logic-young-jesus-lyrics
http://genius.com/Post-malone-white-iverson-lyrics
http://genius.com/Vince-staples-senorita-lyrics
http://genius.com/Drake-and-future-jumpman-lyrics
http://genius.com/Big-sean-blessings-lyrics
http://genius.com/Dr-dre-darkside-gone-lyrics
http://genius.com/Young-thug-check-lyrics
http://genius.com/Chance-the-rapper-angels-lyrics
http://genius.com/A-ap-rocky-everyday-lyrics
http://genius.com/Joey-bada-paper-trail-lyrics
http://genius.com/Skepta-shutdown-lyrics
http://genius.com/Vince-staples-norf-norf-lyrics
http://genius.com/Earl-sweatshirt-grief-lyrics
http://genius.com/Kanye-west-all-day-lyrics
http://genius.com/Drake-back-to-back-lyrics
http://genius.com/Kendrick-lamar-the-blacker-the-berry-lyrics
http://genius.com/Jay-rock-vice-city-lyrics
http://genius.com/Lupe-fiasco-mural-lyrics
http://genius.com/Fetty-wap-trap-queen-lyrics
http://genius.com/Future-march-madness-lyrics
http://genius.com/Travi-scott-antidote-lyrics
http://genius.com/Drake-know-yourself-lyrics
http://genius.com/Kendrick-lamar-king-kunta-lyrics
http://genius.com/Vince-staples-summertime-lyrics
http://genius.com/Drake-hotline-bling-lyrics
http://genius.com/Kendrick-lamar-alright-lyrics
"""

def grab_lyrics():

	text_file = open("Output3.txt", "w")


	for i in range(1, len(song_list.split('\n'))):
		print song_list.split('\n')[i]

		result = requests.get(song_list.split('\n')[i]).content
		soup = BeautifulSoup(result, "html.parser")

		page = soup.find('p').getText()

		text_file.write(page + "\n###############\n" )
		time.sleep(2)


	text_file.close()


def extract():
	result = requests.get("https://genius.com/Rap-genius-top-20-rap-albums-of-2014-lyrics").content
	soup = BeautifulSoup(result, "html.parser")

	page = soup.find_all('h3')

	for i in range(1, len(page)):
		print page[i].find("a")['href']

text_file = open("txt/output_all.txt", "r")

all_text = text_file.readlines()

counter = 0

for i in range(0, len(all_text)):
	if str(all_text[i])[0] != "#" and str(all_text[i])[0] != "\n" and str(all_text[i])[0] != "[" and str(all_text[i])[0] != "":
		if "er" in str(all_text[i])[-3:]:
			print all_text[i]

		# print str(all_text[i])

print counter
	# if text_file.readlines()[i].strip():
	# print text_file.readlines()[300]
	# 	if (text_file.readlines()[i][0] != "#" or text_file.readlines()[i][0] != "["):
	# 		print text_file.readlines()[i]


# extract()
# grab_lyrics()