========================
Yet Another Mastodon Bot
========================

A pretty simple Python3 script which posts random lines from a .txt file to a Mastodon account.
Originally named spn-bot because it was made to post quotes from the TV series Supernatural.

Uses Mastodon.py, a fantastic Mastodon API wrapper:
http://mastodonpy.readthedocs.io/

========================
Get Started:
========================

1.  Set mastodon_hostname to the instance where your bot will live.
    Set time.sleep() post frequency (in seconds).

2.  You will need to generate a client_id, client_secret, and access_token, if you don't have one already.
    https://github.com/tootsuite/documentation/blob/master/Using-the-API/Testing-with-cURL.md
    This tool may be helpful:
    https://tinysubversions.com/notes/mastodon-bot/

    You will have to create/edit a file named hidden.py, containing this function:

    def secret():
        return {
        'client_id': 'xxxxxxxxxxxxxxxxxxxxxxxx',
        'client_secret': 'xxxxxxxxxxxxxxxxxxxxxxxx',
        'access_token': 'xxxxxxxxxxxxxxxxxxxxxxxx',
        'email': 'bot_email@email.internet.com',
        'password': 'bot_pwd'}

========================
Wishlist:
========================

Future versions will include the ability to parse and post 500-ish character blocks from full books or texts.

