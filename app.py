from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mongodb'
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/mongodb'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'Irrrrrrrrrru'})

@app.route('/lang', methods=['GET'])
def return_all():
    languages = mongo.db.languages
    output = []

    for value in languages.find():
        output.append({'_id': str(value['_id']), 'name': value['name']})

    return jsonify({'languages': output})

@app.route('/lang/<string:name>', methods=['GET'])
def return_one(name):
    language = mongo.db.languages
    search = language.find_one({'name': name})
    if search:
        output = {'_id': str(search['_id']), 'name': search['name']}
    else:
        output = "No such name"
    return jsonify({'language': output})

@app.route('/lang', methods=['POST'])
def create():
    language = mongo.db.languages
    name = request.json['name']
    language_id = language.insert({'name': name})
    new_language = language.find_one({'_id': language_id})
    output = {'name': new_language['name']}
    return jsonify({'language': output})

@app.route('/lang/<language_id>', methods=['PUT'])
def udpdate(language_id):
    language = mongo.db.languages
    try:
        language.update_one(
                { '_id': ObjectId(language_id) },
                {
                    '$set': {
                            'name': request.json['name']
                    }
                })
        output = {'language': request.json['name']}
    except:
        print(str('teste'))

    return jsonify({'language': output})

@app.route('/lang/<language_id>', methods=['DELETE'])
def delete(language_id):
    language = mongo.db.languages
    delete = language.delete_many({
        '_id': ObjectId(language_id)
    })
    return jsonify({'languages': "Remove success"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
