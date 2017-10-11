from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/restdb'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'Irrrrrrrrrru' })

@app.route('/lang', methods=['GET'])
def return_all():
	languages = mongo.db.languages
	output = []

	for value in languages.find():
		output.append({'name': value['name']})

	return jsonify({'languages': output})

@app.route('/lang/<string:name>', methods=['GET'])
def return_one(name):
    language = mongo.db.languages
    search = language.find_one({'name': name})
    if search:
        output = {'name': search['name']}
    else:
        output = "No such name"
    return jsonify({'result': output})

@app.route('/lang', methods=['POST'])
def add_one():
    language = mongo.db.languages
    name = request.json['name']
 
    language_id = language.insert({'name': name})
    new_language = language.find_one({'_id': language_id })
    output = {'name' : new_language['name']}
    return jsonify({'result' : output}) 

@app.route('/lang/<string:name>', methods=['PUT'])
def edit_one(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'languages': langs[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
def remove_one(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
