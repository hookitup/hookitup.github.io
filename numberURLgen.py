#This is a script that runs every second to update an index.html page
#   Author: Cheatstapher
#   Version: 1
#   Date: 12/21/2017

import time, threading, datetime

windir = 'c:\\Users\\clebron\\Downloads\\pythonStuff\\numberLink.html'
lindir = '/home/xt2/Documents/numberLink.html'

datte = str(datetime.datetime.now())
num = 0
logtofile = 0

seconds = 0
minutes = 0
hours = 0
days = 0
years = 0

itCount = 0
timeEnd = time.time() + 1

def func1():
    while True:
        global num
        global logtofile
        logtofile = logtofile + 1
        num = num + 1
        if logtofile == itCount:
            print('<html><head><META HTTP-EQUIV="refresh" CONTENT="1">'
                  '<title>Python while loop</title></head>'
                  '<body><b>Born:</b> ' + datte + '</br>'
                  "I'v been alive for " + str(num) + ' Python while loops.</br>'
                  '<font color="red">' + str(itCount) + '</font> iterations every second on my current CPU.</body></br>'
                  '</br><b>Started:</b></br>'
                  'Seconds: ' + str(seconds) + '</br>'
                  'Minutes: ' + "{0:0.1f}".format(minutes) + '</br>'
                  'Hours: ' + "{0:0.1f}".format(hours) + '</br>'
                  'Days: ' + "{0:0.1f}".format(days) + '</br>'
                  'Years: ' + "{0:0.1f}".format(years) + '</br>'
                  '</br>'
                  '</br><b>Code:</b></br>'
                  '<font color=#95A5A6>num</font> <b>=</b> <font color=#8E44AD>0</font></br>'
                  '<font color=#E67E22>while True</font><b>:</b></br>'
                  '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <font color=#95A5A6>num</font> <b>=</b> <font color=#95A5A6>num</font> <b>+</b> <font color=#8E44AD>1</font></br>'
                  '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <font color=#3498DB>print</font><b>(</b><font color=#2ECC71>num to html page</font><b>)</b></br>'
                  '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <font color=#E67E22>continue</font>'
                  '</html>', file=open(windir, 'w'))
            logtofile = 0
            continue
        else:
            continue

def func2():
    while True:
        global seconds
        global minutes
        global hours
        global days
        global years
        seconds = seconds + 1
        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24
        years = days / 365.25
        time.sleep(1)

while time.time() < timeEnd:
    itCount = itCount + 1

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t2.start()
t1.start()

