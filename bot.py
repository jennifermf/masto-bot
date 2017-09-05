# -*- coding: utf-8 -*-

import argparse
import sys
import random
import time
from mastodon import Mastodon


# parse command line arguments

argument_parser = argparse.ArgumentParser(description="Simple Bot for the Mastodon social network")

argument_parser.add_argument("-cc", "--client-credentials", help="filename the client credentials should be stored to", type=str, default=".masto-bot.clientcred.secret")
argument_parser.add_argument("-uc", "--user-credentials", help="filename the user credentials should be stored to", type=str, default=".masto-bot.usercred.secret")
argument_parser.add_argument("-i", "--input-file", default="quotes.txt", help="The file the quotes are read from. Quotes are separated by an empty line, followed by three minus signs, followed by an empty line.")
argument_parser.add_argument("-u", "--username", help="fully qualified username", type=str, required=True)
argument_parser.add_argument("-t", "--time-interval", help="Time (in seconds) to wait in between toots.", type=int, default=6*60*60)
argument_parser.add_argument("-v", "--visibility", help="Visibility scope of toots.", choices=('public', 'unlisted', 'private'), default='unlisted')

args = argument_parser.parse_args()

try:
    (username, hostname) = args.username.split("@")
except ValueError:
    sys.exit("username must be of format username@servername, e.g. <emma.goldman@anarchists.in.space>")
except:
    sys.exit("unexpected error while parsing username")


# establish connection to Mastodon server

mastodon_connection = Mastodon(client_id = args.client_credentials, access_token = args.user_credentials, api_base_url = "https://%s"%(hostname,))


# toot stuff

def not_too_long(toot):
    if len(toot) > 500:
        return False
    elif len(toot) == 0:
        return False
    else:
        return True

# read file that is given as first command line argument,
# split it along empty lines,
# throw out texts that are longer than 500 characters,
# and have it be a list (filter returns an interable, which is not compatible with random.choice(),
## because it as no pre-known length)

toot_list = [ x for x in filter(not_too_long, open(args.input_file).read().split('\n---\n')) ]

active = True

while active:
    try:
        toot_text = random.choice(toot_list)
    except:
        print('Could not generate toot_text. Check your text file and try again.')
        active = False
        break
    try:
        status = mastodon_connection.status_post(status = toot_text, visibility = args.visibility)
        print('Awoooooooo!')
        print('This toot:\n{}\n...was posted at {}.'.format(toot_text, status['created_at']))
        print()
    except:
        print('Failed to toot. :(')
        active = False
        break
    time.sleep(args.time_interval)

