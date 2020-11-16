from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
	{
		'name': 'My woderful store',
		'item': [
			{
				'name': 'My item',
				'price': '15.99',
			}
			]
	}
]

''' Since, we are acting like a server, when we receive post request then we get data and deal with it
when we receive get request then we send data. '''

''' Note: By default, app.route() always do 'GET' request,
if we want it to respond to other request as well then, we have to specify methods. '''

# POST - used to receive data
# GET - used to send data back only


@app.route('/')
def home():
	return render_template('index.html')

# used to create a new store with a given name
# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
	request_data = request.get_json()
	new_store = {
		'name': request_data['name'],
		'items': []
	}
	stores.append(new_store)
	return jsonify(new_store)


# used to get a store with given name and will send some data about it.
# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify(store)
	return jsonify({'message': 'store not found'})

# return a list of all stores
# GET /store
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})

# create an item inside specific store {name:, price:}
# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name:
			new_item = {
				'name': request_data['name'],
				'price': request_data['price']
			}
			store['item'].append(new_item)
			return jsonify(new_item)
	return jsonify({'message': 'store not found'})


# get all the item in a specific store
# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({'items': store['item']})
	return jsonify({'message': 'store not found'})

app.run(port = 5000)
