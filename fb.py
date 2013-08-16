import fbconsole
from urllib import urlretrieve
import imp

USERNAME = "shalinshah1993@gmail.com"
PASWORD = "xyz"
APP_SECRET = "435b9a7786e1773168de0c2f30242b66"
REDIRECT_URI = "https://127.0.0.1:8080"

counter = 0
fb = imp.load_source('fb', 'fbconsole.py')
fb.AUTH_SCOPE = ['read_stream','manage_notifications','read_mailbox','read_requests','user_status']
fbconsole.ACCESS_TOKEN = "713005285382454|QXlQXvch37hPNejb7TuFZBFoulU"
fbconsole.APP_ID = '713005285382454'

"""
fbconsole.automatically_authenticate(
    USERNAME,     # facebook username for authentication
    PASSWORD,     # facebook password for authentication
    APP_SECRET,   # "app secret" from facebook app settings
    REDIRECT_URI, # redirect uri specified in facebook app settings
    True
)
"""
fb.authenticate()

#FQL's to get the notification
userId = fb.fql("SELECT uid,name FROM user WHERE uid = me()")
notify = fb.fql("SELECT notification_id,created_time,title_text FROM notification WHERE recipient_id = me() AND is_unread = 1")
mail = fb.fql("SELECT name,unread_count FROM mailbox_folder WHERE folder_id = 0 AND viewer_id = me()")

#Cunter of Notification
if len(mail):
	counter += 1
if len(notify):
	counter += len(notify) 

print "\n\nUser Id :", userId[0]["uid"] , "- User Name :", userId[0]["name"]
print "No of notifications :", len(notify), "Unread Mails :", mail[0]['unread_count']
print "Total Notifications :", counter

fbconsole.logout()
#import urllib

#query = "SELECT title_html FROM notification WHERE recipient_id = " + str(userId[0]['uid'])
#print(query) 

#query = urllib.quote(query)
#print(query) 

#url1 = "https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id=713005285382454&client_secret=435b9a7786e1773168de0c2f30242b66"
#data = urllib.urlopen(url1).read()
#print data.split("=")[1]

#url = "https://graph.facebook.com/fql?q=" + query + "&access_token=100002187233865"
#data = urllib.urlopen(url).read()
#print(data)
