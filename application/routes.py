from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacters

def format_character(character):
    return {
        'id': character.id,
        'name': character.name,
        'imageURL': character.imageURL,
        'age': character.age,
        'catch_phrase': character.catch_phrase
    }

@app.route('/')
def hello_world():
    return '<p>Hello World!!!</p>'

@app.route('/characters', methods=['GET','POST'])
def characters():
    if request.method == 'POST':
        data = request.json
        character = FriendsCharacters(data['name'], data['imageURL'], data['age'],data['catch_phrase'])
        db.session.add(character)
        db.session.commit()
        return jsonify(id=character.id, name=character.name, imageURL=character.imageURL, age=character.age, catch_phrase=character.catch_phrase)
    else:
        characters = FriendsCharacters.query.all()
        character_list = []
        for character in characters:
            character_list.append(format_character(character))
        return {'characters': character_list}

@app.route('/characters/<id>', methods=['GET', 'DELETE', 'PATCH'])
def character_id(id):
    if request.method == 'PATCH':
        character = FriendsCharacters.query.filter_by(id=id)
        data = request.json
        character.update(dict(name=data['name'],imageURL=character.imageURL, age=data['age'], catch_phrase=data['catch_phrase']))
        db.session.commit()
        updatedCharacter = character.first()
        return jsonify(id=updatedCharacter.id, name=updatedCharacter.name,imageURL=updatedCharacter.imageURL, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)
    elif request.method == 'DELETE':
        character = FriendsCharacters.query.filter_by(id=id).first()
        db.session.delete(character)
        db.session.commit()
        return 'Character deleted successfully'
    else:
        character = FriendsCharacters.query.filter_by(id=id).first()
        return jsonify(id=character.id, name=character.name,imageURL=character.imageURL, age=character.age, catch_phrase=character.catch_phrase)

    

    