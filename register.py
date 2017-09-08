# -*- coding: utf-8 -*-

import sys
import os
import argparse
from mastodon import Mastodon


# parse command line arguments

argument_parser = argparse.ArgumentParser(description="Creates two files: one for client- and one for user-credentials that are subsequentially used to authenticate the Mastodon bot at the server.")

argument_parser.add_argument("-p", "--password", help="password. please note that most terminal shells keep a history!", type=str)
argument_parser.add_argument("-cc", "--client-credentials", help="filename the client credentials should be stored to", type=str, default=".masto-bot.clientcred.secret")
argument_parser.add_argument("-uc", "--user-credentials", help="filename the user credentials should be stored to", type=str, default=".masto-bot.usercred.secret")
argument_parser.add_argument("-u", "--username", help="fully qualified username", type=str, required=True)
argument_parser.add_argument("-e", "--email", help="email address for login", type=str, required=True)

args = argument_parser.parse_args()


# check username argument. it needs to consist of two parts, separated by "@"

try:
    (username, hostname) = args.username.split("@")
except ValueError:
    sys.exit("username must be of format username@servername, e.g. <emma.goldman@anarchists.in.space>")
except:
    sys.exit("unexpected error while parsing username")


# check for already existing credentials files

if os.path.exists(args.client_credentials):
    userinput = input("%s already exists. Would you like to overwrite it? (yes,no): "%(args.client_credentials,))
    if userinput != 'yes':
        sys.exit()

if os.path.exists(args.user_credentials):
    userinput = input("%s already exists. Would you like to overwrite it? (yes,no): "%(args.user_credentials,))
    if userinput != 'yes':
        sys.exit()


# if no password is given via command line, ask interactively

if not args.password:
    password = input("Password for %s: "%(args.username,))
else:
    password = args.password


# register the bot

Mastodon.create_app(
     "%s-bot"%(username,),
     api_base_url = "https://%s"%(hostname,),
     to_file = args.client_credentials
)

mastodon_connection = Mastodon(
        client_id = args.client_credentials,
        api_base_url = "https://%s"%(hostname,)
)

mastodon_connection.log_in(
    args.email,
    password,
    to_file = args.user_credentials
)
