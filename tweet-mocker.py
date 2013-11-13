import twython, time, sys
from twython import Twython, TwythonError

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
APP_KEY="XXXXXXXXXXXXXXXXXXXXX"
APP_SECRET="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
OAUTH_TOKEN="999999999-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
OAUTH_TOKEN_SECRET="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

target = "desired-twitter-account-to-watch-here"
while True:
  print time.asctime(time.localtime())
  # get last status
  status = twitter.show_user(screen_name=target)["status"]
  # get a particular status
  # status = twitter.show_status(id="999999999999999999")
  
  # if file 'laststatuses' doesn't exist, create it
  try: 
    open('laststatuses','r').close()
  except:
    open('laststatuses', 'w').close()

  # print contents of "laststatuses" file to the console, for reference
  f = open('laststatuses','r')
  laststatuses = []
  for line in f.readlines():
    line = line.rstrip()
    if line:
      laststatuses.append(line)
  for x in laststatuses:
    print x
  f.close()

  print "status.id: "
  print status["id"]
  print "laststatuses:"
  print laststatuses
  print "match?"
  print any(str(status["id"]) in s for s in laststatuses)

  # check laststatuses to see if the captured tweet is new
  if not any(str(status["id"]) in s for s in laststatuses):
    print "Last @"+target+" status: " + str(status["id"]) + " : " + status["text"].encode('utf-8')
    
    # modify the tweet here!
    # here's a sample substitution
    newstatus = status["text"].replace("dogs", "cats", 1)

    print "New @"+target+" status: " + newstatus.encode('utf-8')

    # if no change was made, exit
    if newstatus == status["text"]:
      sys.exit()
  
    #tweet it
    try:
      print "tweeting"
      twitter.update_status(status=newstatus)
      laststatuses.insert(0, str(status["id"]))
    except Exception, exception:
      print "Error:"
      print exception
    

    limit = 4
    print "len(laststatuses): " + str(len(laststatuses))
    if len(laststatuses) > limit:
      laststatuses = laststatuses[0:limit]
    print "New laststatuses:"
    print '[%s]' % ', '.join(map(str, laststatuses))

    f = open('laststatuses','w')
    for item in laststatuses:
      f.write("%s\n" % item)
    f.close()

  print 'Sleeping... \n'
  time.sleep(3600)
