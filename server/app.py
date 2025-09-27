from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)

# Database configuration (SQLite for this lab)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "supersecretkey"  # Needed for sessions if any

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    reviews = db.relationship('Review', back_populates='customer')
    items = association_proxy('reviews', 'item')  # association proxy to get items directly

class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    reviews = db.relationship('Review', back_populates='item')

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    customer = db.relationship('Customer', back_populates='reviews')
    item = db.relationship('Item', back_populates='reviews')

# Optional: simple route to test server
@app.route('/')
def index():
    return "Flask-SQLAlchemy Lab 2 is running!"

# Run app
if __name__ == '__main__':
    app.run(debug=True)
