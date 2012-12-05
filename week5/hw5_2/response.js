db.cities.aggregate([
	{$match: { $or: [ 
			{state: 'CT'}, 
			{state: 'NJ'}
			] }},
    {$group : { _id: { state: "$state", city: "$city" }, city_pop : { $sum : "$pop" }  }  },
	{$match : { city_pop : { $gt:25000}}},
	{$group : { _id: null,  avg_pop: { $avg: "$city_pop" }} } 
])

db.cities.aggregate([
	{$match: { $or: [ 
			{state: 'CA'}, 
			{state: 'NY'}
			] }},
    {$group : { _id: { state: "$state", city: "$city" }, city_pop : { $sum : "$pop" }  }  },
	{$match : { city_pop : { $gt:25000}}},
	{$group : { _id: null,  avg_pop: { $avg: "$city_pop" }} } 
])