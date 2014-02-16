__author__ = 'mich'
import urllib2
from bs4 import BeautifulSoup


# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

soup = BeautifulSoup(
    urllib2.urlopen('http://kijkonderzoek.nl/component/com_kijkcijfers/Itemid,133/file,dp-6-1-0-p').read())

for eachRow in soup.find_all('td','kc_headerleft'):
    channel =  eachRow.string

for eachRow in soup.find_all('td','kc_headerright'):
    day = eachRow.string

title = list()
for eachRow in soup.find_all('td','kc_cdtitle'):
    title.append(eachRow.string)

time = list()
for eachRow in soup.find_all('td','kc_cdcb'):
    time.append(eachRow.string)

viewers = list()
viewers_kdh = list()
oddeven = 1
for eachRow in soup.find_all('td','kc_cdrt0'):
    if oddeven%2 == 0:
        viewers.append(eachRow.string)
    else:
        viewers_kdh.append(eachRow.string)

    oddeven += 1

viewers_madl = list()
for eachRow in soup.find_all('td','kc_cdrt1'):
    viewers_madl.append(eachRow.string)

zip(time, title, viewers, viewers_kdh, viewers_madl)