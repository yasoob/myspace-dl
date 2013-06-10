#!/usr/bin/env 
 
import urllib2
import json
import re

url = 'http://www.myspace.com/Modules/PageEditor/Handlers/Music/SearchMusic.ashx'
song = raw_input('which song?  ')
data = b'term=%s&maxArtists=0&maxSongs=20' %(song)
headers = {
    'Hash':'MIGcBgkrBgEEAYI3WAOggY4wgYsGCisGAQQBgjdYAwGgfTB7AgMCAAECAmYDAgIAwAQIYLI97pYniaIEEEZ7OzdEz%2bIWLU44SUNWb30EUFjzQCE6jLLj9dgPm5be2u4N4ljriq5Up6l3RTd81ynC8UyNrmT8KElNy5%2bz8uxPHY3FdSDSgkJUuW3iF4SdT53bMvA8fAP2iOBxBMhGjy9d',
}
req = urllib2.Request(url, data, headers)
r = urllib2.urlopen(req)
a = r.read()
a = json.loads(a)
result = {}
count = 1
for i in a['songs']:
    result[count] = {}
    result[count]['title'] = i['title']
    result[count]['uploader'] = i['artist']
    result[count]['url'] = i['songId'] 
    print str(count) + ".  " + i['title'] + " -by- " + i['artist']
    count += 1


info_url = "http://www.myspace.com/Modules/PageEditor/Handlers/music/queue.ashx"
songId = raw_input('Which song so you want to download ?   ')
songId = result[int(songId)]['url']
data = "type=song&id=%s&at=1" %(songId)
headers = {
    'Hash':'MIGcBgkrBgEEAYI3WAOggY4wgYsGCisGAQQBgjdYAwGgfTB7AgMCAAECAmYDAgIAwAQIYLI97pYniaIEEEZ7OzdEz%2bIWLU44SUNWb30EUFjzQCE6jLLj9dgPm5be2u4N4ljriq5Up6l3RTd81ynC8UyNrmT8KElNy5%2bz8uxPHY3FdSDSgkJUuW3iF4SdT53bMvA8fAP2iOBxBMhGjy9d',
}
req = urllib2.Request(info_url, data, headers)
r = urllib2.urlopen(req)
a = r.read()
a = json.loads(a)
print a['streamURL']

