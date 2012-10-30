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
		<p>
			<form action="/favourite_fruit" method="POST">
				<fieldset>
					<legend>What is your favourite fruit?</legend>
					<input type="text" name="fruit" />
					<br />
					<input type="submit" value="Submit" />					
				</fieldset>
			</form>
		</p>
	</body>
</html>