# -*- coding: utf-8 -*-
from mastodon import Mastodon
import hidden
import random
import time

##############
# initialize #
##############

mastodon_hostname = 'botsin.space'      # your domain.name here
secret = hidden.secret()                # store your secrets in hidden.py's secret(), as a dict()
api_base_url = 'https://' + mastodon_hostname

visibility = 'unlisted'                 # visibility can be 'direct' 'private' 'unlisted' or 'public'

mastodon = Mastodon(client_id = secret['client_id'], client_secret = secret['client_secret'], access_token = secret['access_token'], api_base_url = api_base_url)
headers = { 'Authorization': 'Bearer %s'%secret['access_token'] }

##########
# log in #
##########

try:
    mastodon.log_in(username = secret['email'], password = secret['password'], code = None, redirect_uri = "urn:ietf:wg:oauth:2.0:oob", scopes = ['write'])
    print('Successfully logged in!')
except:
    print('Failed to log in. Check your hidden.py file and try again.')
    quit()

##############
# toot stuff #
##############
active = True
while active:
    try:
        toot_list = [line.strip() for line in open('quotes.txt')]
        toot_text = random.choice(open('quotes.txt').readlines())
    except:
        print('Could not generate toot_text. Check your text file and try again.')
        active = False
    try:
        status = mastodon.status_post(status = toot_text, visibility = visibility)
        print('Toot success!')
        print('This toot:\n{}\n...was posted at {}.'.format(toot_text, status['created_at']))
        print()
    except:
        print('Failed to toot. :(')
        active = False
    time.sleep(6*60*60)     # every 6 hours
