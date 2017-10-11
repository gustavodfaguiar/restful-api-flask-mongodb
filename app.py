from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works! irrru!'})

@app.route('/lang', methods=['GET'])
def return_all():
	languagens = mongo.db.languages
	output = []

	for value in languages.find():
		output.append({'name': value['name']})

	return jsonify({'languages': output})

@app.route('/lang/<string:name>', methods=['GET'])
def return_one(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})

@app.route('/lang', methods=['POST'])
def add_one():
    language = {'name': request.json['name']}
    languages.append(language)
    return jsonify({'languages': languages})

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
    app.run(debug=True, port=8080)
