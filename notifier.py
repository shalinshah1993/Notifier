import httplib
import getpass
import base64
import re
import time
import serial
import fbconsole as fb
from urllib import urlretrieve
import imp
import sys

INTERVAL = 1 # check after INTERVAL minutes
serv = 'mail.google.com'
path = '/mail/feed/atom'
GMAIL = 0
FB = 1

def writeSer(type,data):
	try:
		if "linux" in sys.platform:
			ser = serial.Serial('/dev/ttyUSB0', 9600)
		elif "win" in sys.platform:
			ser = serial.Serial('COM0', 9600)
		if len(str(data)) == 1:
			data = '0' + str(data)
		else:
			data = str(data)
		ser.write(str(type) + data) 
	except serial.serialutil.SerialException:
		print 'Error writing to serial device - Please check if arduino is properly connected'

class Gmail:

	def count(self,data):
		matches = re.findall('<fullcount>([0-9]+)</fullcount>', data)
		if len(matches) == 0:
			print 'Error in parsing feed, check user name and password are correct'
			return 0
		return int(matches[0])

	def getfeed(self,auth):
		print 'Checking...'
		conn = httplib.HTTPSConnection(serv)
		conn.putrequest('GET', path)
		conn.putheader('Authorization', 'Basic %s'%auth)
		conn.endheaders()
		return conn.getresponse().read()

	def __init__(self):
		last_check = time.time() - INTERVAL*60 # subtract so that we check first time
		self.auth = base64.encodestring('%s:%s'%(raw_input('Username: '),getpass.getpass()))
		while True:
			if time.time() - last_check < INTERVAL*60:
				continue
			last_check = time.time()
			msgs = self.count(self.getfeed(self.auth))
			print msgs,'mails'
			writeSer(GMAIL,str(msgs))


class Facebook:

	def __init__(self):
		self.counter = 0
		#fb = imp.load_source('fb', '.fbconsole.py')
		fb.AUTH_SCOPE = ['read_stream','manage_notifications','read_mailbox','read_requests','user_status']
		#fb.ACCESS_TOKEN = "713005285382454|QXlQXvch37hPNejb7TuFZBFoulU"
		#fb.APP_ID = '713005285382454'
		fb.authenticate()		

		last_check = time.time() - INTERVAL*60 # subtract so that we check first time
		while True:
			if time.time() - last_check < INTERVAL*60:
				continue
			last_check = time.time()
			self.queryFB()
			#Counter of Notification
			if len(self.mail):
				self.counter += 1
			if len(self.notify):
				self.counter += len(self.notify)
			self.printNotification()
			writeSer(FB,self.counter)
			self.counter = 0
		
	def queryFB(self):
		#FQL's to get the notification
		self.userId = fb.fql("SELECT uid,name FROM user WHERE uid = me()")
		self.notify = fb.fql("SELECT notification_id,created_time,title_text FROM notification WHERE recipient_id = me() AND is_unread = 1")
		self.mail = fb.fql("SELECT name,unread_count FROM mailbox_folder WHERE folder_id = 0 AND viewer_id = me()")
		
	def printNotification(self):
		print "\nUser Id :", self.userId[0]["uid"] , "- User Name :", self.userId[0]["name"]
		print "No of notifications :", len(self.notify), "Unread Mails :", self.mail[0]['unread_count']
		print "Total Notifications :", self.counter

	def __del__(self):
		fb.logout() 

class fb_gmail():
	def __init__(self):
		print "Enter your GMAIL details:"
		self.auth = base64.encodestring('%s:%s'%(raw_input('Username: '),getpass.getpass()))
		print "Authenticating your FB details:"
		fb.AUTH_SCOPE = ['read_stream','manage_notifications','read_mailbox','read_requests','user_status']
		fb.authenticate()
		
		last_check1 = time.time() - INTERVAL * 60 # GMAIL check
		last_check2 = time.time() - INTERVAL * 60 + 30 # FB check
		fCounter = 0
		gCounter = 0
		
		while True:
			if time.time() - last_check1 > 60 * INTERVAL:
				last_check1 = time.time()
				gCounter = self.count(self.getfeed(self.auth))
				print "Unread Mails on GMAIL :", gCounter
				writeSer(GMAIL,str(gCounter))
				
			if time.time() - last_check2 > 60 * INTERVAL:
				last_check2 = time.time()
				userId = fb.fql("SELECT uid,name FROM user WHERE uid = me()")
				notify = fb.fql("SELECT notification_id,created_time,title_text FROM notification WHERE recipient_id = me() AND is_unread = 1")
				mail = fb.fql("SELECT name,unread_count FROM mailbox_folder WHERE folder_id = 0 AND viewer_id = me()")
				
				if len(mail):
					fCounter += 1
				if len(notify):
					fCounter += len(notify)
				writeSer(FB,fCounter)
				print "Notifiactions on FB :",fCounter
				fCounter = 0
				
	def getfeed(self,auth):
		conn = httplib.HTTPSConnection(serv)
		conn.putrequest('GET', path)
		conn.putheader('Authorization', 'Basic %s'%auth)
		conn.endheaders()
		return conn.getresponse().read()
	      
	def count(self,data):
		matches = re.findall('<fullcount>([0-9]+)</fullcount>', data)
		if len(matches) == 0:
			print 'Error in parsing feed, check user name and password are correct'
			return 0
		return int(matches[0])
	      
	def __del__(init):
		fb.logout()
			
if __name__ == '__main__':
	choice = input("Welome to Command line FB-Gmail Notifier:-\n-Please type '1' for GMAIL\n-Please type '2' for FB\n-Please type '3' for GMAIL and FB both\nYour input : ")
	if choice == 1:
		print "Started GMAIL Notification Service...."
		gmail = Gmail()
	elif choice == 2:
		print "Started FB Notification Service....."
		fb = Facebook()
	elif choice == 3:
		print "Started FB and GMAIL notification Service....."
		fb_gmail()
	else:
		print "Please enter a valid choice."
