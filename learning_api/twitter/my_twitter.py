import urllib
import json
import requests
import codecs
from random import randint

#import modules for OAuth authentication
from requests_oauthlib import OAuth1
#from requests_oauthlib import OAuth2

# Variables that contains the user credentials to access Twitter API 
Consumer_Key = '5ghAMyEWYe9iyOjCkmutOWWXKX'
Consumer_Secret = 'RF2qOVYQpXYjSQZ9SEd1QaddlL04EWwXXbNgjcaNvY58u7m3BD'
Access_Token = '112072231-xRBiwnREcUFL31fXZ3dfhXwohPiWMbBfCmvPdlXR'
Access_Token_Secret =  'XwKkvr7KAMG5FZpkoy1sDdS5lMOshzChwKCcLqBYG5EyJX'
auth = OAuth1(Consumer_Key, Consumer_Secret, Access_Token, Access_Token_Secret)

#twitter api base url
base_url = 'https://api.twitter.com/1.1/'

#get a list of followers in user id : name format
def get_followers():
	print("Pulling List of your followors.......!!")
	url = '{}followers/list.json'.format(base_url)
	r = requests.get(url, auth=auth)
	f_json =  r.json()	
	for x in f_json['users']:
		print('Name: {1} , Screen Name {0}'.format(x['screen_name'], x['name']))

	print('\n \n')

#pull latest tweet from timeline
def get_tweet_from_timeline():
	print("Pulling tweets from your timeline.......!!")
	url = '{}statuses/home_timeline.json'.format(base_url)
	timeline_data = requests.get(url, auth=auth)
	timeline_data_json =  timeline_data.json()
	with codecs.open('my_timeline.txt', 'w', encoding = "utf-8") as timeline_file:
		json.dump(timeline_data_json, timeline_file, indent = 4, ensure_ascii = False)

	for x in timeline_data_json:
		print("{} : {} : {}".format(x['user']['name'].encode('utf-8'), x['user']['screen_name'].encode('utf-8'), x['text'].encode('utf-8')))

#post tweets to timeline
#example_ url = 'https://api.twitter.com/1.1/statuses/update.json?status={}'
#tweet_message = urllib.quote(tweet)

def post_tweet_to_timeline():
	print("Posting tweets to your timeline.......!!")
	url = '{}statuses/update.json'.format(base_url)
	tweet = raw_input("Write your tweet here:")
	data = {'status' : tweet}
	#url_tweet = '{}'.format(url, tweet_message)
	r = requests.post(url, auth=auth, params = data)
	return r.status_code

#post message to user using user's screen name
#message = urllib.quote(msg)
#example_ url = 'https://api.twitter.com/1.1/direct_messages/new.json?text={}&screen_name={}'
def post_message_to_user(msg, screen_name):
	print("Sending message to {}.......!!".format(screen_name))
	data = {'text' : msg,
			'screen_name' : screen_name}
	url = '{}direct_messages/new.json'.format(base_url)
	r = requests.post(url, auth=auth, params = data )
	return r.status_code

#post_welcome_message_to_user, requires dms enable in settings. 
def post_welcome_message_to_user(msg):
	print("Sending welcome message to {}.......!!".format(screen_name))
	message = { "welcome_message" : { "message_data": { "text": "Welcome!"} } }
	url = '{}direct_messages/welcome_messages/new.json'.format(base_url)
	r = requests.post(url, auth=auth, json=message )
	print(r.json())
	return r.status_code

if __name__ == '__main__':
	
	get_followers()

	get_tweet_from_timeline()

	status = post_tweet_to_timeline()

	status = post_message_to_user('Welcome to twitter {}!!'.format(randint(1 , 10)), 'srawla')

	#status = post_welcome_message_to_user('welcome message by rule')
	try:
		if status == requests.codes.ok:
			print("Success!!")
		else:
			print("Failure: OOPS something went wrong {}".format(status))
	except NameError as e:
		print("No Status Returned \n{}".format(e))

	
	

	

