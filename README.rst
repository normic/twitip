======
twitip
======
Python tool which twitters your current public IP address and 
provides very basic template support.

Currently tested against Python 3.5 on Linux systems only.

-----
Usage
-----
twitip expects a file `twitip.ini` in it's directory.

Sample file could be::

    [General]
    LOCATION    = my Castle
    MESSAGE     = My current IP address in {0} is: {1}.{2}.{3}.{4}

    TWITTER_CONSUMER_KEY =
    TWITTER_CONSUMER_SECRET =
    TWITTER_ACCESS_TOKEN_KEY =
    TWITTER_ACCESS_TOKEN_SECRET =


Where {0} refers to the LOCATION entry.
And {1} to {4} refers to the octets of the IP address.

The TWITTER vars have to be set correctly, otherwise you won't be able to use the twitter API.

