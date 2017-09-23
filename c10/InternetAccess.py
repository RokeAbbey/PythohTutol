#coding=utf-8
import urllib2
u = urllib2.urlopen(u'http://tycho.usno.navy.mil/cgi-bin/timer.pl')
print u'in with'
print u
for line in u:
    #print line
    if u'EDT' in line:
        print line
