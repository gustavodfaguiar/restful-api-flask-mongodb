from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name': 'Javascript',}, {'name': 'Python'}, {'name': 'Ruby'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works! irrru!'})

@app.route('/lang', methods=['GET'])
def return_all():
    return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['GET'])
def return_one(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})

@app.route('/lang', methods=['POST'])
def add_one():
    language = {'name': request.json['name']}
    languages.append(language)
    return jsonify({'languages': languages})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
