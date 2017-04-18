##Desktop Silicon Valley Company News Web Scraper##
##Finished Sunday, August 4th, 2015##
## Software for Stan Chudnovsky##

#from urllib import urlopen
import urllib2
from webbrowser import open_new
from time import sleep
from subprocess import check_output
from os import system
from sys import exit

from bs4 import BeautifulSoup

urls = ["http://techcrunch.com/", 
	"http://www.silicontap.com/",
	"http://www.siliconbeat.com/",
	"http://venturebeat.com/",
	"http://www.entrepreneur.com/latest"]

header = """Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) 
		Gecko/20091102 Firefox/3.5.5"""

check_if_just_launched = 0

def get_html(url):

	req = urllib2.Request(str(url), 
						None, 
						{'User-agent' : header})

	response = urllib2.urlopen(req).read()
	soup = BeautifulSoup(response, "html.parser")
	return soup


def get_date_and_titles(
		url, 
		root_tag, 
		root_class, 
		date_tag, 
		header_tag, 
		*args):

	print('\n' + "Oldest at top, Newest at bottom" + '\n')
	
	for div_outer in reversed(
		get_html(url).find_all(str(root_tag), 
		{"class": str(root_class)})):

		if ''.join(div_outer['class']) == "river-blockriver-block-video":
			continue

		if len(args) == 0:
			print(div_outer.find(str(header_tag)).text)
			print(div_outer.find(str(date_tag)).text.strip() + '\n')
		else:
			print(div_outer.find(
				str(header_tag), 
				{"class": str(args[0])}).text)
			print(div_outer.find(
				str(date_tag), 
				{"class": str(args[1])}).text.strip() + '\n')


def ask_for_site(url):

	question = raw_input("Would you like to see the site? Y or N >> ")

	if question in ("Y", "y"):
		open_new(url)
	elif question in ("N", "n"):
		print("Returning to choices...")
		# sleep(1)
		display_user_interface()
	else:
		print("Invalid phrase. Try again")
		ask_for_site(url)

def quit_options():

	options = raw_input("""Would you like to minimize screen until next 
		interval OR kill process? q or k (Press u to undo) >> """)

	if options in ("q", "Q"):
		system("printf '\e[2t'")
	elif options in ("k", "K"):
		exit()
	elif options in ("u", "U"):
		display_user_interface()
	else:
		print("Invalid phrase. Try again")
		quit_options()


def display_user_interface():

	x = raw_input("""Would you like to view:
	a)Techcrunch
	b)Silicontap
	c)Siliconbeat
	d)Venturebeat
	e)Enterpreneur
		
	Press the letter associated with the site you want or "q" to quit >> """)

	if x in ("a", "A", "Techcrunch", "techcrunch"):
		get_date_and_titles(
			urls[0], 
			'li', 
			'river-block', 
			'time',  
			'h2',
			'post-title',
			'timestamp')

		ask_for_site(urls[0])

	elif x in ("b", "B", "Silicontap", "silicontap"):
		get_date_and_titles(
			urls[1], 
			'li', 
			'post', 
			'small', 
			'h2') 

		ask_for_site(urls[1])

	elif x in ("c", "C", "Siliconbeat", "siliconbeat"):
		get_date_and_titles(
			urls[2], 
			'div', 
			'post-excerpt', 
			'time',  
			'a') 

		ask_for_site(urls[2])

	elif x in ("d", "D", "Venturebeat", "venturebeat"):
		get_date_and_titles(
			urls[3], 
			'header', 
			'article-header', 
			'time',  
			'h2',
			'article-title',
			'the-time')

		ask_for_site(urls[3])

	elif x in ("e", "E", "Enterpreneur", "enterpreneur"):
		get_date_and_titles(
			urls[4], 
			'div', 
			'pl pl-floathero', 
			'time',  
			'h3')

		ask_for_site(urls[4])

	elif x == "q":
		quit_options()
		return 1

	else:
		print("Invalid phrase. Please try again")
		display_user_interface()

while True:
	#sleep(1800)
	if check_if_just_launched != 0:
		sleep(10)

	check_if_just_launched = 1

	system("printf '\e[1t'")
	system("printf '\e[5t'")

	instance_question = display_user_interface()
	
	if instance_question == 1:
		continue

	while True:
		sleep(2)
		
		y = raw_input("""Would you like to view another site's articles? 
			Y or N >> """)  

		if y in ("Y", "y"):
			sleep(1)
			display_user_interface()
		elif y in ("N", "n"):
			sleep(1)
			print("Awaiting next interval")
			system("printf '\e[2t'")
			break

#seems like everything is working


