
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db = connection.reddit
data = db.stories

def find():

  print "find, reporting for duty"
  query = {'title':{'$regex':'Google'}}    # this will return a cursor 
  projection = {'title':1, '_id':0}

  try:
	cursor = data.find(query,projection)

  except:
	print "Unexpected error:", sys.exc_info()[0]

  sanity = 0
  for doc in cursor:
	print doc
	sanity += 1
	if (sanity > 10):
		break
		  
find()
