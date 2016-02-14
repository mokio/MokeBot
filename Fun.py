import discord
import json
import requests
import urllib2
import sys
import csv
from bs4 import BeautifulSoup
from tabulate import tabulate
import wikipedia
from wikipedia.exceptions import PageError, DisambiguationError
import random
reload(sys)
sys.setdefaultencoding('utf-8')

def wikiSearch(searchWord):
    try:
        summary = wikipedia.summary(searchWord)
        summary = summary[:2000]
        summary = summary.encode('utf-8')
    except DisambiguationError as e:
        summary = e
    except PageError:
        summary = "No wikipedia page exists"
    return summary

def urbanSearch(define):
    r = requests.Session()
    URL = 'http://api.urbandictionary.com/v0/define?term={0}'.format(define)
    response = r.get(URL)
    data = json.loads(response.text)
    if data['result_type'] == 'no_results':
        definition = '"' + define +'" is not defined'
    else:
        definition = data['list'][0]['definition']
        definition = define +': ' + definition
    return definition
	
def rollTheDice(game_list):
	return random.choice(game_list)

def addGame(game, game_list):
	f = open('game_list.txt', 'a')
	f.write(game+'\n')
	game_list.extend([game])
	f.close()
	return game_list
	
def checkEm():
	x = random.randint(100000, 999999)
	list = [int(i) for i in str(x)]
	if list[3] == list[4] == list[5] == list[2] == list[1] == list[0]:
		return str(x) + " You win the fucking game."
	elif list[3] == list[4] == list[5] == list[2] == list[1]:
		return str(x) + " Check em mother fucker."
	elif list[3] == list[4] == list[5] == list[2]:
		return str(x) + " Check em quads!"
	elif list[3] == list[4] == list[5]:
		return str(x) + " Check em trips!"
	elif list[4] == list[5]:
		return str(x) + " Check em dubs!"
	else:
		return str(x)
	
def roll(n = None):
	if n == None:
		n = 100
	else:
		n = int(n)
	return random.randint(0,n)
	
def rps(first, second):
	x = random.randint(1, 3)
	y = random.randint(1, 3)
	if x == y:
		return "Players have tied, rolling again.\n\n" + rps(first, second)
	elif x == 1 and y == 3 :
		return "%s: Rock\n\n%s: Scissors\n\n%s wins!" % (first, second, first)
	elif x == 2 and y == 1:
		return "%s: Paper\n\n%s: Rock\n\n%s wins!" % (first, second, first)
	elif x == 3 and y == 2:
		return "%s: Scissors\n\n%s: Paper\n\n%s wins!" % (first, second, first)
	elif y == 1 and x == 3 :
		return "%s: Rock\n\n%s: Scissors\n\n%s wins!" % (second, first, second)
	elif y == 2 and x == 1:
		return "%s: Paper\n\n%s: Rock\n\n%s wins!" % (second, first, second)
	elif y == 3 and x == 2:
		return "%s: Scissors\n\n%s: Paper\n\n%s wins!" % (second, first, second)

	














