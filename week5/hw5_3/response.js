db.grades.aggregate([
	{$unwind : "$scores"},
	{$match: { 'scores.type' : { $ne: 'quiz' } }},
	{$group : { _id : { sid : "$student_id", cid : "$class_id" },  std_cls_avg : { $avg : "$scores.score" }}},
	{$group : { _id: "$_id.cid", cls_avg : {$avg: "$std_cls_avg"} }},
	{$sort : { cls_avg : -1} }
])