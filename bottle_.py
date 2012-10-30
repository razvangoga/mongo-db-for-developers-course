import bottle
import pymongo

#web server root route
@bottle.route('/')
def home_page():
	fruits = ['apple', 'orange', 'grape', 'peach', 'banana']
	return bottle.template('bottle_index', username="rg", model=fruits);
	
#web server alternate route
@bottle.route('/2')
def home_page():
	fruits = ['apple', 'orange', 'grape', 'peach', 'banana']
	return bottle.template('bottle_index',  { "username":"rg", "model":fruits });

#web server post favourite fruit route	
@bottle.post('/favourite_fruit')
def favourite_fruit():
	fruit = bottle.request.forms.get("fruit");
	
	if(fruit == None or fruit == ""):
		fruit = "No fruit selected"
	
	bottle.response.set_cookie("fruit", fruit)
	bottle.redirect("/show_fruit")

#web server show fruit route
@bottle.route('/show_fruit')
def show_fruit():
	fruit = bottle.request.get_cookie("fruit")
	return bottle.template('bottle_fruit_selected',  { "fruit":fruit });
	
#added to make the web server watch the files for chages (and not need restart)
bottle.debug(True)
bottle.run(host='localhost', port=8082)