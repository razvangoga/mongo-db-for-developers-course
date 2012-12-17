//validate
db.messages.find({$and: [
	{ "headers.From": "andrew.fastow@enron.com"  },
	{ "headers.To": "john.lavorato@enron.com" }
	]}).count()
	
//response
db.messages.find({$and: [
	{ "headers.From": "andrew.fastow@enron.com"  },
	{ "headers.To": "jeff.skilling@enron.com" }
	]}).count()	