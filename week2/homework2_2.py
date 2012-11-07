import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades

def find():
	query = {'type':'homework'}
	result = grades.find(query).sort([('student_id',pymongo.DESCENDING),('score',pymongo.DESCENDING)])
	
	sid = ''
	iid = ''
	for doc in result:	
		if(sid == ''):
			sid = doc['student_id']
		
		if(sid != doc['student_id']):
			grades.remove({'_id': iid})
			sid = doc['student_id']
        
		iid = doc['_id']
	grades.remove({'_id':iid})
	
find()