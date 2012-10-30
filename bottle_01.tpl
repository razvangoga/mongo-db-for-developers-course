<!DOCTYPE html>
<html>
	<head>
		<title>Hello World!</title>
	</head>
	<body>
		<p>Welcome {{username}}</p>
		<p>
			<ul>
				%for item in model:
					<li>{{item}}</li>
				%end
			</ul>
		</p>
	</body>
</html>