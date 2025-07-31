from flask import Flask
from flask_migrate import Migrate
from models import db, Animal, Zookeeper, Enclosure

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if not animal:
        return "<h1>Animal not found</h1>", 404

    return f"""
        <ul>Name: {animal.name}</ul>
        <ul>Species: {animal.species}</ul>
        <ul>Zookeeper: {animal.zookeeper.name}</ul>
        <ul>Enclosure: {animal.enclosure.environment}</ul>
    """

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zk = Zookeeper.query.get(id)
    if not zk:
        return "<h1>Zookeeper not found</h1>", 404

    animals_list = "".join([f"<ul>Animal: {animal.name}</ul>" for animal in zk.animals])
    return f"""
        <ul>Name: {zk.name}</ul>
        <ul>Birthday: {zk.birthday}</ul>
        {animals_list}
    """

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enc = Enclosure.query.get(id)
    if not enc:
        return "<h1>Enclosure not found</h1>", 404

    animals_list = "".join([f"<ul>Animal: {animal.name}</ul>" for animal in enc.animals])
    return f"""
        <ul>Environment: {enc.environment}</ul>
        <ul>Open to Visitors: {enc.open_to_visitors}</ul>
        {animals_list}
    """


if __name__ == '__main__':
    app.run(port=5555, debug=True)
