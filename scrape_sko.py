__author__ = 'mich'
import urllib2
from bs4 import BeautifulSoup


# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

def getDayResult(url=list()):
    day = list()
    chan = list()
    title = list()
    time = list()
    viewers = list()
    viewers_kdh = list()
    viewers_madl = list()

    for eachUrl in url:
        print eachUrl
        soup = BeautifulSoup(urllib2.urlopen(url).read())

        for eachRow in soup.find_all('td','kc_headerleft'):
            channel =  eachRow.string

        for eachRow in soup.find_all('td','kc_headerright'):
            whatday = eachRow.string

        oddEven = 1
        for eachRow in soup.find_all('td','kc_cdtitle'):
            chan.append(channel)
            day.append(whatday)
            title.append(eachRow.string)

        for eachRow in soup.find_all('td','kc_cdcb'):
            time.append(eachRow.string)

        for eachRow in soup.find_all('td','kc_cdrt0'):
            if oddEven%2 == 0:
                viewers.append(eachRow.string)
            else:
                viewers_kdh.append(eachRow.string)

            oddEven += 1

        for eachRow in soup.find_all('td','kc_cdrt1'):
            viewers_madl.append(eachRow.string)


    return zip(chan, day, time, title, viewers, viewers_kdh, viewers_madl)



channels = list()
channelNrs = (1,2,47)
for whatChannel in channelNrs:
    for broadCasted in range(0, 14):
        url = 'http://kijkonderzoek.nl/component/com_kijkcijfers/Itemid,133/file,dp-' + str(broadCasted) + '-' + str(whatChannel) + '-0-p'
        channels.append(url)





result = getDayResult(url=channels)