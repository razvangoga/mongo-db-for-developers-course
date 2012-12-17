import pymongo

connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.photo
images = db.images
albums = db.albums

result = images.find()

imagesToRemove = []

for image in result:
	containingAlbums = albums.find({'images': image['_id']})
	
	if(containingAlbums.count() == 0):
		imagesToRemove.append(image['_id'])
		
for iid in imagesToRemove:
	images.remove({'_id': iid})