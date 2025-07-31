from app import app, db
from models import Animal, Zookeeper, Enclosure

with app.app_context():
    print("Clearing old data...")
    Animal.query.delete()
    Zookeeper.query.delete()
    Enclosure.query.delete()

    print("Seeding database...")

    # Zookeepers
    zk1 = Zookeeper(name="Dylan Taylor", birthday="1990-06-12")
    zk2 = Zookeeper(name="Stephanie Contreras", birthday="1996-09-20")
    db.session.add_all([zk1, zk2])

    # Enclosures
    enc1 = Enclosure(environment="trees", open_to_visitors=True)
    enc2 = Enclosure(environment="pond", open_to_visitors=False)
    db.session.add_all([enc1, enc2])

    # Animals
    a1 = Animal(name="Logan", species="Snake", zookeeper=zk1, enclosure=enc1)
    a2 = Animal(name="Lilly", species="Tiger", zookeeper=zk2, enclosure=enc2)
    a3 = Animal(name="Bobby", species="Giraffe", zookeeper=zk1, enclosure=enc1)
    db.session.add_all([a1, a2, a3])

    db.session.commit()
    print("Done seeding!")
