db.messages.aggregate([
	{ $unwind : "$headers.To" },
	{ $group: { _id: { from : "$headers.From", to : "$headers.To" }, mail_count : { $sum : 1 } }},
	{$sort: { 'mail_count' : -1 }},
	{ $limit : 10 }
])