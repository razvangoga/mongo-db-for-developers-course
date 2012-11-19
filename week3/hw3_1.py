import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school_w3
students = db.students

def find():
	result = students.find()
	
	for doc in result:	
		minScore = { 'score': 101 }
		for score in doc['scores']:
			if(score['type'] == 'homework' and score['score'] < minScore['score']):
				minScore = score
		
		if(minScore['score'] != 101):
			doc['scores'].remove(minScore)
			students.save(doc)
	
find()