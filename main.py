import mechanize
import random
import string
import time
import config

googleuser = config.googleUsername
link = config.referalURL


def randString():
	return ''.join(random.choice(string.ascii_uppercase) for i in range(40))

def diversify(user): #dot trick
	newUsername = user.replace('.', '') #remove existing dots
	ranSpot = 1 + random.randrange(len(user))
	newUsername = newUsername[:ranSpot] + '.' + newUsername[ranSpot:]
	print newUsername
	return newUsername

def sleep():
	time.sleep(60)

def refer():
	br = mechanize.Browser()
	br.open(link)
	br.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)')]
	# form = 
	# list(br.forms())[0]
	br.select_form(nr=0)
	br['email'] = googleuser + "+" + randString() + "@gmail.com"
	print br['email']
	br.submit()
	br.close()
	# sleep()




if __name__ == "__main__":
	while True:
		try:
			refer()
		except:
			print "fail"
			googleuser = diversify(googleuser)
			sleep()
			pass