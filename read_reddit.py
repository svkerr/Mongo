import json
import urllib2
import pymongo

# connect to mongo
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the reddit database
db=connection.reddit
stories = db.stories

# get the reddit home page
# reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")

# parse the json into python objects
# NOTE: class video uses different approach.but since i curled file, simply open the file etc.,

with open('reddit_page','r',) as f:
  parsed = json.load(f)

# parsed = json.load(reddit_page.read() )

# iterate through every news item on the page
for item in parsed['data']['children']:
  # put it in mongo
  stories.insert(item['data'])

