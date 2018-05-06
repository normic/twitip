import twitter
import urllib.request

__version__ = '0.1'
__title__ = 'twitip'
__description__ = 'Tool which twitters the current IP address with basic template support.'


LOCATION = ''
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN_KEY = ''
TWITTER_ACCESS_TOKEN_SECRET = ''


def main():
    print(__title__, __version__, " - ", __description__)

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
    status = api.PostUpdate(msg)


def createmessage(ipaddress):
    ip_array = ipaddress.split('.')

    msgtpl = "My IP Address in {0} is: {1}.{2}.{3}.{4}"
    msg = msgtpl.format(LOCATION, ip_array[0], ip_array[1], ip_array[2], ip_array[3])
    print(msg)
    return msg


if __name__ == "__main__":
    main()
