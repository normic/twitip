import sys
import twitter
import urllib.request
from configparser import ConfigParser


__version__ = '0.2'
__title__ = 'twitip'
__description__ = 'Tool which twitters the current IP address with basic template support.'


def main():
    response = urllib.request.urlopen('http://icanhazip.com')
    curip = response.read().decode('utf-8').strip()
    print("Your IP address is:", curip)
    sendtwitter(createmessage(curip))


def sendtwitter(msg):
    api = twitter.Api(
        consumer_key=TWITTER_CONSUMER_KEY,
        consumer_secret=TWITTER_CONSUMER_SECRET,
        access_token_key=TWITTER_ACCESS_TOKEN_KEY,
        access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )
    try:
        status = api.PostUpdate(msg)
    except twitter.TwitterError as e:
        print("Error while sending message", e)
        sys.exit(3)


def createmessage(ipaddress):
    ip_array = ipaddress.split('.')

    # msgtpl = "My IP Address in {0} is: {1}.{2}.{3}.{4}"
    msg = MSGTPL.format(LOCATION, ip_array[0], ip_array[1], ip_array[2], ip_array[3])
    print(msg)
    return msg


if __name__ == "__main__":
    # version info
    print(__title__, __version__, " - ", __description__)

    # look for and read config file
    config = ConfigParser()

    try:
        with open('twitip.ini') as f:
            config.read_file(f)
    except IOError:
        print("Error: twitip.ini not found in current directory!")
        sys.exit(2)

    try:
        LOCATION = config['General'].get('location', 'my castle')
        MSGTPL = config['General'].get('message', 'My IP Address in {0} is: {1}.{2}.{3}.{4}')
    except KeyError:
        print("Error: Did you forgot to add a [General] section?")
        sys.exit(2)

    try:
        TWITTER_CONSUMER_KEY = config['General']['TWITTER_CONSUMER_KEY']
    except KeyError:
        print("Error: TWITTER_CONSUMER_KEY not found!")
        sys.exit(2)

    try:
        TWITTER_CONSUMER_SECRET = config['General']['TWITTER_CONSUMER_SECRET']
    except KeyError:
        print("Error: TWITTER_CONSUMER_SECRET not found!")
        sys.exit(2)

    try:
        TWITTER_ACCESS_TOKEN_KEY = config['General']['TWITTER_ACCESS_TOKEN_KEY']
    except KeyError:
        print("Error: TWITTER_ACCESS_TOKEN_KEY not found!")
        sys.exit(2)

    try:
        TWITTER_ACCESS_TOKEN_SECRET = config['General']['TWITTER_ACCESS_TOKEN_SECRET']
    except KeyError:
        print("Error: TWITTER_ACCESS_TOKEN_SECRET not found!")
        sys.exit(2)

    main()
