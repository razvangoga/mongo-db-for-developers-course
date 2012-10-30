import bottle
import pymongo

#web server root route
@bottle.route('/')
def home_page():
	return "Hello World\n"
	
#web server other route
@bottle.route('/testpage')
def test_page():
	return "Hello Test page\n"	

#added to make the web server watch the files for chages (and not need restart)
bottle.debug(True)
bottle.run(host='localhost', port=8082)