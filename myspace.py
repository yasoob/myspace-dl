#!/usr/bin/env 
 
import urllib2
import json
import re
import subprocess

print "Myspace music downloader made by Yasoob <yasoob.khld@gmail.com>"
print "This program uses rtmpdump for downloading"

url = 'http://www.myspace.com/Modules/PageEditor/Handlers/Music/SearchMusic.ashx'
song = raw_input('\nwhich song do you want  to search for?  ')
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
    result[count]['title'] = (i['title'].replace("<em>","")).replace("</em>","")
    result[count]['uploader'] = i['artist']
    result[count]['url'] = i['songId'] 
    print str(count) + ".  " + result[count]['title'] + " -by- " + result[count]['uploader']
    count += 1


info_url = "http://www.myspace.com/Modules/PageEditor/Handlers/music/queue.ashx"
songId = raw_input('Which song so you want to download ?   ')
name = result[int(songId)]['title']
songId = result[int(songId)]['url']
data = "type=song&id=%s&at=1" %(songId)
req = urllib2.Request(info_url, data, headers)
r = urllib2.urlopen(req)
a = r.read()
a = json.loads(a)
streamURL = "mp4:"+a['streamURL'].split(".com/")[1]
print streamURL
cmd = 'rtmpdump -r "rtmpte://fms.ec-music.myspacecdn.com/" -a "" -f "LNX 11,2,202,235" -o "{}.flv" - -W "http://lads.myspacecdn.com/music/sdkwrapper/SDKWrapper.2.2.16.swf?ili=false&pguid=bd1ab4fde7b84b7089e5ed714007719e&pertid64=-6868838582826384204&cip=115.167.69.194&sip=172.16.0.2&hash=MIGmBgkrBgEEAYI3WAOggZgwgZUGCisGAQQBgjdYAwGggYYwgYMCAwIAAQICZgMCAgDABAg30iVjjk7mowQQADI7jEQRqtXEHalqOxdJbwRYHt7ZytsvewZpywM16%252fvP58Ii0sDljgh97xfuXDzKDYiI%252fjPiID7lEVopr2XgVMyOVbgdqfEotNmXWlPL6ORFvJ8fjk4hPQEBKkudN9zd0WHsFN190OHl8A%253d%253d&pertid=b4c4229bb3fbaca00000000000000000&ptype=30&hostenv=www.&uid=-1&pcc=en-US&cc=en-US" -p "http://www.myspace.com" -y "{}"'.format(name,streamURL)
p = subprocess.Popen(cmd, shell=True)
p.wait()
print "song downloaded."


