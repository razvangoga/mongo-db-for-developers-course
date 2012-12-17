db.images.aggregate([
	{ $group : { _id: null, sum : { $sum : "$_id" } }}
])