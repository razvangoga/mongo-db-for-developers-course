person = {'name':'RG', 'color':'red', 'hair':'brown', 'interests' : ['cycling','running','biking'] }

for key in person:
	if (key == 'interests'):
		print "Interests...."
		for interest in person[key]:
			print "\tinterest is " + interest
	else:
		print "key is " + key + " value is " + person[key]