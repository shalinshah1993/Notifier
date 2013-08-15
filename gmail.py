import httplib
import getpass
import base64
import re
import time
import serial

INTERVAL = 1 # check every INTERVAL minutes

serv = 'mail.google.com'
path = '/mail/feed/atom'

auth = base64.encodestring('%s:%s'%(raw_input('Username: '),getpass.getpass()))

def count(data):
 matches = re.findall('<fullcount>([0-9]+)</fullcount>', data)
 if len(matches) == 0:
     print 'Error in parsing feed, check user name and password are correct'
     return 0
 return int(matches[0])

def getfeed():
 print 'Checking...'
 conn = httplib.HTTPSConnection(serv)
 conn.putrequest('GET', path)
 conn.putheader('Authorization', 'Basic %s'%auth)
 conn.endheaders()
 return conn.getresponse().read()

def writeSer(data):
 try:
     #ser = serial.Serial('/dev/ttyUSB0')
     ser = serial.Serial('/dev/ttyUSB0', 9600)
     ser.write(data) 
 except serial.serialutil.SerialException:
     print 'Error writing to serial device'
     raise

last_check = time.time() - INTERVAL*60 # subtract so that we check first time

while True:
    if time.time() - last_check < INTERVAL*60:
        continue
    last_check = time.time()
    msgs = count(getfeed())
    print msgs,'mails'
    writeSer(str(msgs))	
