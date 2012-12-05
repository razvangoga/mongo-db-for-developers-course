db.posts.aggregate([
	{ $unwind: "$comments" }, 
	{$group: { _id: "$comments.author", post_count : { $sum : 1 }}},
	{$sort: { 'post_count' : -1 }}
])