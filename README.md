
Yet Another Mastodon Bot
========================

A pretty simple Python3 script which posts random lines from a .txt file to a Mastodon account.
Originally named spn-bot because it was made to post quotes from the TV series Supernatural.

Uses Mastodon.py, a fantastic Mastodon API wrapper:
http://mastodonpy.readthedocs.io/

Get Started:
========================

1. Install Mastodon.py: `pip3 install Mastodon.py`
2. Run `python3 register.py` with at least the `--username` and `--email` parameters.
3. Run `python3 bot.py` with at least the `--username` parameter.


Wishlist:
========================

- And get rid of that time.sleep() thing in favor of actual scheduled tasks.

