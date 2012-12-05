db.cities.aggregate([
    {$project: 
     {
		first_char: {$substr : ["$city",0,1]},
		pop:1,
		_id:0
     }},
	{$match: { first_char : { $in : ['0','1','2','3','4','5','6','7','8','9'] }}},
	{$group: { _id : null, pop_count: { $sum: "$pop" } } }
])