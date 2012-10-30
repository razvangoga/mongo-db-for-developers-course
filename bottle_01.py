import bottle
import pymongo

#web server root route
@bottle.route('/')
def home_page():
	fruits = ['apple', 'orange', 'grape', 'peach', 'banana']
	return bottle.template('bottle_01', username="rg", model=fruits);
	
#web server alternate route
@bottle.route('/2')
def home_page():
	fruits = ['apple', 'orange', 'grape', 'peach', 'banana']
	return bottle.template('bottle_01',  { "username":"rg", "model":fruits });	
	
#added to make the web server watch the files for chages (and not need restart)
bottle.debug(True)
bottle.run(host='localhost', port=8082)