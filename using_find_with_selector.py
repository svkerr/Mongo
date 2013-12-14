
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db = connection.school
scores = db.scores

def find():

  print "find, reporting for duty"
  query = {'type':'exam'}    # this will return a cursor 
  selector = {'student_id':1, '_id':0}

  try:
	cursor = scores.find(query,selector)

  except:
	print "Unexpected error:", sys.exc_info()[0]

  sanity = 0
  for doc in cursor:
	print doc
	sanity += 1
	if (sanity > 10):
		break
		  


def find_one():

  print "find one, reporting for duty"
  query = {'student_id':10}

  try:
	doc = scores.find_one(query)     
	# Note: due to pymongo driver, call to mongo is not findOne()

  except:
	print "Unexpected error:", sys.exc_info()[0]

  print doc

# Execute calls
# find_one()
find()
